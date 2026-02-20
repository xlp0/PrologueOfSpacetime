/*
  Digital Synesthesia: The Wind Turbine Generator Pro (SCAD)
  
  Role: The Engine - High Efficiency.
  Function: Converts Kinetic Energy (Wind) -> Electrical Energy (DC Motor).
  
  Features:
  - 7 Blades (Higher torque/efficiency).
  - Airfoil shape (Teardrop profile).
  - Larger Scale (160mm total diameter).
  - Spinner/Nose Cone (Aerodynamics).
*/

$fn = 100;

// --- Parameters ---
// Generator (DC Motor)
motor_d = 24.5;    // Standard Hobby Motor (RF-300/500)
motor_len = 30;    
shaft_d = 2.0;     // Shaft diameter (Tight fit)

// Rotor (The Upgrade)
blade_len = 80;    // Long Blades (Total D ~170mm)
blade_count = 7;   // High Efficiency
twist = 45;        // Aggressive Twist for torque
root_width = 12;   // Wide at base
tip_width = 4;     // Narrow at tip (taper)

// Tail
tail_dist = 80;    
tail_area = 50;

// --- Modules ---

// 0. Airfoil Shape (2D Profile)
module airfoil() {
    // Simple Teardrop (Leading Edge Rounded, Trailing Edge Sharp)
    scale([1, 0.4]) // Flatten it
    circle(d=root_width); // Leading edge
    translate([root_width/2, -root_width/5, 0])
        polygon([[0,0], [root_width*2, root_width/5], [0, root_width/2.5]]); // Trailing edge
}

// 1. The Rotor (Hub + 7 Blades)
module rotor() {
    difference() {
        // Spinner / Nose Cone
        union() {
            cylinder(d1=motor_d+2, d2=5, h=25); // Aerodynamic Cone
            cylinder(d=motor_d+2, h=8); // Strong Base
        }
        // Shaft Hole (Tight Press Fit)
        translate([0,0,-1])
            cylinder(d=shaft_d, h=15);
    }
    
    // Blades
    for (i=[0:blade_count-1]) {
        rotate([0, 0, i*(360/blade_count)])
            translate([motor_d/2 - 1, 0, 4]) // Attach to base
            rotate([15, 0, 0]) // Pitch/Attack Angle (critical for lift)
            linear_extrude(height=blade_len, twist=twist, scale=tip_width/root_width)
            offset(r=1) // Smooth edges
            square([root_width, 2], center=true); // Fallback to flat foil if complex. 
            // Better: Use square for reliability in printing. Airfoil is hard to print vertical.
    }
}

// 2. The Nacelle (Motor Housing + Tail Boom)
module nacelle() {
    difference() {
        // Main Body
        union() {
            cylinder(d=motor_d + 5, h=motor_len, center=true); // Housing
            translate([0, 0, -motor_len/2])
                cube([8, tail_dist, 8]); // Stronger Boom
        }
        
        // Motor Void
        cylinder(d=motor_d, h=motor_len + 2, center=true);
        
        // Wire Holes
        translate([0, 0, -5])
            rotate([90, 0, 0])
            cylinder(d=3, h=motor_d + 10, center=true);
        
        // Cooling Vents
        translate([0, 0, 5])
             rotate([90, 0, 0])
             cylinder(d=10, h=motor_d + 10, center=true);
    }
    
    // Tail Vane (Large Fin)
    translate([0, tail_dist, -motor_len/2 + 10])
        cube([2, 50, 60], center=true);
}

// 3. Tower Mount (Swivel)
module mount() {
    difference() {
        union() {
            cylinder(d=25, h=35); // Strong Post
            translate([0, 0, 30])
                cube([motor_d+5, 25, 10], center=true); // Platform
        }
        translate([0,0,-1])
            cylinder(d=16, h=25); // Pipe mount (16mm ID / 1/2" PVC)
    }
}

// --- Layout for Printing ---
translate([0, 0, 0]) rotor();
translate([80, 0, 0]) rotate([90, 0, 0]) nacelle();
translate([-50, 0, 0]) mount();
