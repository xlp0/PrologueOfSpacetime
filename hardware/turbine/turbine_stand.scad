/*
  Digital Synesthesia: The Wind Turbine Stand — SPLIT VERSION
  
  Specs:
  - Tower height: 100mm | Bearing center: 80mm.
  - Inner gap between towers (face-to-face): 160mm.
  - Bearing hole: 20.2mm dia (20mm OD + 0.2mm FDM press-fit clearance).
  - Tower width = bearing thickness = 6mm.
  
  SPLIT FOR PRINTING:
  Split at X=0 → LEFT half + RIGHT half.
  Each half: ~100mm × 80mm × 100mm → fits any printer.
  Tab+slot joint at the cut face — glue together when assembled.
  
  HOW TO PRINT:
  1. Set print_part = "left"  → F6 → Export STL → print it
  2. Set print_part = "right" → F6 → Export STL → print it
  3. Set print_part = "preview" to see both halves assembled
  4. Glue the two halves together with super glue or epoxy
  
  PRINT ORIENTATION: sideways (rotate([90,0,0]) applied)
  Towers horizontal → layer lines along tower length → STRONG
*/

$fn = 80;

// ── CHANGE THIS to switch what you are printing ─────────────────
print_part = "left"; 
// "left"  "right"  "preview"
// ────────────────────────────────────────────────────────────────

// --- Geometry Parameters ---
bearing_spacing = 166;
base_width      = 80;
base_thick      = 10;
tower_h         = 100;
tower_width     = 6;
tower_depth     = 45;

flare_y = 14;
flare_x = 8;
flare_z = 30;

top_cap_r = tower_depth / 2;   // = 22.5mm: semicircular dome cap at tower top
                                // Seamless join: cap diameter = column depth at junction
                                // Also saves filament vs flat-top rectangle

bearing_od = 20.2;
bearing_h  = 80;

base_len = bearing_spacing + tower_width + 20;   // 192mm total

// --- Tab/Slot Joint Parameters ---
// Two rectangular tabs on the cut face (X=0) for alignment & strength.
// Tab protrudes from LEFT half in +X direction; slot cut into RIGHT half.
tab_w     = 25;    // tab width (Y direction)
tab_thick = 8;     // tab depth (X direction, how far it protrudes / slot depth)
tab_h     = 6;     // tab height (Z direction)
tab_gap   = 0.25;  // clearance so tab slides into slot (0.25mm = snug fit)
tab_y1    =  20;   // center Y of first tab
tab_y2    = -20;   // center Y of second tab
tab_z     = 4;     // center Z of both tabs (within base thickness)

// --- Modular Motor Connector (left outer face) ---
// These features let a motor mount / extension module attach to the left side.
// The motor module needs a matching tab (conn_slot_w × conn_slot_h × conn_slot_depth)
// and two M4 bolts to lock in place.
conn_slot_w     = 30;   // slot width (Y) on left end face of base plate
conn_slot_h     = 6;    // slot height (Z) — fits within base_thick=10mm
conn_slot_depth = 8;    // slot depth (X, going inward from left end face)
conn_bolt_y     = 12;   // Y offset of M4 bolt holes (±12mm from center)
conn_tower_z    = 55;   // Z height of alignment holes on left tower outer face


// ─── HELPER MODULES ──────────────────────────────────────────────

module rounded_base() {
    r = 3;
    minkowski() {
        cube([base_len - 2*r, base_width - 2*r, base_thick - 2*r], center=true);
        sphere(r=r);
    }
}

module flared_tower(x_pos) {
    flare_top   = base_thick + flare_z;   // 40mm: where flare ends
    cap_ctr_z   = tower_h - top_cap_r;   // 77.5mm: centre of rounded cap cylinder

    union() {
        // 1. Straight column — vertical walls, bearing hole cuts here (full circle ✓)
        translate([x_pos, 0, (flare_top + cap_ctr_z) / 2])
            cube([tower_width, tower_depth, cap_ctr_z - flare_top], center=true);

        // 2. Rounded dome cap — horizontal cylinder (axis along X)
        //    Widest at cap_ctr_z (= tower_depth, seamless join), narrows to 0 at tower_h
        //    Saves filament vs flat rectangle top; looks polished
        translate([x_pos, 0, cap_ctr_z])
            rotate([0, 90, 0])
            cylinder(r=top_cap_r, h=tower_width, center=true);

        // 3. Flared base — hull() taper, all 4 sides, stress relief
        hull() {
            translate([x_pos, 0, flare_top])
                cube([tower_width, tower_depth, 0.2], center=true);
            translate([x_pos, 0, base_thick + 0.1])
                cube([tower_width + 2*flare_x, tower_depth + 2*flare_y, 0.2], center=true);
        }
    }
}

