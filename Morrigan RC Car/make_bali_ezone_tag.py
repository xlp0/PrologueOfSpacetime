#!/usr/bin/env python3
"""Generate a manifold 'Bali E-Zone' replacement dashboard nameplate STL and
anti-scorch White PLA Snapmaker Orca .3mf plate for the Morrigan 1:8 4x4 Buggy.
"""

from collections import Counter, defaultdict
import json
import math
import os
import struct
import sys
import zipfile
import xml.etree.ElementTree as ET

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path as MplPath
from matplotlib.patches import PathPatch

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PRINT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, PRINT_ROOT)

import make_named_keychain as mnk  # noqa: E402

SOURCE_STL = os.path.join(SCRIPT_DIR, "STLs", "011DashPassClover.stl")
OUT_STL = os.path.join(SCRIPT_DIR, "STLs", "011DashPass_BaliEZone.stl")
TEMPLATE_3MF = os.path.join(SCRIPT_DIR, "Morrigan_Plate3_RoofCage_And_3WheelRings.3mf")
OUT_3MF = os.path.join(SCRIPT_DIR, "Morrigan_DashTag_BaliEZone_White.3mf")
FONT_PATH = r"C:\Windows\Fonts\arialbd.ttf"
PREVIEW_PNG = (
    r"C:\Users\andre\.gemini\antigravity\brain\2af96bf9-b351-47a2-b229-d78f50df01f0"
    r"\scratch\bali_ezone_preview.png"
)

TAG_TEXT = "Bali E-Zone"
TARGET_TEXT_WIDTH_MM = 51.5
TEXT_Y_MIN_MM = 5.50
Z_BASE = 1.5000
Z_TOP = 2.3000
BED_CENTER_X = 135.5
BED_CENTER_Y = 136.0


def read_binary_stl(path):
    """Read vertices of all triangles from a binary STL."""
    with open(path, "rb") as f:
        f.read(80)
        count = struct.unpack("<I", f.read(4))[0]
        tris = []
        for _ in range(count):
            d = struct.unpack("<12fH", f.read(50))
            tris.append((d[3:6], d[6:9], d[9:12]))
    return tris


def extract_base_shell(stl_path):
    """Return shifted base-shell triangles (<Z=1.5) and CCW top rim polygon."""
    raw_tris = read_binary_stl(stl_path)
    x0 = min(v[0] for t in raw_tris for v in t)
    y0 = min(v[1] for t in raw_tris for v in t)
    z0 = min(v[2] for t in raw_tris for v in t)
    x1 = max(v[0] for t in raw_tris for v in t)
    center_x = 0.5 * (x1 - x0)

    def shift_pt(v):
        sx = round(v[0] - x0, 4)
        sy = round(v[1] - y0, 4)
        sz = round(v[2] - z0, 4)
        if 1.49 <= sz <= 1.505:
            sz = Z_BASE
        return (sx, sy, sz)

    kept = []
    z0_tris_2d = []
    for t in raw_tris:
        st = tuple(shift_pt(v) for v in t)
        zs = [v[2] for v in st]
        if max(zs) > Z_BASE + 0.001:
            continue
        if all(abs(z - Z_BASE) < 0.005 for z in zs):
            continue
        if all(abs(z - 1.25) < 0.005 for z in zs):
            continue
        kept.append(st)
        if all(abs(z) < 0.005 for z in zs):
            z0_tris_2d.append([(v[0], v[1]) for v in st])

    ec = Counter()
    for v0, v1, v2 in kept:
        for a, b in ((v0, v1), (v1, v2), (v2, v0)):
            if a != b:
                ec[(a, b)] += 1

    unmatched = [(a, b) for (a, b), c in ec.items() if ec.get((b, a), 0) != c]
    adj = defaultdict(list)
    for a, b in unmatched:
        adj[a].append(b)

    visited = set()
    loops = []
    for a, b in unmatched:
        if (a, b) in visited:
            continue
        loop = [a]
        cur = b
        visited.add((a, b))
        while cur != a and len(loop) < 5000:
            loop.append(cur)
            nxts = [nxt for nxt in adj[cur] if (cur, nxt) not in visited]
            if not nxts:
                break
            nxt = nxts[0]
            visited.add((cur, nxt))
            cur = nxt
        loops.append((loop, cur == a))

    if len(loops) != 1 or not loops[0][1]:
        raise RuntimeError(f"Expected 1 closed rim loop, got {len(loops)} loops: {[(len(l), c) for l, c in loops]}")

    rim_2d = [(p[0], p[1]) for p in loops[0][0]]
    top_outer_ccw = mnk.ensure_ccw(rim_2d)
    return kept, top_outer_ccw, center_x, z0_tris_2d


