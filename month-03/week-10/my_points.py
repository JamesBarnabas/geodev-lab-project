# Here i have a csv points of petrol stations in Lokoja LGA.
from turtle import filling

import pandas as pd
import geopandas as gpd
table = pd.read_csv("data/raw/petrol_stations.csv")
print (table.head(3))

#import the petrol_stations as csv
filling_stations= gpd.GeoDataFrame(table, geometry=gpd.points_from_xy(table["longitude"], table ["latitude"]), crs = "EPSG:32632")
print (filling_stations.head(3))
print (filling_stations.crs)

filling_stations.to_file ("data/processed/filling_stations.gpkg", layer ="filling_stations")
print ("Saved", len (filling_stations), "filling stations")
