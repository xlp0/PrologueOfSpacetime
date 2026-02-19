/*
  Digital Synesthesia: VR Lens Holder (SCAD)
  
  Role: The Synthesist's Eye (Hardware Interface).
  Function: Holds a 24mm Lens for the VR Headset.
  
  Specs:
  - Outer Diameter: 37mm
  - Total Height: 3mm (3 Layers x 1mm)
  - Aperture Layers (Bottom): 2 Layers @ 22mm ID
  - Lens Layer (Top): 1 Layer @ 24mm ID
*/

$fn = 100; // Resolution

outer_d = 37;
layer_h = 1;

// Layer 1 & 2: The Stop / Aperture (22mm hole)
// Total height = 2mm
module aperture_layers() {
    difference() {
        cylinder(h = layer_h * 2, d = outer_d);
        translate([0, 0, -1])
            cylinder(h = (layer_h * 2) + 2, d = 22);
    }
}

// Layer 3: The Lens Seat (24mm hole)
// Total height = 1mm
module lens_seat() {
    difference() {
        cylinder(h = layer_h, d = outer_d);
        translate([0, 0, -1])
            cylinder(h = layer_h + 2, d = 24);
    }
}

// Assembly
union() {
    // Bottom 2 layers (0mm to 2mm)
    aperture_layers();
    
    // Top 1 layer (2mm to 3mm)
    translate([0, 0, layer_h * 2])
        lens_seat();
}
