import geopandas as gpd

wards = gpd.read_file("data/processed/cleaned_wards.gpkg", layer="clipped")
settlements = gpd.read_file("data/raw/lokoja_settlements.gpkg", layer="lokoja_settlements")
rivers = gpd.read_file("data/raw/lokoja_rivers.gpkg", layer ="rivers_streams")
# rivers = gpd.list_layers ("data/raw/lokoja_rivers.gpkg")

nearest= gpd.sjoin_nearest( settlements, rivers[["geometry"]], how = "left", distance_col = "distance" \
"_m")
nearest["distance_km"] = (nearest["distance_m"]/1000).round(2)
print (nearest[["set_name", "distance_km"]])
nearest.to_file ("data/processed/nearest_settlements_to_rivers.gpkg", driver= "GPKG")

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(11, 11))

# Background
wards.plot(ax=ax, facecolor="#f0f0f0", edgecolor="grey", linewidth=0.4)
rivers.plot(ax=ax, color="#1f77b4", linewidth=1.2, alpha=0.8, label="Rivers")

# Settlements coloured by distance
nearest.plot(
    ax=ax,
    column="distance_km",
    cmap="YlOrRd",          # yellow → orange → red (farther = redder)
    markersize=35,
    legend=True,
    legend_kwds={"label": "Distance to nearest river (km)", "shrink": 0.6},
    edgecolor="black",
    linewidth=0.3
)

ax.set_title("Settlements – Distance to Nearest River", fontsize=14)
ax.set_axis_off()
plt.tight_layout()

plt.savefig("month-03/week-11/Week_11.png", dpi=300,bbox_inches="tight")
plt.show()