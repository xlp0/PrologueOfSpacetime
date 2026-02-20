/*
  Digital Synesthesia: The Sovereign Drone (SCAD)
  
  Role: The Sovereign Eye (The Observer).
  Function: Pathfinding via FPV (First Person View).
  
  Specs:
  - Configuration: True-X Quadcopter.
  - Stack Mount: 30.5x30.5mm (Standard Flight Controller).
  - Motor Mount: 16x19mm (Standard 22xx Motors).
  - Prop Size: 5-inch (Standard).
*/

$fn = 100;

// --- Parameters ---
arm_thick = 4;      // Thickness of Arms (mm)
body_thick = 2;     // Thickness of Center Plates
motor_to_motor = 220; // Diagonal distance (mm)

// Standard Mounts
stack_mount = 30.5; // FC Mounting Holes
motor_hole_d = 3.2; // M3 Screw
motor_mount_x = 16;
motor_mount_y = 19;

// Calculated
arm_len = motor_to_motor / 2;
arm_angle = 45;

// --- Modules ---

// 1. Motor Mount (End of Arm)
module motor_pad() {
    difference() {
        cylinder(d=28, h=arm_thick); // Pad
        
        // Center Shaft Hole
        translate([0,0,-1]) cylinder(d=8, h=arm_thick+2);
        
        // Bolt Pattern (16x19)
        translate([motor_mount_x/2, motor_mount_y/2, -1]) cylinder(d=motor_hole_d, h=arm_thick+2);
        translate([-motor_mount_x/2, motor_mount_y/2, -1]) cylinder(d=motor_hole_d, h=arm_thick+2);
        translate([motor_mount_x/2, -motor_mount_y/2, -1]) cylinder(d=motor_hole_d, h=arm_thick+2);
        translate([-motor_mount_x/2, -motor_mount_y/2, -1]) cylinder(d=motor_hole_d, h=arm_thick+2);
    }
}

// 2. The Arm
module arm() {
    // Main Body
    translate([15, 0, 0]) // Offset from center
        cube([arm_len/1.4, 12, arm_thick], center=true); // Arm Beam
        
    // Motor Pad at Tip
    translate([arm_len/1.4 + 15, 0, 0])
        motor_pad();
}

// 3. Center Plate (Body)
module center_plate() {
    difference() {
        // Main Body Shape
        union() {
            cube([50, 50, body_thick], center=true); // Base Plate
            // FPV Camera Mount (Front)
            translate([25, 0, 10])
                cube([2, 20, 20], center=true); // Simple Bracket
        }
        
        // Stack Mounting Holes (30.5x30.5)
        translate([stack_mount/2, stack_mount/2, -10]) cylinder(d=3.2, h=20);
        translate([-stack_mount/2, stack_mount/2, -10]) cylinder(d=3.2, h=20);
        translate([stack_mount/2, -stack_mount/2, -10]) cylinder(d=3.2, h=20);
        translate([-stack_mount/2, -stack_mount/2, -10]) cylinder(d=3.2, h=20);
        
        // Weight reduction (Center Cutout)
        cube([20, 20, 20], center=true);
    }
}

// --- Assembly ---

// Center
center_plate();

// 4 Arms (X Configuration)
for (i=[0:3]) {
    rotate([0, 0, 45 + (i*90)])
        translate([30, 0, 0]) // Shift out from center
        arm();
}
