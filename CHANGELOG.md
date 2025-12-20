# Changelog

## [3.35-Ascension] - 2025-12-20
### Added
- **ElvUI Minimap Compatibility** - When ElvUI's minimap is enabled, Carbonite automatically disables its minimap ownership, allowing both to coexist. ElvUI manages the Blizzard Minimap while Carbonite's map window works independently.
- **FarmHud Compatibility** - Carbonite now works seamlessly with FarmHud addon. When FarmHud is active, Carbonite's minimap control is temporarily disabled to allow GatherMate2 and other minimap pins to display on the HUD.

### New Files
- `CarboniteElvUICompat.lua` - Compatibility module for ElvUI integration

---

## [3.34-Ascension] - 2025-12-20
### Fixed
- Fixed `table index is nil` error in `InT1` (Line ~24655).
- Fixed `attempt to index field 'Win1'` error in `ShU1` (Line ~8981).
- Fixed `attempt to index local 'map'` error in `GPP` (Line ~7688).
- Fixed `attempt to index local 'map'` error in `ToS1` (Line ~1956).
- Fixed `attempt to index field 'GOp'` error in `TP2` (Line ~25076).
- Fixed `attempt to index local 'map'` error in `ALP` (Line ~11906).
- Fixed `attempt to compare nil with number` error in `F` (Line ~18184).
- Fixed `attempt to index field '?'` error in `SCM1` (Line ~23842).
- Fixed `attempt to index local 'inf'` error in `ITCZ` (Line ~6978).
- Fixed `attempt to index global 'GameMenuFrame'` error in `ShowUIPanel` (Line ~6871).

### Changed
- Disabled Carbonite's internal version check and update notification.
