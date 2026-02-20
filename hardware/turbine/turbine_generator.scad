/*
  Digital Synesthesia: The Wind Turbine Generator Pro V2 (SCAD)
  
  Role: The Engine - High Efficiency.
  Function: Converts Kinetic Energy (Wind) -> Electrical Energy (DC Motor).
  
  Features:
  - 7 Blades (Higher torque/efficiency).
  - Airfoil shape (Teardrop profile).
  - Larger Scale (200mm total diameter).
  - Spinner/Nose Cone (Aerodynamics).
  - Split Nacelle (Body + Clamp) for easy motor insertion.
*/

$fn = 100;

// --- Parameters ---
// Generator (DC Motor)
motor_d = 24.5;    // Standard Hobby Motor (RF-300/500)
motor_len = 30;    
shaft_d = 2.0;     // Shaft diameter (Tight fit)

// Rotor (The Upgrade)
blade_len = 100;   // EXTRA Long Blades (Total D ~220mm)
blade_count = 7;   // High Efficiency
twist = 45;        // Aggressive Twist for torque
root_width = 25;   // WIDE at base (Stronger)
tip_width = 8;     // Narrow at tip (taper)

// Tail
tail_dist = 100;    
tail_area = 60;

// --- Modules ---

// 0. Airfoil Shape (2D Profile)
module airfoil_shape() {
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
            cylinder(d1=motor_d+5, d2=5, h=30); // Aerodynamic Cone (Longer)
            cylinder(d=motor_d+5, h=10); // Strong Base
        }
        // Shaft Hole (Tight Press Fit)
        translate([0,0,-1])
            cylinder(d=shaft_d, h=25);
    }
    
    // Blades
    for (i=[0:blade_count-1]) {
        rotate([0, 0, i*(360/blade_count)])
            translate([motor_d/2, 0, 5]) // Attach to base
            rotate([20, 0, 0]) // Pitch/Attack Angle (critical for lift)
            linear_extrude(height=blade_len, twist=twist, scale=tip_width/root_width)
            offset(r=1) // Smooth edges
            square([root_width, 3], center=true); // Thicker blades (3mm)
    }
}

// 2. The Nacelle Main Body (Motor Bed)
module nacelle_body() {
    difference() {
        // Main Block
        union() {
            // Motor Bed
            translate([0,0,0])
                cube([motor_d + 10, motor_len + 10, motor_d/2 + 5], center=true);
            
            // Tail Boom Socket
            translate([0, tail_dist/2, 0])
                cube([10, tail_dist, 10], center=true); 
        }
        
        // Motor Void (Half Cylinder)
        translate([0, 0, 5])
            rotate([90, 0, 0])
            cylinder(d=motor_d, h=motor_len + 20, center=true);
            
        // Screw Holes for Clamp
        translate([15, 0, 5]) cylinder(d=3, h=20, center=true);
        translate([-15, 0, 5]) cylinder(d=3, h=20, center=true);
        
        // Wire Path
        translate([0, 0, -5])
             rotate([90, 0, 0])
             cylinder(d=4, h=motor_len + 30, center=true);
    }
    
    // Tail Fin
    translate([0, tail_dist, 5])
        cube([2, 60, 70], center=true); // Bigger Tail
}

// 2b. Nacelle Clamp (Top Strap)
module nacelle_clamp() {
    difference() {
        cube([motor_d + 10, 10, 10], center=true);
        
        // Motor Curve
        translate([0, 0, -5])
            rotate([90, 0, 0])
            cylinder(d=motor_d, h=12, center=true);
            
        // Screw Holes
        translate([15, 0, 0]) cylinder(d=3.2, h=20, center=true);
        translate([-15, 0, 0]) cylinder(d=3.2, h=20, center=true);
    }
}

// 3. Tower Mount (Swivel)
module mount() {
    difference() {
        union() {
            cylinder(d=30, h=40); // Strong Post
            // Platform
            translate([0, 0, 35])
                cube([40, 40, 5], center=true);
        }
        // Pipe Void
        translate([0,0,-1])
            cylinder(d=22, h=30); // 21.5mm is standard 1/2" PVC OD (Loose fit)
            
        // Pivot Screw Hole (Top)
        translate([0,0,30])
             cylinder(d=5, h=20);
    }
}

// --- Layout for Printing ---
translate([0, 0, 0]) rotor();
translate([120, 0, motor_d/2]) nacelle_body();
translate([120, 40, 0]) nacelle_clamp(); // Print 2 of these usually, but 1 is fine here
translate([-60, 0, 0]) mount();
