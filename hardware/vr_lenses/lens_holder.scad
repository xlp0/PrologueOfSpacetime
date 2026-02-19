/*
  Digital Synesthesia: VR Lens Holder (SCAD)
  
  Role: The Synthesist's Eye (Hardware Interface).
  Function: Holds a 24mm Lens for the VR Headset.
  
  Instructions:
  1. Render (F6) -> Export as STL.
  2. The 3 parts will be exported as one file, laid out flat.
  3. Print.
  4. Stack them: Aperture + Aperture + Lens Seat.
*/

$fn = 100; // Resolution

outer_d = 37;
id_aperture = 22;
id_lens = 24;
thickness = 1;
spacing = 40; // Distance between parts

// Module for a single ring
module lens_ring(id) {
    difference() {
        cylinder(h = thickness, d = outer_d);
        translate([0, 0, -1])
            cylinder(h = thickness + 2, d = id);
    }
}

// Layout: 3 Discs side-by-side
// Layer 1: Bottom (Aperture)
translate([0, 0, 0]) {
    lens_ring(id_aperture);
}

// Layer 2: Middle (Aperture)
translate([spacing, 0, 0]) {
    lens_ring(id_aperture);
}

// Layer 3: Top (Lens Seat)
translate([spacing * 2, 0, 0]) {
    lens_ring(id_lens);
}
