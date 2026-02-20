/*
  Digital Synesthesia: The Astronomer's Eye V4 (Helical Focus)
  
  Role: The Observer.
  Function: Modular Refractor with *Twist-to-Focus* (Helical).
  
  Specs:
  - Lens: 50mm Diameter.
  - Eyepiece: 1.25".
  - Focuser: HELICAL THREAD (Turn to Focus).
  - Mount: Vixen Style Dovetail.
*/

$fn = 100;

// --- Parameters ---
lens_d = 50.5;      
tube_id = 52;       
tube_wall = 4;      
tube_od = tube_id + (2 * tube_wall);

// Thread Params (Helical Focuser)
thread_pitch = 5;   // 5mm per turn (Coarse for printing)
thread_len = 40;    // Focus travel
thread_depth = 1.5; // Depth of thread groove

// --- Modules ---

// 1. Thread Generator (Triangular Profile)
module thread(d, pitch, len, inner=false) {
    linear_extrude(height=len, twist = -360 * (len/pitch), slices=100)
        translate([input_d/2, 0])
             circle(r=thread_depth, $fn=3); // Triangle profile
}

// 2. Bolt Flange (Connection)
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

// 3. Front Tube (Same as V3)
module tube_front() {
    union() {
        difference() {
            cylinder(d=tube_od, h=100);
            translate([0,0,-1]) cylinder(d=tube_id, h=102);
            
            // Lens Seat (Recess)
            translate([0,0,95]) {
                 difference() {
                     cylinder(d=tube_id+1, h=10); 
                 }
            }
        }
        
        // Lens Cell Seat (Lip)
        translate([0,0,95]) {
            difference() {
                 cylinder(d=tube_od, h=5);
                 translate([0,0,-1]) cylinder(d=lens_d-1, h=7); 
            }
        }
        
        // Bottom Flange
        bolt_flange();
    }
}

// 4. Back Tube (Female Threaded)
module tube_back() {
    translate([80, 0, 0])
    union() {
        difference() {
            cylinder(d=tube_od, h=100);
            
            // Inner Void (Standard Tube)
            translate([0,0,-1]) cylinder(d=tube_id, h=62); // Bottom part clear
            
            // Threaded Section (Top 40mm)
            translate([0,0,60])
                // Create female thread by differencing a male thread shape?
                // Better: Linear Extrude Inner Profile
                linear_extrude(height=thread_len+2, twist = -360 * ((thread_len+2)/thread_pitch), slices=100)
                    difference() {
                        circle(d=tube_id); // Outside of thread
                        // Inner Shape: Gear-like cut
                        for(i=[0:5]) { // 6-start thread? No, simple 1-start.
                            // Just a simple corrupted circle method for threads
                            // Standard circle
                        }
                    }
             // Actually, simplified threading method:
             // Subtract a helix.
        }
        
        // The Void with Threads (Simplified Method)
        translate([0,0,50])
             difference() {
                 cylinder(d=tube_id, h=52); // Placeholder for void
                 // Internal Thread geometry is HARD without library. 
                 // Strategy: Use 'Threadlib' concept manually.
                 // We will make 3 small "Pins" inside the tube that ride in the helical groove of the drawtube.
                 // This is easier to print and smoother.
             }
             
        // GUIDE PINS (For Helical Motion)
        // Instead of full female threads, we use 3 pins to ride in the male groove.
        for(i=[0:2]) {
            rotate([0,0, i*120])
            translate([tube_id/2 - 1, 0, 90])
                rotate([0,90,0])
                cylinder(d=3, h=4); // Pin protrudes into tube
        }

        // Vixen Rail
        translate([0, -tube_od/2 - 10, 40]) {
            difference() {
                cube([43, 15, 80], center=true); 
                rotate([90,0,0]) cylinder(d=6.5, h=40, center=true);
            }
        }
        
        // Top Flange
        translate([0,0,100]) bolt_flange();
    }
}

// 5. Helical Focuser Drawtube (Male Threaded Groove)
module focuser_helical() {
    translate([160, 0, 0])
    difference() {
        // Tube Body
        cylinder(d=tube_id - 1, h=80); 
        
        // ID for Eyepiece
        translate([0,0,-1]) cylinder(d=31.75 + 0.4, h=82); 
        
        // HELICAL GROOVE (The Thread)
        // We cut a groove for the pins to ride in.
        linear_extrude(height=80, twist = -360 * (80/thread_pitch), slices=200)
            translate([(tube_id-1)/2, 0])
            circle(d=4, $fn=10); // The Groove Shape
    }
    
    // Grip Ring (Knurled)
    translate([160, 0, 0])
    difference() {
        cylinder(d=tube_id + 10, h=10);
        translate([0,0,-1]) cylinder(d=31.75 + 0.4, h=12);
    }
}

// 6. Lens Cap
module lens_ring() {
    translate([-60, 0, 0])
    difference() {
        cylinder(d=tube_od, h=4);
        translate([0,0,-1]) cylinder(d=lens_d-1, h=6); 
    }
}

// --- Layout ---
tube_front();
tube_back();
lens_ring();
focuser_helical();
