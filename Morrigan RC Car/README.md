# Morrigan 1:8 4x4 RC Rock Bouncer / Crawler

Everything for our custom **Morrigan 1:8 4x4** build (Snapmaker U1 print plates, STL meshes, Shopee Indonesia BOM, and custom **Bali E-Zone** dashboard nameplate).

- **Original Printables Model:** [Morrigan 1:8 Scale RC Rock Bouncer / Crawler by Black Crow](https://www.printables.com/model/492423-morrigan-18-scale-rc-rock-bouncer-crawler-by-black) (`https://www.printables.com/model/492423-morrigan-18-scale-rc-rock-bouncer-crawler-by-black`)
- **Shopee Indonesia Shopping List (with Direct Links & Exact Variant Picks):** [Morrigan_4x4_Shopping_List_Shopee_With_Options.xlsx](./Morrigan_4x4_Shopping_List_Shopee_With_Options.xlsx)
- **3D Models:**
  - [3D Models/Plates_3MF/](./3D%20Models/Plates_3MF/) — 11 ready-to-print Snapmaker U1 `.3mf` plates
  - [3D Models/STLs/](./3D%20Models/STLs/) — All 44 `.stl` meshes (including custom [`011DashPass_BaliEZone.stl`](./3D%20Models/STLs/011DashPass_BaliEZone.stl))
- **Custom Dash Tag Generator:** [make_bali_ezone_tag.py](./make_bali_ezone_tag.py)

---

## Snapmaker U1 Plate-by-Plate Print Guide

All plates are configured for the **Snapmaker U1 (`270 x 270 mm`, `0.4 mm` nozzle)** with B2 belt-transmission settings, `0 mm`-gap `outer_and_inner` brim adhesion on tall/hollow parts, `70 °C` textured PEI bed, `0.8 mm` Spiral Lift Z-hop, and Arachne walls (`Morrigan_DashTag_BaliEZone_White.3mf` uses an anti-scorch White PLA profile).

| Plate File | Parts | Included Meshes | Recommended Color | Status / Notes |
|---|---|---|---|---|
| [`Morrigan_Plate1_FrontCage_Radiator_Dash.3mf`](./3D%20Models/Plates_3MF/Morrigan_Plate1_FrontCage_Radiator_Dash.3mf) | 11 | `001Front`, `003CSwitchGeneral`, `003RadiatorBox`, `008Shifter`, `009DashMain`, `00TestBlock`, `010DashDriver`, `011DashPassClover`, `012SteeringWheel`, `014SteeringValve`, `020Radiator` | Electric Blue | Printed (replace `011DashPassClover` with white **Bali E-Zone** dash tag below) |
| [`Morrigan_Plate2_CenterMainCage_Seats_Lights.3mf`](./3D%20Models/Plates_3MF/Morrigan_Plate2_CenterMainCage_Seats_Lights.3mf) | 1 | `002Center.stl` | Electric Blue | Printed (isolated solo cage plate) |
| [`Morrigan_Plate2B_Seats_And_LightBarCase.3mf`](./3D%20Models/Plates_3MF/Morrigan_Plate2B_Seats_And_LightBarCase.3mf) | 3 | `007Seat2X` x2, `015LightBarCase` | Black or Electric Blue | Remaining (use Black for two-tone contrast with blue cage) |
| [`Morrigan_Plate3_RoofCage_And_3WheelRings.3mf`](./3D%20Models/Plates_3MF/Morrigan_Plate3_RoofCage_And_3WheelRings.3mf) | 1 | `013Top.stl` | Electric Blue | Printed (isolated solo roof cage plate) |
| [`Morrigan_Plate3B_3WheelRings.3mf`](./3D%20Models/Plates_3MF/Morrigan_Plate3B_3WheelRings.3mf) | 3 | `253WheelRing` x3 | Electric Blue or Black | Remaining beadlock rings (pair with Plates 6 & 7) |
| [`Morrigan_Plate4_RearCage_And_B2Transmission.3mf`](./3D%20Models/Plates_3MF/Morrigan_Plate4_RearCage_And_B2Transmission.3mf) | 2 | `004RearUpper`, `005RearLower` | Electric Blue or Black | Rear upper & lower roll cage |
| [`Morrigan_Plate4B_B2Transmission.3mf`](./3D%20Models/Plates_3MF/Morrigan_Plate4B_B2Transmission.3mf) | 6 | `A2Spacer`, `B2FrontCover`, `B2MainCase`, `B2MotorPlate3542`, `B2transferCase`, `B2transferCaseCover` | Black or Electric Blue | **B2 6.25:1 GT2 Belt Transmission** (`B2MotorPlate3542` fits `3542` 4-bolt outrunner) |
| [`Morrigan_Plate5_4x4Axles_Spindles_Links_Steering.3mf`](./3D%20Models/Plates_3MF/Morrigan_Plate5_4x4Axles_Spindles_Links_Steering.3mf) | 24 | Front & rear axles, spindles, 4x hubs, 4x front `125 mm` links, 4x rear `150 mm` links, steering links, retainers | Black | Heavy drivetrain / suspension plate |
| [`Morrigan_Plate6_CenterFloor_And_2Wheels.3mf`](./3D%20Models/Plates_3MF/Morrigan_Plate6_CenterFloor_And_2Wheels.3mf) | 7 | `019CheaterBodyCenterLower`, `250WheelOuter` x2, `251WheelInner` x2, `254WheelLocker` x2 | Black | Center floor + first 2 wheels |
| [`Morrigan_Plate7_Remaining_2Wheels_And_Ring.3mf`](./3D%20Models/Plates_3MF/Morrigan_Plate7_Remaining_2Wheels_And_Ring.3mf) | 7 | `250WheelOuter` x2, `251WheelInner` x2, `253WheelRing` x1, `254WheelLocker` x2 | Black | Remaining 2 wheels + 4th beadlock ring |
| [`Morrigan_DashTag_BaliEZone_White.3mf`](./3D%20Models/Plates_3MF/Morrigan_DashTag_BaliEZone_White.3mf) | 1 | `011DashPass_BaliEZone.stl` | **White PLA** | Anti-scorch White PLA profile (`200 °C` nozzle, `210 °C` L1, ironing off, 3-loop purge skirt, `0.8 mm` Spiral Lift) |
