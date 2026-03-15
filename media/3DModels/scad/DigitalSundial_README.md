# Digital Sundial

## Overview
This OpenSCAD script (`DigitalSundial.scad`) generates a functional digital sundial. Unlike traditional sundials that cast a shadow line, this device uses a cleverly designed gnomon to project the current time in digital digits using sunlight.

## Credits
- **Author**: Mojoptix
- **Website**: [www.mojoptix.com](http://www.mojoptix.com)
- **Email**: julldozer@mojoptix.com
- **Date**: 13 October 2015
- **License**: Creative Commons CC-BY (Attribution)
- **Video Podcast**: [Episode #001](http://www.mojoptix.com/fr/2015/10/12/ep-001-cadran-solaire-numerique)

## Key Components
The script allows you to generate several distinct parts of the sundial assembly:

1.  **Gnomon**: The main part that casts the digital shadow. It displays time in 20-minute intervals (e.g., 10:00, 10:20, 10:40).
2.  **Central Connector Piece**: Connects the gnomon to the base/jar lid.
3.  **Top Part of Lid**: The upper section of the mounting mechanism.
4.  **Bottom Part of Lid**: The lower section designed to fit a standard jar (specifically a Bonne Maman jam jar).

## Configuration Parameters

### Part Selection (`FLAG_PRINT`)
Select which part to render by changing the `FLAG_PRINT` variable:
- `1`: The Gnomon
- `2`: The Central Connector Piece
- `3`: The Top Part of the Lid
- `4`: The Bottom Part of the Lid
- `10`: Display Everything

### Location Adjustment (`FLAG_northern_hemisphere`)
Set the hemisphere for correct time projection:
- `1`: Northern Hemisphere
- `0`: Southern Hemisphere

### Printing Aids
- `FLAG_gnomon_brim`: Set to `1` to add a brim to the gnomon for better bed adhesion.
- `FLAG_bottom_lid_support`: Set to `1` to add support structures for the lid teeth.

### Other Settings
- `gnomon_radius`: Radius of the gnomon (default: 30mm). Adjusting this scales the model.
- `epsilon_thickness`: Small value to prevent z-fighting in OpenSCAD preview.

## How It Works
The standard gnomon is replaced by a complex 3D-printed shape containing thousands of tiny holes. These holes are calculated to let sunlight pass through only at specific angles corresponding to the time of day.

### The Magic: Digital Shadow
- **Pixels**: The time is formed by "pixels" of light.
- **Light Guides**: Each pixel is a light guide designed to let light through for specific sun positions.
- **Time Steps**: The display updates every 20 minutes to keep the complexity manageable.

## Usage
1.  **Open** `DigitalSundial.scad` in OpenSCAD.
2.  **Configure** the `FLAG_northern_hemisphere` to your location.
3.  **Select** the part to print using `FLAG_PRINT`.
4.  **Render (F6)** and **Export as STL**.
5.  **Print** using a 3D printer (PLA or ABS recommended).
6.  **Assemble** with a jar, screws, nuts, and washers as specified in the script comments (M6 screws/nuts/washers implied by hole dimensions).

## Dependencies
- **OpenSCAD**: Required to view and compile the script.
- **Hardware**:
    - M6 Screws
    - M6 Nuts and Washers
    - Glass Jar (Bonne Maman style recommended for the lid adapter)
