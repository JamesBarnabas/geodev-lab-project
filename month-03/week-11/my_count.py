import geopandas as gpd

wards = gpd.read_file("data/processed/cleaned_wards.gpkg", layer="clipped")
settlements = gpd.read_file("data/raw/lokoja_settlements.gpkg", layer="lokoja_settlements")

# Spatial join: which settlements fall inside which ward?
settlements_per_ward = gpd.sjoin(
    settlements,
    wards[["ward", "geometry"]],
    how="inner",
    predicate="within"
)

# Count settlements per ward
counts = (
    settlements_per_ward
    .groupby("ward")
    .size()
    .rename("settlement_count")
    .reset_index()
)

# Attach counts to the wards table
wards = wards.merge(counts, on="ward", how="left")

# Fix the missing values and rename the column cleanly
wards["settlements_per_ward"] = wards["settlement_count"].fillna(0).astype(int)

# Optional: drop the temporary column if you don’t need it
wards = wards.drop(columns=["settlement_count"])

print(wards[["ward", "settlements_per_ward"]])
print("Total counted:", wards["settlements_per_ward"].sum(), "of", len(settlements))
# missing = settlements[settlements.index.isin(settlements_per_ward.index)]

# print ( "Missing settlments: ", {len(missing)})
# print (missing)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 10))

# Plot wards
wards.plot(ax=ax, facecolor="lightgrey", edgecolor="black", linewidth=0.5)

# Plot all settlements in blue
settlements.plot(ax=ax, color="blue", markersize=8, label="Inside wards")

# Plot the missing ones in red
missing.plot(ax=ax, color="red", markersize=20, label="Outside wards")

ax.legend()
plt.title("Settlements vs Wards")
plt.show()