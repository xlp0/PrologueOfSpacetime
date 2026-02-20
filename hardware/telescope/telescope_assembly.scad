/*
  Digital Synesthesia: The Astronomer's Eye (Refractor Telescope)
  
  Role: The Observer.
  Function: Magnifies distant light (The Firefall).
  
  Specs:
  - Objective Lens: 50mm Diameter (Standard Surplus).
  - Eyepiece: 1.25" (31.75mm) Standard Eyepiece.
  - Tube ID: Slightly larger than lens.
*/

$fn = 100; // Resolution

// --- Parameters ---
lens_d = 50;        // Diameter of Objective Lens (mm)
lens_thick = 5;     // Thickness of Lens edge (mm)
focal_length = 360; // Focal Length of Lens (mm)
tube_wall = 3;      // Thickness of the main tube wall (mm)

eyepiece_d = 31.75; // Standard 1.25" Eyepiece
focuser_travel = 50;// How much the focuser slides (mm)

// Calculated Dimensions
tube_id = lens_d + 1; // 1mm clearance
tube_od = tube_id + (2 * tube_wall);
focuser_od = tube_id - 0.5; // Slight friction fit inside main tube
focuser_id = eyepiece_d + 0.5; // Fit for eyepiece

// --- Modules ---

// 1. Main Tube (Holds the Objective Lens)
module main_tube() {
    difference() {
        // Outer Shell
        cylinder(d=tube_od, h=150); // Print in sections if needed
        
        // Inner Void
        translate([0,0,-1])
            cylinder(d=tube_id, h=152);
    }
    
    // Lens Cell (Front Stop)
    translate([0, 0, 140]) { // Near the front
        difference() {
            cylinder(d=tube_od, h=10);
            translate([0,0,-1])
                cylinder(d=lens_d - 2, h=12); // Lip to hold lens
        }
    }
}

// 2. Focuser Tube (Slides inside Main Tube)
module focuser_tube() {
    translate([60, 0, 0]) { // Move aside for printing
        difference() {
            // Sliding Tube
            cylinder(d=focuser_od, h=focuser_travel + 30);
            
            // Inner Void for Eyepiece
            translate([0,0,-1])
                cylinder(d=focuser_id, h=focuser_travel + 32);
        }
        
        // Handle / Grip Ring
        translate([0, 0, 0]) {
            difference() {
                cylinder(d=focuser_od + 5, h=5); // Grip at back
                translate([0,0,-1])
                    cylinder(d=focuser_id, h=7);
            }
        }
    }
}

// 3. Dew Shield (Optional Front Extension)
module dew_shield() {
    translate([-60, 0, 0]) { // Move aside
        difference() {
            cylinder(d=tube_od + 4, h=60);
            translate([0,0,-1])
                cylinder(d=tube_od + 0.5, h=62); // Fits overly Main Tube
        }
    }
}

// --- Layout for Printing ---
main_tube();
focuser_tube();
dew_shield();
