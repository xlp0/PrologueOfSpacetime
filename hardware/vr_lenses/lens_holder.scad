// Digital Synesthesia: VR Lens Holder (SCAD)
// Specs: 37mm OD, 1mm Thickness.
// Layout: 2 Sets (Left/Right Eye) -> 6 Discs Total.
// Row 1 (Left Eye): 2x 22mm, 1x 24mm.
// Row 2 (Right Eye): 2x 22mm, 1x 24mm.

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
            translate([0,0,-1]) cylinder(r=12, h=3); 
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
