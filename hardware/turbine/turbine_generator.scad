/*
  Digital Synesthesia: The Wind Turbine Generator (SCAD)
  
  Role: The Engine.
  Function: Converts Kinetic Energy (Wind) -> Electrical Energy (DC Motor).
  
  Components:
  1. Rotor (Blades + Hub).
  2. Nacelle (Holds the Generator/Motor).
  3. Tail (Orientation).
  4. Mount (Connects to Tower).
*/

$fn = 100;

// --- Parameters ---
// Generator (DC Motor)
motor_d = 24.5;    // Diameter of standard hobby motor (RF-300/500)
motor_len = 30;    // Length of motor body
shaft_d = 2.0;     // Motor shaft diameter (Press fit)

// Rotor
blade_len = 50;
blade_count = 3;   // Standard efficient count
twist = 30;

// Tail
tail_dist = 60;    // Distance from mast
tail_area = 40;    // Size of fin

// --- Modules ---

// 1. The Rotor (Hub + Blades)
module rotor() {
    difference() {
        // Nose Cone Hub
        union() {
            cylinder(d1=motor_d, d2=5, h=15); // Cone shape
            cylinder(d=motor_d, h=5); // Base
        }
        // Shaft Hole (Press Fit)
        translate([0,0,-1])
            cylinder(d=shaft_d, h=10);
    }
    
    // Blades
    for (i=[0:blade_count-1]) {
        rotate([0, 0, i*(360/blade_count)])
            translate([motor_d/2 - 2, 0, 5]) // Attach to base
            rotate([20, 0, 0]) // Pitch angle
            linear_extrude(height=blade_len, twist=twist, scale=0.5)
            square([8, 2], center=true);
    }
}

// 2. The Nacelle (Motor Housing + Tail Boom)
module nacelle() {
    difference() {
        // Main Body
        union() {
            cylinder(d=motor_d + 4, h=motor_len, center=true); // Motor housing
            translate([0, 0, -motor_len/2])
                cube([6, tail_dist, 6]); // Tail Boom
        }
        
        // Motor Void
        cylinder(d=motor_d, h=motor_len + 2, center=true);
        
        // Wire Holes
        translate([0, 0, -5])
            rotate([90, 0, 0])
            cylinder(d=3, h=motor_d + 10, center=true);
    }
    
    // Tail Vane (The Fin)
    translate([0, tail_dist, -motor_len/2 + 5])
        cube([2, 40, 40], center=true);
}

// 3. Tower Mount (Swivel)
module mount() {
    difference() {
        union() {
            cylinder(d=20, h=30); // Swivel post
            translate([0, 0, 25])
                cube([motor_d+4, 20, 10], center=true); // Platform
        }
        translate([0,0,-1])
            cylinder(d=15, h=20); // Pipe mount (15mm ID)
    }
}

// --- Layout for Printing ---
// Arrange parts flat
translate([0, 0, 0]) rotor();
translate([60, 0, 0]) rotate([90, 0, 0]) nacelle(); // Print flat on side
translate([-40, 0, 0]) mount();
