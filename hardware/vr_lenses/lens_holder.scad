// Digital Synesthesia: VR Lens Holder (SCAD)
// Specs: 37mm OD, 1mm Thickness.
// Layout: 3 Discs (2x 22mm, 1x 24mm).

$fn = 100; // Smoothness

// Disc 1 (Bottom Aperture - 22mm)
translate([0, 0, 0]) {
    difference() {
        cylinder(r=18.5, h=1); // 37mm OD / 2 = 18.5mm Radius
        translate([0,0,-1])
            cylinder(r=11, h=3); // 22mm ID / 2 = 11mm Radius
    }
}

// Disc 2 (Middle Aperture - 22mm)
translate([40, 0, 0]) {
    difference() {
        cylinder(r=18.5, h=1);
        translate([0,0,-1])
            cylinder(r=11, h=3);
    }
}

// Disc 3 (Top Lens Seat - 24mm)
translate([80, 0, 0]) {
    difference() {
        cylinder(r=18.5, h=1);
        translate([0,0,-1])
            cylinder(r=12, h=3); // 24mm ID / 2 = 12mm Radius
    }
}
