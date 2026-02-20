/*
  Digital Synesthesia: The Astronomer's Eye V3 (Focus & Mount)
  
  Role: The Observer.
  Function: Modular Refractor with Focusing Lock & Mounting Rail.
  
  Specs:
  - Lens: 50mm Diameter.
  - Eyepiece: 1.25".
  - Focuser: Sliding Drawtube with Thumb Screw Lock.
  - Mount: Vixen Style Dovetail (43mm base).
*/

$fn = 100;

// --- Parameters ---
lens_d = 50.5;      
tube_id = 52;       
tube_wall = 4;      
tube_od = tube_id + (2 * tube_wall);

flange_width = 10;
dovetail_len = 80;

// --- Modules ---

// 1. Bolt Flange (Connection)
module bolt_flange() {
    difference() {
        cylinder(d=tube_od + 20, h=5); 
        translate([0,0,-1]) cylinder(d=tube_id, h=7); 
        
        for(i=[0:2]) {
            rotate([0,0, i*120])
                translate([(tube_od/2) + 5, 0, -1])
                cylinder(d=3.2, h=7);
        }
    }
}

// 2. Optical Tube Assembly (OTA) - Front Section
module tube_front() {
    union() {
        difference() {
            cylinder(d=tube_od, h=100);
            translate([0,0,-1]) cylinder(d=tube_id, h=102);
        }
        
        // Lens Cell Seat (At Top)
        translate([0,0,95]) {
            difference() {
                 cylinder(d=tube_od, h=5);
                 translate([0,0,-1]) cylinder(d=lens_d-2, h=7); // Lip
            }
        }
        
        // Bottom Flange
        bolt_flange();
    }
}

// 3. Focuser Section (Back Tube) With Lock & Mount
module tube_back() {
    translate([80, 0, 0])
    union() {
        difference() {
            cylinder(d=tube_od, h=100);
            translate([0,0,-1]) cylinder(d=tube_id, h=102);
            
            // Focus Lock Screw Hole
            translate([0, 0, 80])
                rotate([90,0,0])
                cylinder(d=5, h=tube_od+10, center=true); // M5 or Thumb Screw
        }
        
        // Focus Lock Nut Geometry
        translate([0, -tube_od/2 - 2, 80]) {
            difference() {
                cube([15, 8, 15], center=true);
                rotate([90,0,0]) cylinder(d=5, h=10, center=true);
            }
        }

        // Vixen Dovetail Rail (The Mount)
        translate([0, -tube_od/2 - 10, 40]) {
            difference() {
                // Approximate Vixen Shape (Trapezoid)
                union() {
                    cube([43, 15, dovetail_len], center=true); // Base width
                    // Angled cuts for dovetail happen here in reality, simplified as block with chamfer?
                    // Better: Polygon extrusion
                }
                
                // Mounting Hole (1/4-20)
                rotate([90,0,0])
                    cylinder(d=6.5, h=40, center=true);
            }
        }
        
        // Top Flange
        translate([0,0,100]) bolt_flange();
    }
}

// 4. Lens Retaining Ring
module lens_ring() {
    translate([-60, 0, 0])
    difference() {
        cylinder(d=tube_od, h=4);
        translate([0,0,-1]) cylinder(d=lens_d-1, h=6); 
    }
}

// 5. Focuser Drawtube (1.25")
module focuser() {
    translate([160, 0, 0])
    difference() {
        // Drawtube OD matches Main Tube ID closely
        cylinder(d=tube_id - 0.5, h=80); 
        
        // ID for Eyepiece
        translate([0,0,-1]) cylinder(d=31.75 + 0.4, h=82); 
    }
}

// 6. Thumb Screw Knob (For Focus Lock)
module thumb_screw() {
    translate([-60, 60, 0])
    union() {
        cylinder(d=20, h=5); // Knob Head
        cylinder(d=9, h=15); // Grip Shaft
        translate([0,0,-10]) cylinder(d=4.8, h=10); // Screw Shaft (M5-ish, print tight or heat insert)
    }
}

// --- Layout ---
tube_front();
tube_back();
lens_ring();
focuser();
thumb_screw();
