# Data notes

## GRID3 NGA - Operational LGA Boundaries

- Source: https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about
- Downloaded: 9-9-2026
- 774 features, polygons
- Columns: lga_name (text), lga_code (numbers), statename (text), statecode (text).
- No nulls in lga_name
- Covers my area of interest (LOKOJA LGA)

## OSM roads, extracted via QuickOSM
- Query: highway =* within Lokoja LGA extent
-Extracted: [9-9-2026]
- 8261 features, lines 
- Not all the features had the surface categorized as paved or unpaved. 
- However, all the highway categories was well represented, with no null values. 
- The LGA roads was covered showing high features in the built-up areas and sparse road in rural or vegetated areas. 
-

## GLOBAL COPERNICUS 30M ELEVATION DATA
- Source: Extracted from opentopography plugin in QGIS
- Covered my area of study
- 30 m resolution

## CRS AND PREPARATION
- All source layers arrived in EPSG: 4326
- Study area: Lokoja LGA, extracted from GRID3 LGA 
- All layers clipped to study area, then reprojected to EPSG: 32632 (UTM 32N), this was done to put get the measurements well defined and accurate, road layers clipped to the LGA to ensure that all the analysis sticks within the area of interest. 
- Area check: Lokoja Area 3187 km2, matches published figure. 
- Working files in data/processed/, raw files untouched.

  ##  QUALITY CHECKS
- COMPLETENESS: Checked most of the major roads, with no null values covering majorly the urban area which makes it useful for the analysis.
- CURRENT STATE: Most of the roads were covered, covering  about 2024 till date
- Positional: raods align well with satellite imagery
- Attribute Accuracy: The roads seems okay, and well labelled, however the road names are not that correct, and shouldn't be used for decision making.
- FITNESS: Adequate for checking infrastructure affected during flood, not adequate for road characteristics or quality questions. 
