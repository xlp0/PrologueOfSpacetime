// Digital Synesthesia: VR Lens Holder (SCAD)
// Specs: 37mm OD.
// Layout: 3 Rows.
// Row 1 (Left Eye): 2x 22mm (1mm thick), 1x 24mm (1mm thick).
// Row 2 (Right Eye): 2x 22mm (1mm thick), 1x 24mm (1mm thick).
// Row 3 (Extra): 2x 25mm (2mm thick).

$fn = 100; // Smoothness

// Module for a single set (One Eye)
module lens_set() {
    // Disc 1 (Bottom Aperture - 22mm)
    translate([0, 0, 0]) {
        difference() {
            cylinder(r=18.5, h=1); 
            translate([0,0,-1]) cylinder(r=11, h=3); 
        }
    }

    // Disc 2 (Middle Aperture - 22mm)
    translate([40, 0, 0]) {
        difference() {
            cylinder(r=18.5, h=1);
            translate([0,0,-1]) cylinder(r=11, h=3);
        }
    }

    // Disc 3 (Top Lens Seat - 24mm)
    translate([80, 0, 0]) {
        difference() {
            cylinder(r=18.5, h=1);
            translate([0,0,-1]) cylinder(r=12, h=3); // 24mm ID
        }
    }
}

// Instantiate Left Eye (Row 1)
translate([0, 0, 0]) {
    lens_set();
}

// Instantiate Right Eye (Row 2) - Shifted down by 40mm
translate([0, 40, 0]) {
    lens_set();
}

// Instantiate Extra 25mm Mounts (Row 3) - Shifted down by 80mm
translate([0, 80, 0]) {
    // Disc 1 (25mm ID, 2mm Thick)
    difference() {
        cylinder(r=18.5, h=2); 
        translate([0,0,-1]) cylinder(r=12.5, h=4); // 25mm ID
    }

    // Disc 2 (25mm ID, 2mm Thick)
    translate([40, 0, 0]) {
        difference() {
            cylinder(r=18.5, h=2); 
            translate([0,0,-1]) cylinder(r=12.5, h=4); // 25mm ID
        }
    }
}
