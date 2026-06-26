# KiCad Conversion Task List

This project contains Eagle design files. The primary target for conversion is the **EEGbreakout REVB** folder.
Since KiCad CLI tools were not available for automated conversion, a project structure has been prepared for **manual import**.

## Preparation
- [x] Create project directory `KiCad`
- [x] Create `KiCad/eeg-adapter-revb.kicad_pro`
- [x] Create `KiCad/README_CONVERSION.md` with instructions

## Manual Conversion Steps (See `KiCad/README_CONVERSION.md`)

### 1. Schematic Import
- [ ] Open `KiCad/eeg-adapter-revb.kicad_pro` in KiCad.
- [ ] Open Schematic Editor.
- [ ] **File -> Import -> Non-KiCad Schematic...**
- [ ] Select `EEGbreakout REVB/EEGbreakoutREVB.sch`.
- [ ] Save as `KiCad/eeg-adapter-revb.kicad_sch`.

### 2. PCB Import
- [x] Open PCB Editor.
- [x] **File -> Import -> Non-KiCad Board File...**
- [x] Select `EEGbreakout REVB/EEGbreakoutREVB.brd`.
- [x] Save as `KiCad/eeg-adapter-revb.kicad_pcb` (Completed using `kicad-cli pcb import`).

### 3. Verification
- [x] Run ERC in Schematic (Completed using `kicad-cli sch erc`).
- [x] Run DRC in PCB (Completed using `kicad-cli pcb drc`).
- [x] Update PCB from Schematic (F8) to sync netlists (Completed in KiCad GUI by linking reference designators).

## Outputs Generated
- [x] Gerber files plotted in `KiCad/Gerbers/` (F.Cu, B.Cu, F.Silk, B.Silk, F.Mask, B.Mask, Edge.Cuts)
- [x] Excellon Drill files generated in `KiCad/Gerbers/`