def point_seg_dist(px, py, ax, ay, bx, by):
    """Return shortest Euclidean distance from point P to segment AB."""
    abx, aby = bx - ax, by - ay
    ab2 = abx * abx + aby * aby
    if ab2 < 1e-12:
        return math.hypot(px - ax, py - ay)
    t = max(0.0, min(1.0, ((px - ax) * abx + (py - ay) * aby) / ab2))
    return math.hypot(px - (ax + t * abx), py - (ay + t * aby))


def min_dist_to_poly_edges(pt, poly):
    px, py = pt
    n = len(poly)
    return min(point_seg_dist(px, py, poly[i][0], poly[i][1], poly[(i + 1) % n][0], poly[(i + 1) % n][1]) for i in range(n))


def layout_tag_shapes(text, font_path, center_x, y_min_target, target_width, top_outer_ccw):
    """Parse TTF outlines, center on badge, validate boundary clearance."""
    ttf = mnk.TTFParser(font_path)
    probe = ttf.layout_word(text, 1.0 / ttf.units_per_em)
    pxs = [p[0] for c in probe for p in c]
    pys = [p[1] for c in probe for p in c]
    raw_w = max(pxs) - min(pxs)
    scale = (target_width / raw_w) / ttf.units_per_em

    scaled_probe = ttf.layout_word(text, scale)
    sxs = [p[0] for c in scaled_probe for p in c]
    sys_ = [p[1] for c in scaled_probe for p in c]
    dx = center_x - 0.5 * (min(sxs) + max(sxs))
    dy = y_min_target - min(sys_)

    contours = ttf.layout_word(text, scale, offset_x=dx, offset_y=dy)
    shapes = mnk.classify_word_contours(contours)

    min_margin = float("inf")
    for outer_ccw, holes_cw in shapes:
        for pt in outer_ccw + [p for h in holes_cw for p in h]:
            if not mnk.point_in_poly(pt[0], pt[1], top_outer_ccw):
                raise RuntimeError(f"Text vertex {pt} falls outside badge rim!")
            d = min_dist_to_poly_edges(pt, top_outer_ccw)
            if d < min_margin:
                min_margin = d
    if min_margin < 2.0:
        raise RuntimeError(f"Text too close to curved badge border: {min_margin:.3f} mm (< 2.0 mm)")

    fxs = [p[0] for o, _ in shapes for p in o]
    fys = [p[1] for o, _ in shapes for p in o]
    stats = {
        "shapes": len(shapes),
        "holes": sum(len(h) for _, h in shapes),
        "x_range": (min(fxs), max(fxs)),
        "y_range": (min(fys), max(fys)),
        "min_margin_mm": min_margin,
    }
    return shapes, stats


def build_manifold_tag(kept_base, top_outer_ccw, shapes):
    """Stitch base shell, Z=1.5000 shelf, and extruded Z=1.5000..2.3000 letters."""
    tris_3d = list(kept_base)

    # Top flat face of badge base around extruded letter islands
    shelf_holes_cw = [mnk.ensure_cw(o) for o, _ in shapes]
    for a, b, c in mnk.triangulate_polygon_with_holes(top_outer_ccw, shelf_holes_cw):
        tris_3d.append(((a[0], a[1], Z_BASE), (b[0], b[1], Z_BASE), (c[0], c[1], Z_BASE)))

    # Counter floors inside enclosed letters (B, a, o, e) at Z_BASE
    for _, inner_holes_cw in shapes:
        for h_cw in inner_holes_cw:
            for a, b, c in mnk.triangulate_polygon_with_holes(mnk.ensure_ccw(h_cw), []):
                tris_3d.append(((a[0], a[1], Z_BASE), (b[0], b[1], Z_BASE), (c[0], c[1], Z_BASE)))

    # Raised letter walls + top caps from Z_BASE -> Z_TOP
    for o_ccw, inner_holes_cw in shapes:
        mnk.add_wall_strip(tris_3d, o_ccw, Z_BASE, Z_TOP)
        for h_cw in inner_holes_cw:
            mnk.add_wall_strip(tris_3d, h_cw, Z_BASE, Z_TOP)
        for a, b, c in mnk.triangulate_polygon_with_holes(o_ccw, inner_holes_cw):
            tris_3d.append(((a[0], a[1], Z_TOP), (b[0], b[1], Z_TOP), (c[0], c[1], Z_TOP)))

    if not mnk.verify_manifold(tris_3d):
        raise RuntimeError("Generated 011DashPass_BaliEZone mesh failed verify_manifold()!")
    return tris_3d


