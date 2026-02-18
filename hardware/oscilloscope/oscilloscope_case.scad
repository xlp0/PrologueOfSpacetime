/*
  Digital Synesthesia: The Oscilloscope Case (SCAD)
  
  Role: The Geometry (Container for the Biologist's Mind).
  Fits: Arduino Nano + 0.96" OLED Display.
  
  Instructions:
  1. Install OpenSCAD.
  2. Open this file.
  3. Render (F6) -> Export as STL.
  4. 3D Print.
*/

// Dimensions (mm)
width = 40;
length = 60;
height = 25;
wall = 2;

// OLED Cutout (0.96" I2C)
oled_w = 27;
oled_h = 15;
oled_x = (width - oled_w) / 2;
oled_y = 10;

// Main Box
difference() {
    // Outer Shell
    cube([width, length, height]);
    
    // Inner Cavity
    translate([wall, wall, wall])
        cube([width - 2*wall, length - 2*wall, height]);
        
    // OLED Cutout (Top Face)
    translate([oled_x, length - oled_y - oled_h, height - wall - 1])
        cube([oled_w, oled_h, wall + 2]);
        
    // Probe Hole (Front Face)
    translate([width/2, 0, height/2])
        rotate([90, 0, 0])
        cylinder(h=wall+2, r=3, center=true); // 6mm hole for wires
        
    // USB Hole (Back Face)
    translate([width/2, length, height/2])
        rotate([90, 0, 0])
        cylinder(h=wall+2, r=4, center=true); // 8mm hole for USB
}

// Lid (Separate Piece)
translate([width + 10, 0, 0]) {
    difference() {
        cube([width, length, 2]); // Lid plate
        
        // Screw holes (optional)
        translate([4, 4, -1]) cylinder(h=4, r=1.5);
        translate([width-4, 4, -1]) cylinder(h=4, r=1.5);
        translate([width-4, length-4, -1]) cylinder(h=4, r=1.5);
        translate([4, length-4, -1]) cylinder(h=4, r=1.5);
    }
    
    // Snap-fit lip
    translate([wall+0.5, wall+0.5, 2])
        difference() {
            cube([width - 2*wall - 1, length - 2*wall - 1, 3]);
            translate([1, 1, -1])
                cube([width - 2*wall - 3, length - 2*wall - 3, 5]);
        }
}
