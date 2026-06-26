# KiCad Conversion Instructions

The KiCad conversion for `eeg-adapter` (Revision B) has been initialized.
Since the KiCad command-line tools were not available to perform the automated import, the following steps must be performed manually using the KiCad GUI.

## Prerequisites
- KiCad (Version 6.0, 7.0, or 8.0) installed on your system.
- This repository cloned.

## Steps

### 1. Open the Project
1. Launch **KiCad**.
2. Open the project file located at:  
   `/home/mhough/dev/eeg-adapter-modern/KiCad/eeg-adapter-revb.kicad_pro`

### 2. Import Schematic
1. Open the **Schematic Editor** (Escheema) from the KiCad project view.
2. If prompted to create a new schematic, say **Yes**.
3. Go to **File** -> **Import** -> **Non-KiCad Schematic...**
4. Select the Eagle Schematic file:
   `/home/mhough/dev/eeg-adapter-modern/EEGbreakout REVB/EEGbreakoutREVB.sch`
5. KiCad will convert the symbols. Review the log for any errors.
6. **Save** the schematic. It should be saved as `eeg-adapter-revb.kicad_sch` in the `KiCad` folder.

### 3. Import PCB
1. Close the Schematic Editor and open the **PCB Editor** (Pcbnew).
2. Go to **File** -> **Import** -> **Non-KiCad Board File...**
3. Select the Eagle Board file:
   `/home/mhough/dev/eeg-adapter-modern/EEGbreakout REVB/EEGbreakoutREVB.brd`
4. KiCad will convert the footprints and tracks.
5. **Save** the board. It should be saved as `eeg-adapter-revb.kicad_pcb` in the `KiCad` folder.

### 4. Link & Verify
1. In the PCB Editor, press **F8** (Update PCB from Schematic) to ensure the netlist matches.
2. Check for any missing footprints or broken nets.
3. Run **DRC** (Design Rules Check) to catch any conversion artifacts (e.g., clearance violations).

## Notes
- The Eagle files are from version 7.1.0, which should import cleanly into modern KiCad.
- Some Eagle layers might be mapped to "User" layers in KiCad. You may need to move them to appropriate technical layers if necessary.
