/*
  Digital Synesthesia: The Wind Turbine Stand (SCAD)
  
  Role: The Foundation.
  Function: Elevates the Turbine the user already has.
  
  Specs:
  - Height: 175mm (Center of shaft, exceeds 170mm min).
  - Length: 160mm (Aerodynamic base).
  - Bearings: 2x 699 (or exact 9mm ID, 20mm OD).
  
  Features:
  - Strong A-Frame base.
  - Generous center cutout to save filament.
  - Bearing pockets with 20.3mm tolerance for easy press-fit on standard 3D printers.
*/

$fn = 100;

// --- Parameters ---
// Dimensions
stand_h = 175;       // Height to center of bearings
base_len = 160;      // Length of the base (Wind direction)
base_width = 80;     // Width of the base (Stability)
housing_len = 50;    // Length of the top tube (gap between bearings)
housing_od = 32;     // Outer diameter of the horizontal tube

// Bearing Constraints (9mm ID, 20mm OD)
bearing_od = 20.3;   // Adds 0.3mm clearance for 3D printer shrinkage
bearing_id = 9.0;    // 9mm
bearing_depth = 6.0; // Fit a 6mm-wide bearing (standard 699 or 689)
shaft_clear = 13.0;  // Generous clearance hole so the 9mm shaft won't rub

module turbine_stand() {
    difference() {
        // 1. Solid Body (Pyramid/A-Frame Base)
        hull() {
            // Main Base plate
            translate([0, 0, 5]) 
                cube([base_len, base_width, 10], center=true);
            
            // Top bearing housing (horizontal tube)
            translate([0, 0, stand_h])
                rotate([0, 90, 0])
                cylinder(d=housing_od, h=housing_len, center=true);
        }
        
        // 2. Large Center Cutout (Save material, keep structural strength)
        translate([0, 0, stand_h/2 + 5])
            scale([1.2, 1, 1]) // Stretch into oval
            rotate([90, 0, 0])
            cylinder(d=stand_h - 45, h=base_width + 20, center=true);
            
        // 3. Bearing Pockets & Shaft Geometry
        translate([0, 0, stand_h]) {
            // Central shaft pass-through (so shaft doesn't drag)
            rotate([0, 90, 0])
                cylinder(d=shaft_clear, h=housing_len + 10, center=true);
            
            // Front Bearing Pocket (20.3mm wide, 6mm deep by default)
            translate([housing_len/2 - bearing_depth/2 + 0.1, 0, 0])
                rotate([0, 90, 0])
                cylinder(d=bearing_od, h=bearing_depth + 0.2, center=true);
                
            // Rear Bearing Pocket
            translate([-housing_len/2 + bearing_depth/2 - 0.1, 0, 0])
                rotate([0, 90, 0])
                cylinder(d=bearing_od, h=bearing_depth + 0.2, center=true);
        }
        
        // 4. Mounting Holes (M5 Screws for fixing to a desk/floor)
        translate([base_len/2 - 15, base_width/2 - 15, -1]) cylinder(d=5.5, h=25);
        translate([base_len/2 - 15, -base_width/2 + 15, -1]) cylinder(d=5.5, h=25);
        translate([-base_len/2 + 15, base_width/2 - 15, -1]) cylinder(d=5.5, h=25);
        translate([-base_len/2 + 15, -base_width/2 + 15, -1]) cylinder(d=5.5, h=25);
    }
}

// Render the Stand
turbine_stand();
