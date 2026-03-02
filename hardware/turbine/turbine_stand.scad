/*
  Digital Synesthesia: The Wind Turbine Stand
  
  Specs:
  - Tower height: 100mm | Bearing center: 80mm.
  - Inner gap between towers (face-to-face): 160mm.
  - Bearing hole: 20.2mm dia (20mm OD + 0.2mm FDM press-fit clearance).
  - Tower width = bearing thickness = 6mm.
  
  Stress Relief:
  - Towers flare outward at base using hull() — wider at bottom, narrow at top.
  - Like a pillar/pylon: naturally stronger at the stress point, visible from all angles.
  - All outer edges rounded via minkowski on the base plate.
*/

$fn = 80;

// --- Parameters ---
bearing_spacing = 166;   // Center-to-center; inner gap = 166-6 = 160mm
base_width      = 80;
base_thick      = 10;
tower_h         = 100;
tower_width     = 6;
tower_depth     = 45;

// Flare: how much each tower widens toward the base
flare_y = 14;   // Each tower face widens by 14mm at the base (each side, so +28mm total depth)
flare_z = 30;   // The flare zone height: from base top (Z=base_thick) up by this amount

bearing_od = 20.2;
bearing_h  = 80;    // hole top = 90.1mm < 100mm tower ✓

base_len = bearing_spacing + tower_width + 20;


// --- Rounded cube for base plate ---
module rounded_base() {
    r = 3;
    minkowski() {
        cube([base_len - 2*r, base_width - 2*r, base_thick - 2*r], center=true);
        sphere(r=r);
    }
}

// --- Flared tower ---
// Bottom is wide (flared), top is narrow. hull() blends them into one smooth shape.
// This is the standard FDM stress-relief: more material exactly where stress is highest.
module flared_tower(x_pos) {
    hull() {
        // Top of tower: narrow (normal tower cross section)
        translate([x_pos, 0, tower_h - 0.1])
            cube([tower_width, tower_depth, 0.2], center=true);

        // Midpoint anchor (keeps the straight section before flare starts)
        translate([x_pos, 0, base_thick + flare_z])
            cube([tower_width, tower_depth, 0.2], center=true);

        // Bottom of tower: wide flared base
        translate([x_pos, 0, base_thick + 0.1])
            cube([tower_width, tower_depth + 2*flare_y, 0.2], center=true);
    }
}


module turbine_stand() {
    difference() {
        union() {
            // 1. Base plate (rounded outer edges)
            translate([0, 0, base_thick/2])
                rounded_base();

            // 2. Left tower (flared at base for stress relief)
            flared_tower(-bearing_spacing/2);

            // 3. Right tower (flared at base for stress relief)
            flared_tower(+bearing_spacing/2);
        }

        // --- Cutouts ---

        // Bearing holes (20.2mm dia, coaxial along X-axis)
        translate([-bearing_spacing/2, 0, bearing_h])
            rotate([0, 90, 0])
            cylinder(d=bearing_od, h=tower_width + 4, center=true);
        translate([+bearing_spacing/2, 0, bearing_h])
            rotate([0, 90, 0])
            cylinder(d=bearing_od, h=tower_width + 4, center=true);

        // Mounting holes M5
        translate([ bearing_spacing/2 + tower_width/2 + 5,  base_width/2 - 15, -1]) cylinder(d=5.5, h=base_thick + 4);
        translate([ bearing_spacing/2 + tower_width/2 + 5, -base_width/2 + 15, -1]) cylinder(d=5.5, h=base_thick + 4);
        translate([-bearing_spacing/2 - tower_width/2 - 5,  base_width/2 - 15, -1]) cylinder(d=5.5, h=base_thick + 4);
        translate([-bearing_spacing/2 - tower_width/2 - 5, -base_width/2 + 15, -1]) cylinder(d=5.5, h=base_thick + 4);
    }
}

turbine_stand();
