import geopandas as gpd
wards = gpd.read_file("data/processed/cleaned_wards.gpkg", layer="clipped")

print ( "The geometry is valid, True or False: ", wards.is_valid.all())