import geopandas as gpd

wards = gpd.read_file("data/processed/cleaned_wards.gpkg", layer="clipped")
roads = gpd.read_file("data/raw/lokoja_roads.gpkg", layer="lokoja_clipped_roads")

# # 1. Make sure both layers speak the same CRS
roads = roads.to_crs(wards.crs)

# # 2. SORT: give every road the ward it touches
# roads_per_ward = gpd.sjoin(
#     roads,
#     wards[["ward", "geometry"]],
#     how="inner",
#     predicate="within"      # was "within"
# )

# # 3. COUNT: roads in each ward
# counts = (
#     roads_per_ward
#     .groupby("ward")
#     .size()
#     .rename("road_count")
#     .reset_index()
# )

# # 4. WRITE ON THE PIGEONHOLE: attach counts to WARDS (not roads)
# wards = wards.merge(counts, on="ward", how="left")
# wards["road_count"] = wards["road_count"].fillna(0).astype(int)

# print(wards[["ward", "road_count"]])
# print("Total counted:", wards["road_count"].sum(), "of", len(roads))

roads_m = roads.to_crs(32632)            # metres (UTM zone 32N, covers Lokoja)
wards_m = wards.to_crs(32632)
pieces = gpd.overlay(roads_m, wards_m[["ward","geometry"]], how="intersection")
pieces["len_km"] = pieces.length / 1000
km = pieces.groupby("ward")["len_km"].sum().reset_index()
print (km)