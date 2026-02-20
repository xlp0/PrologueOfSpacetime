/*
  Digital Synesthesia: Basic Turbine Model (SCAD)
  
  Role: The Engine / The Flow.
  Function: Demonstrates Fluid Dynamics (Wind/Water/Air).
  
  This is a parametric model. Change the variables below to customize.
*/

$fn = 100; // Resolution

// Parameters
hub_d = 10;         // Hub Diameter (mm)
blade_count = 8;    // Number of Blades
blade_length = 20;  // Length of each blade from hub center (mm)
blade_thick = 2;    // Thickness of blade (mm)
height = 10;        // Total Height (mm)
twist_angle = 45;   // Twist of the blades (degrees)
hole_d = 2;         // Shaft hole size (mm)

// The Hub (Center)
module hub() {
    difference() {
        cylinder(d=hub_d, h=height, center=true);
        cylinder(d=hole_d, h=height + 2, center=true); // Shaft Hole
    }
}

// A Single Blade
module blade() {
    linear_extrude(height=height, twist=twist_angle, center=true)
        translate([hub_d/2 - 1, 0, 0]) // Start slightly inside hub
            square([blade_length, blade_thick], center=true);
}

// Assembly
union() {
    hub();
    
    // Create Blades in a Circle
    for (i = [0 : blade_count - 1]) {
        rotate([0, 0, i * (360 / blade_count)])
            blade();
    }
}