def render_preview(top_outer_ccw, z0_tris_2d, shapes, out_png, stats):
    """Save a crisp 2D top-down preview showing badge border, text, and margins."""
    os.makedirs(os.path.dirname(out_png), exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 3.2), dpi=180)
    ax.set_facecolor("#263238")
    for tri2d in z0_tris_2d:
        xs = [p[0] for p in tri2d] + [tri2d[0][0]]
        ys = [p[1] for p in tri2d] + [tri2d[0][1]]
        ax.fill(xs, ys, color="#DCE3E8", linewidth=0)

    rim_xs = [p[0] for p in top_outer_ccw] + [top_outer_ccw[0][0]]
    rim_ys = [p[1] for p in top_outer_ccw] + [top_outer_ccw[0][1]]
    ax.fill(rim_xs, rim_ys, color="#FFFFFF", edgecolor="#90A4AE", linewidth=1.2)

    for outer_ccw, holes_cw in shapes:
        verts = []
        codes = []
        for ring in [outer_ccw] + holes_cw:
            verts.extend(ring + [ring[0]])
            codes.extend([MplPath.MOVETO] + [MplPath.LINETO] * (len(ring) - 1) + [MplPath.CLOSEPOLY])
        patch = PathPatch(MplPath(verts, codes), facecolor="#111111", edgecolor="#000000", linewidth=0.5)
        ax.add_patch(patch)

    ax.set_aspect("equal")
    ax.set_xlim(-2, 62.5)
    ax.set_ylim(-2, 22)
    xr, yr = stats["x_range"], stats["y_range"]
    ax.set_title(
        f"011DashPass_BaliEZone (60.25 x 20.00 mm) | Text X:[{xr[0]:.1f},{xr[1]:.1f}] Y:[{yr[0]:.1f},{yr[1]:.1f}] | Min border clearance: {stats['min_margin_mm']:.2f} mm",
        fontsize=9,
    )
    ax.set_xlabel("X (mm)")
    ax.set_ylabel("Y (mm)")
    plt.tight_layout()
    fig.savefig(out_png)
    plt.close(fig)


def tris_to_3mf_object_xml(tris_3d):
    """Convert triangles to centered-XY, Z>=0 3MF object XML matching Orca schema."""
    xs = [v[0] for t in tris_3d for v in t]
    ys = [v[1] for t in tris_3d for v in t]
    zs = [v[2] for t in tris_3d for v in t]
    cx = 0.5 * (min(xs) + max(xs))
    cy = 0.5 * (min(ys) + max(ys))
    zmin = min(zs)

    v_map = {}
    verts = []
    tri_indices = []
    for v0, v1, v2 in tris_3d:
        idx = []
        for v in (v0, v1, v2):
            key = (round(v[0] - cx, 4), round(v[1] - cy, 4), round(v[2] - zmin, 4))
            vi = v_map.get(key)
            if vi is None:
                vi = len(verts)
                v_map[key] = vi
                verts.append(key)
            idx.append(vi)
        tri_indices.append(tuple(idx))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<model unit="millimeter" xml:lang="en-US" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" xmlns:slic3rpe="http://schemas.slic3r.org/3mf/2017/06">',
        ' <metadata name="slic3rpe:Version3mf">1</metadata>',
        ' <resources>',
        '  <object id="1" type="model">',
        '   <mesh>',
        '    <vertices>',
    ]
    lines.extend(f'     <vertex x="{x:.4f}" y="{y:.4f}" z="{z:.4f}"/>' for x, y, z in verts)
    lines.append('    </vertices>')
    lines.append('    <triangles>')
    lines.extend(f'     <triangle v1="{a}" v2="{b}" v3="{c}"/>' for a, b, c in tri_indices)
    lines.extend([
        '    </triangles>',
        '   </mesh>',
        '  </object>',
        ' </resources>',
        '</model>',
    ])
    return "\n".join(lines).encode("utf-8"), len(verts), len(tri_indices)


