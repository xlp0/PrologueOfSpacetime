/*
  Digital Synesthesia: The Wind Turbine Stand (Drop-in Style)
  
  Role: The Foundation.
  Function: Elevates an *existing* turbine.
  
  Specs:
  - Height: >170mm.
  - Length: 160mm.
  - Bearing Outer Diameter (OD): 20mm.
  - Bearing Inner Diameter (ID): 9mm (Shaft).
  
  Features:
  - Dual rectangular towers.
  - U-shaped slots at the top for easy "drop-in" of the 20mm bearings.
*/

$fn = 100;

// --- Parameters ---
// Overall Dimensions
base_len = 160;      // Distance between the towers (Length of base)
base_width = 80;     // Width of the base plate for stability
base_thick = 10;     // Thickness of the base plate

tower_h = 175;       // Total height of the towers
tower_width = 30;    // Width of each rectangular tower (in X)
tower_depth = 40;    // Depth of each rectangular tower (in Y)

// Bearing Constraints
bearing_od = 20.5;   // 20mm + 0.5mm clearance for easy sliding
bearing_w = 7.0;     // Approx width of a standard 9x20 bearing (699 is 6mm, 689 is 5mm). Slot is just a cutout anyway.
slot_depth = 25;     // How deep the bearing drops into the tower

module drop_in_turbine_stand() {
    difference() {
        // --- Solid Structure ---
        union() {
            // 1. The Base Plate
            cube([base_len, base_width, base_thick], center=true);
            
            // 2. Tower 1 (Left)
            translate([-base_len/2 + tower_width/2, 0, tower_h/2])
                cube([tower_width, tower_depth, tower_h], center=true);
                
            // 3. Tower 2 (Right)
            translate([base_len/2 - tower_width/2, 0, tower_h/2])
                cube([tower_width, tower_depth, tower_h], center=true);
                
            // 4. Corner braces for strength (Optional but recommended for 170mm tall towers)
            // Left brace
            translate([-base_len/2 + tower_width, 0, base_thick/2])
                rotate([0, -45, 0])
                cube([tower_depth, tower_depth, tower_depth], center=true);
            // Right brace
            translate([base_len/2 - tower_width, 0, base_thick/2])
                rotate([0, 45, 0])
                cube([tower_depth, tower_depth, tower_depth], center=true);
        }
        
        // --- Cutouts ---
        
        // 1. Left Bearing Slot (Top of Tower 1)
        translate([-base_len/2 + tower_width/2, 0, tower_h]) {
            // Drop-in track (U-Shape)
            cube([bearing_w + 2, bearing_od, slot_depth*2], center=true); // The vertical slide
            // Rest pocket (Rounded bottom)
            translate([0, 0, -slot_depth])
                rotate([0, 90, 0])
                cylinder(d=bearing_od, h=bearing_w + 4, center=true);
        }
        
        // 2. Right Bearing Slot (Top of Tower 2)
        translate([base_len/2 - tower_width/2, 0, tower_h]) {
            // Drop-in track (U-Shape)
            cube([bearing_w + 2, bearing_od, slot_depth*2], center=true); // The vertical slide
            // Rest pocket (Rounded bottom)
            translate([0, 0, -slot_depth])
                rotate([0, 90, 0])
                cylinder(d=bearing_od, h=bearing_w + 4, center=true);
        }
        
        // 3. Mounting Holes (To screw the base down safely)
        translate([base_len/2 - 15, base_width/2 - 15, -base_thick]) cylinder(d=5.5, h=base_thick*3);
        translate([base_len/2 - 15, -base_width/2 + 15, -base_thick]) cylinder(d=5.5, h=base_thick*3);
        translate([-base_len/2 + 15, base_width/2 - 15, -base_thick]) cylinder(d=5.5, h=base_thick*3);
        translate([-base_len/2 + 15, -base_width/2 + 15, -base_thick]) cylinder(d=5.5, h=base_thick*3);
    }
}

// Render the Stand
translate([0, 0, base_thick/2]) drop_in_turbine_stand();
