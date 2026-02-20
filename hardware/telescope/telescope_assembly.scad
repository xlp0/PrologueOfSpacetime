/*
  Digital Synesthesia: The Astronomer's Eye V2 (Robust Telescope)
  
  Role: The Observer.
  Function: Modular, Bolt-Together Refractor.
  
  Specs:
  - Lens: 50mm Diameter.
  - Eyepiece: 1.25".
  - Connection: M3 Bolt Flanges (Stronger than glue/friction).
  - Mount: 1/4-20 Nut Trap (Standard Tripod).
*/

$fn = 100;

// --- Parameters ---
lens_d = 50.5;      // 50mm + Tolerance
tube_id = 52;       // Inner Diameter
tube_wall = 4;      // Thicker walls
tube_od = tube_id + (2 * tube_wall);

flange_width = 10;  // How wide the connection flange is

// --- Modules ---

// 1. Bolt Flange (For connecting tubes)
module bolt_flange() {
    difference() {
        cylinder(d=tube_od + 20, h=5); // Wide flange
        translate([0,0,-1]) cylinder(d=tube_id, h=7); // Center hole
        
        // M3 Bolt Pattern (3 Bolts)
        for(i=[0:2]) {
            rotate([0,0, i*120])
                translate([(tube_od/2) + 5, 0, -1])
                cylinder(d=3.2, h=7); // M3 Clearance
        }
    }
}

// 2. Optical Tube Assembly (OTA) - Front Section
module tube_front() {
    union() {
        difference() {
            cylinder(d=tube_od, h=100);
            translate([0,0,-1]) cylinder(d=tube_id, h=102);
            
            // Lens Seat (Recess)
            translate([0,0,95]) {
                 difference() {
                     cylinder(d=tube_id+1, h=10); // Clear space
                     // Step is naturally formed by the tube_id if we make lens seat bigger?
                     // Let's make a specific seat.
                 }
            }
        }
        
        // Lens Cell Seat (At Top)
        translate([0,0,95]) {
            difference() {
                 cylinder(d=tube_od, h=5);
                 translate([0,0,-1]) cylinder(d=lens_d-2, h=7); // Lip
            }
        }
        
        // Bottom Flange (Connects to Focuser Section)
        bolt_flange();
    }
}

// 3. Focuser Section (Back Tube)
module tube_back() {
    translate([80, 0, 0])
    union() {
        difference() {
            cylinder(d=tube_od, h=100);
            translate([0,0,-1]) cylinder(d=tube_id, h=102);
            
            // Tripod Mount Block (1/4-20 Nut Trap)
            translate([0, -tube_od/2, 20])
                rotate([90,0,0])
                cylinder(d=12, h=10); // Drill hole later? 
        }
        
        // Tripod Block (External)
        translate([0, -tube_od/2 - 5, 30]) {
            difference() {
                cube([30, 15, 40], center=true);
                // 1/4-20 Nut Trap
                rotate([90, 0, 0]) {
                    cylinder(d=6.5, h=20, center=true); // Screw hole
                    translate([0,0,2]) cylinder(d=13, h=6, $fn=6); // Nut Hex
                }
            }
        }

        // Top Flange (Connects to Front)
        translate([0,0,100]) bolt_flange();
        
        // Bottom Focuser Adapter (Simple Reducer)
        bolt_flange(); // At bottom too? No, needs adapter.
    }
}

// 4. Lens Retaining Ring (Screw or Press fit)
module lens_ring() {
    translate([-60, 0, 0])
    difference() {
        cylinder(d=tube_od, h=4);
        translate([0,0,-1]) cylinder(d=lens_d-2, h=6); // Aperture
        
        // Bolt holes to match Flange (if we bolted it... )
        // Actually, let's make it press fit or simple cap.
        // Simple Cap:
        translate([0,0,2]) cylinder(d=tube_od+2, h=5); // Outer rim
    }
}

// 5. Focuser Tube (1.25")
module focuser() {
    translate([160, 0, 0])
    difference() {
        cylinder(d=31.75 + 4, h=60); // OD
        translate([0,0,-1]) cylinder(d=31.75 + 0.2, h=62); // ID (Eyepiece)
    }
}

// --- Layout ---
tube_front();
tube_back();
lens_ring();
focuser();