def build_white_pla_3mf(template_3mf, out_3mf, tris_3d):
    """Package tag into a single-object Snapmaker U1 .3mf with anti-scorch White PLA settings."""
    obj_xml, n_verts, n_tris = tris_to_3mf_object_xml(tris_3d)
    stl_name = "011DashPass_BaliEZone.stl"
    obj_zip_path = f"3D/Objects/1_{stl_name}_1.model"

    with zipfile.ZipFile(template_3mf, "r") as zin:
        entries = {name: zin.read(name) for name in zin.namelist()}

    # 1. Update 3D/3dmodel.model, 3D/_rels/3dmodel.model.rels, Metadata/model_settings.config
    model_rels = (
        "<?xml version='1.0' encoding='utf-8'?>\n"
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">\n'
        f' <Relationship Target="/{obj_zip_path}" Id="rel-1" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel" />\n'
        "</Relationships>\n"
    ).encode("utf-8")

    root_model = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<model xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" '
        'xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06" '
        'unit="millimeter" xml:lang="en-US">\n'
        ' <metadata name="slic3rpe:Version3mf">1</metadata>\n'
        ' <resources>\n'
        '  <object id="101" type="model">\n'
        '   <components>\n'
        f'    <component p:path="/{obj_zip_path}" objectid="1" transform="1 0 0 0 1 0 0 0 1 0 0 0" />\n'
        '   </components>\n'
        '  </object>\n'
        ' </resources>\n'
        ' <build>\n'
        f'  <item objectid="101" transform="1 0 0 0 1 0 0 0 1 {BED_CENTER_X:.4f} {BED_CENTER_Y:.4f} 0.0000" printable="1" />\n'
        ' </build>\n'
        '</model>\n'
    ).encode("utf-8")

    model_settings = (
        "<?xml version='1.0' encoding='utf-8'?>\n"
        "<config>\n"
        '  <object id="101">\n'
        f'   <metadata key="name" value="{stl_name}" />\n'
        '   <metadata key="extruder" value="1" />\n'
        '   <metadata key="enable_support" value="0" />\n'
        '   <part id="1" subtype="normal_part">\n'
        f'    <metadata key="name" value="{stl_name}" />\n'
        '    <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1" />\n'
        f'    <metadata key="source_file" value="{stl_name}" />\n'
        '   </part>\n'
        '  </object>\n'
        '  <plate>\n'
        '   <metadata key="plater_id" value="1" />\n'
        '   <metadata key="plater_name" value="Bali E-Zone Dash Tag (White PLA)" />\n'
        '   <metadata key="locked" value="false" />\n'
        '   <model_instance>\n'
        '    <metadata key="object_id" value="101" />\n'
        '    <metadata key="instance_id" value="0" />\n'
        '    <metadata key="identify_id" value="1" />\n'
        '   </model_instance>\n'
        '  </plate>\n'
        '</config>\n'
    ).encode("utf-8")

    # 2. Patch project_settings.config for anti-scorch White PLA
    cfg = json.loads(entries["Metadata/project_settings.config"].decode("utf-8"))
    overrides = {
        "filament_colour": ["#FFFFFF"],
        "filament_multi_colors": ["#FFFFFF"],
        "nozzle_temperature": ["200"],
        "nozzle_temperature_initial_layer": ["210"],
        "ironing_type": "no ironing",
        "layer_height": "0.16",
        "initial_layer_print_height": "0.2",
        "wall_loops": "3",
        "wall_generator": "arachne",
        "detect_thin_wall": "1",
        "top_shell_layers": "5",
        "bottom_shell_layers": "4",
        "sparse_infill_density": "25%",
        "sparse_infill_pattern": "gyroid",
        "brim_type": "no_brim",
        "brim_width": "0",
        "elefant_foot_compensation": "0.1",
        "skirt_loops": "3",
        "skirt_distance": "5",
        "skirt_height": "1",
        "z_hop": ["0.8", "0.8", "0.8", "0.8"],
        "z_hop_types": ["Spiral Lift", "Spiral Lift", "Spiral Lift", "Spiral Lift"],
        "reduce_crossing_wall": "1",
        "reduce_infill_retraction": "0",
        "retract_before_wipe": ["70%", "70%", "70%", "70%"],
        "retraction_speed": ["45", "45", "45", "45"],
        "wipe": ["1", "1", "1", "1"],
        "wipe_distance": ["3", "3", "3", "3"],
        "wipe_on_loops": "1",
        "outer_wall_speed": ["60", "60"],
        "top_surface_speed": ["60", "60"],
        "inner_wall_speed": ["80", "80"],
        "internal_solid_infill_speed": ["80", "80"],
        "sparse_infill_speed": ["100", "100"],
        "travel_speed": ["200", "200"],
        "initial_layer_speed": ["35", "35"],
        "initial_layer_infill_speed": ["50", "50"],
        "textured_plate_temp": ["65"],
        "textured_plate_temp_initial_layer": ["65"],
        "hot_plate_temp": ["65"],
        "hot_plate_temp_initial_layer": ["65"],
        "close_fan_the_first_x_layers": ["2"],
        "enable_support": "0",
        "enable_prime_tower": "0",
    }
    for k, v in overrides.items():
        cfg[k] = v

    existing_diff = cfg.get("different_settings_to_system", ["", "", ""])
    diff_set = set(s for s in existing_diff[0].split(";") if s)
    diff_set.update(overrides.keys())
    existing_diff[0] = ";".join(sorted(diff_set))
    cfg["different_settings_to_system"] = existing_diff

    # Write clean .3mf replacing old 3D/Objects entry
    out_entries = {}
    for k, v in entries.items():
        if k.startswith("3D/Objects/"):
            continue
        out_entries[k] = v
    out_entries[obj_zip_path] = obj_xml
    out_entries["3D/3dmodel.model"] = root_model
    out_entries["3D/_rels/3dmodel.model.rels"] = model_rels
    out_entries["Metadata/model_settings.config"] = model_settings
    out_entries["Metadata/project_settings.config"] = json.dumps(cfg, indent=4).encode("utf-8")

    with zipfile.ZipFile(out_3mf, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for k, v in out_entries.items():
            zout.writestr(k, v)
    return n_verts, n_tris


def main():
    kept, top_outer_ccw, center_x, z0_tris_2d = extract_base_shell(SOURCE_STL)
    print(f"Base shell: {len(kept)} tris, top rim verts: {len(top_outer_ccw)}, center_x: {center_x:.4f}")

    shapes, stats = layout_tag_shapes(
        TAG_TEXT, FONT_PATH, center_x, TEXT_Y_MIN_MM, TARGET_TEXT_WIDTH_MM, top_outer_ccw
    )
    print(
        f"Text '{TAG_TEXT}': {stats['shapes']} outer shapes, {stats['holes']} holes, "
        f"X={stats['x_range']}, Y={stats['y_range']}, min border clearance={stats['min_margin_mm']:.3f} mm"
    )

    tris_3d = build_manifold_tag(kept, top_outer_ccw, shapes)
    mnk.write_binary_stl(OUT_STL, tris_3d, f"Bali E-Zone Dash Tag ({len(tris_3d)} tris)")
    print(f"Wrote manifold STL: {OUT_STL} ({len(tris_3d)} tris)")

    render_preview(top_outer_ccw, z0_tris_2d, shapes, PREVIEW_PNG, stats)
    print(f"Rendered preview: {PREVIEW_PNG}")

    n_verts, n_tris = build_white_pla_3mf(TEMPLATE_3MF, OUT_3MF, tris_3d)
    print(f"Wrote 3MF: {OUT_3MF} ({n_verts} unique verts, {n_tris} tris)")


if __name__ == "__main__":
    main()
