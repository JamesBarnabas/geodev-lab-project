# Check my lga vector layer, wards layer and settlements layer
import geopandas as gpd
#print (gpd.list_layers("data/raw/lokoja_settlements.gpkg"))
print (gpd.list_layers("data/raw/lokoja_wards.gpkg"))
#Clipped is the layer name as exported from QGIS. It is the only layer in the file.
wards = gpd.read_file("data/raw/lokoja_wards.gpkg", layer="clipped")
settlements = gpd.read_file ("data/raw/lokoja_settlements.gpkg", layer="lokoja_settlements")
print (wards.head())
print (settlements.head())
print (wards.columns)
print (settlements.columns)

# Clean the dataset, there are some wards from the clipped Lokoja Layer that shows up in other LGAS. 
# Filter and clean the Lokoja wards layer to only include wards in Lokoja LGA.
cleaned_wards = wards[wards["lga"] == "Lokoja"]
print (cleaned_wards.head())
print ('The number of wards in lokoja before cleaning is ', len(wards))
print ('The number of wards in lokoja after cleaning is ', len(cleaned_wards))

print("The following wards are found in Lokoja LGA:", cleaned_wards["ward"].tolist())

print ("--------------------------")
print (cleaned_wards.geom_type.value_counts())
print ("CRS: ", cleaned_wards.crs)
print ("Bounds: ", cleaned_wards.total_bounds)
print ("Rows and columns: ", cleaned_wards.shape)
cleaned_wards.to_file(
    'data/processed/cleaned_wards.gpkg',
    layer='clipped')