// The two tabs (protrude in +X from X=0)
module tabs() {
    translate([tab_thick/2, tab_y1, tab_z])
        cube([tab_thick, tab_w, tab_h], center=true);
    translate([tab_thick/2, tab_y2, tab_z])
        cube([tab_thick, tab_w, tab_h], center=true);
}

// The matching slots (cut into right half at X=0, with clearance)
module slots() {
    translate([tab_thick/2, tab_y1, tab_z])
        cube([tab_thick + 1, tab_w + tab_gap*2, tab_h + tab_gap*2], center=true);
    translate([tab_thick/2, tab_y2, tab_z])
        cube([tab_thick + 1, tab_w + tab_gap*2, tab_h + tab_gap*2], center=true);
}

// The complete stand solid (before splitting)
module turbine_stand() {
    difference() {
        union() {
            translate([0, 0, base_thick/2]) rounded_base();
            flared_tower(-bearing_spacing/2);
            flared_tower(+bearing_spacing/2);
        }
        // Bearing holes
        translate([-bearing_spacing/2, 0, bearing_h])
            rotate([0, 90, 0]) cylinder(d=bearing_od, h=tower_width + 4, center=true);
        translate([+bearing_spacing/2, 0, bearing_h])
            rotate([0, 90, 0]) cylinder(d=bearing_od, h=tower_width + 4, center=true);
        // Mounting holes M5
        translate([ bearing_spacing/2 + tower_width/2 + 5,  base_width/2 - 15, -1]) cylinder(d=5.5, h=base_thick+4);
        translate([ bearing_spacing/2 + tower_width/2 + 5, -base_width/2 + 15, -1]) cylinder(d=5.5, h=base_thick+4);
        translate([-bearing_spacing/2 - tower_width/2 - 5,  base_width/2 - 15, -1]) cylinder(d=5.5, h=base_thick+4);
        translate([-bearing_spacing/2 - tower_width/2 - 5, -base_width/2 + 15, -1]) cylinder(d=5.5, h=base_thick+4);

        // ── MODULAR CONNECTOR (left outer side) ──────────────────────────
        // Allows a motor mount / extension module to snap-fit and bolt onto the left side.
        //
        // 1. Rectangular slot on LEFT END FACE of base plate (solid material, robust)
        //    A matching rectangular tab on the motor module slides in here for alignment.
        translate([-base_len/2 + conn_slot_depth/2, 0, base_thick/2])
            cube([conn_slot_depth + 1, conn_slot_w, conn_slot_h], center=true);

        // 2. Two M4 bolt holes through the left end face of the base plate
        //    Motor module is bolted through these for permanent attachment.
        translate([-base_len/2 - 1, conn_bolt_y,  base_thick/2])
            rotate([0, 90, 0]) cylinder(d=4.5, h=conn_slot_depth + 4);
        translate([-base_len/2 - 1, -conn_bolt_y, base_thick/2])
            rotate([0, 90, 0]) cylinder(d=4.5, h=conn_slot_depth + 4);

        // 3. Two M4 alignment holes on outer face of LEFT TOWER column
        //    Motor module uses these to align with the bearing axis height.
        translate([-bearing_spacing/2 - tower_width/2 - 1,  conn_bolt_y, conn_tower_z])
            rotate([0, 90, 0]) cylinder(d=4.5, h=tower_width + 4);
        translate([-bearing_spacing/2 - tower_width/2 - 1, -conn_bolt_y, conn_tower_z])
            rotate([0, 90, 0]) cylinder(d=4.5, h=tower_width + 4);
    }
}


// ─── SPLIT HALVES ─────────────────────────────────────────────────

// LEFT HALF: everything with X ≤ 0, PLUS the two tabs protruding in +X
module left_half() {
    union() {
        // Left portion of stand (intersection clips at X=0)
        intersection() {
            turbine_stand();
            translate([-500, 0, 50]) cube([1000, 1000, 1000], center=true);  // keep X≤0
        }
        // Add tabs on the right face of left half (X=0 face)
        tabs();
    }
}

// RIGHT HALF: everything with X ≥ 0, MINUS the slot cutouts
module right_half() {
    difference() {
        // Right portion of stand
        intersection() {
            turbine_stand();
            translate([500, 0, 50]) cube([1000, 1000, 1000], center=true);   // keep X≥0
        }
        // Cut matching slots at X=0 face
        slots();
    }
}

// ─── PRINT ORIENTATION & SELECTION ───────────────────────────────
// Each half is rotated for sideways printing (towers horizontal = stronger layers)

if (print_part == "left") {
    // Left half: slide it to sit on its flat cut face (X=0 face on bed)
    rotate([90, 0, 0])
    translate([base_len/4, 0, base_width/2])   // center it and lift
        left_half();

} else if (print_part == "right") {
    // Right half: mirror it so it also sits nicely on bed
    rotate([90, 0, 0])
    translate([-base_len/4, 0, base_width/2])
        right_half();

} else {
    // PREVIEW: show both halves assembled (no rotation, full model)
    left_half();
    right_half();
}
