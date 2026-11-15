import geopandas as gpd

wards = gpd.read_file("data/processed/cleaned_wards.gpkg",layer ='clipped')

roads = gpd.read_file ("data/raw/lokoja_roads.gpkg", layer ='lokoja_clipped_roads')

settlements = gpd.read_file("data/raw/lokoja_settlements.gpkg", layer ='lokoja_settlements')
print ("My wards crs is : ", wards.crs)
print ("My roads crs is ", roads.crs)
print ("My settlement crs is ", settlements.crs)
print ('Roads in Lokoja: ', len(roads))
print ("Road Lenth in Lokoja:, ",  round(roads.length.sum()/1000, 2), "km")

wards['area_sq_km'] = wards.area/100000
print (wards[['ward', 'area_sq_km']].head())
print ("Lokoja LGA total area: ", round(wards['area_sq_km'].sum(), 1), "km2" )

