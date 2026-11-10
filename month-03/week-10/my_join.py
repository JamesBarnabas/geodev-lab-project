
# Check my lga vector layer, wards layer and settlements layer
import geopandas as gpd
#Clipped is the layer name as exported from QGIS. It is the only layer in the file.
wards = gpd.read_file("data/raw/lokoja_wards.gpkg", layer="clipped")
settlements = gpd.read_file ("data/raw/lokoja_settlements.gpkg", layer="lokoja_settlements")

cleaned_wards = wards[wards["lga"] == "Lokoja"]

filling_stations = gpd.read_file("data/processed/filling_stations.gpkg", layer="filling_stations")
# 1. Define cleaning function for robust matching
def clean_name(name):
  if isinstance(name, str):
    return name.strip().upper().replace('-', ' ')
  return name


# 2. Create join keys on both datasets
cleaned_wards['join_key'] = cleaned_wards['ward'].apply(clean_name)
filling_stations['join_key'] = filling_stations['ward'].apply(clean_name)

# 3. Perform the attribute join (stations -> wards)
stations_enriched = filling_stations.merge(
    cleaned_wards.drop(
        columns='geometry'
    ),  # Drop geometry to avoid duplicate geometry columns
    on='join_key',
    how='left',
    suffixes=('', '_ward'),
)

# 4. Check match count before and after
matched_count = stations_enriched['ward_ward'].notna().sum()
print(f'Matched on attribute join: {matched_count} of {len(filling_stations)}')

# 5. Save the enriched dataset
stations_enriched.to_file(
    'data/processed/filling_stations_enriched.gpkg',
    layer='filling_stations_enriched',
)
print (stations_enriched.head())
print (stations_enriched.columns[0:5])