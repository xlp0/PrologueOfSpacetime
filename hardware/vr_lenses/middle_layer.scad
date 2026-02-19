// Digital Synesthesia: VR Lens Holder - Middle Layer (SCAD)
// Specs: 37mm OD, 2mm Thickness.
// Aperture: 25mm.
// Quantity: 2 Discs.

$fn = 100; // Smoothness

// Disc 1 (25mm ID, 2mm Thick)
translate([0, 0, 0]) {
    difference() {
        cylinder(r=18.5, h=2); 
        translate([0,0,-1]) cylinder(r=12.5, h=4); // 25mm ID / 2 = 12.5mm Radius
    }
}

// Disc 2 (25mm ID, 2mm Thick)
translate([40, 0, 0]) {
    difference() {
        cylinder(r=18.5, h=2); 
        translate([0,0,-1]) cylinder(r=12.5, h=4); // 25mm ID / 2 = 12.5mm Radius
    }
}
