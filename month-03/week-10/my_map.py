import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("data/processed/cleaned_wards.gpkg", layer="clipped")
settlements = gpd.read_file(
    "data/raw/lokoja_settlements.gpkg", layer="lokoja_settlements"
)

fig, ax = plt.subplots(figsize=(10, 10))

# colour by wards
wards.plot(
    ax=ax,
    column="ward",
    cmap="Set3",
    edgecolor="black",
    linewidth=0.5,
    legend=True,
    legend_kwds={
        "bbox_to_anchor": (1.05, 1),
        "loc": "upper left",
        "title": "Wards",
    },
)

# Plot settlements on top
settlements.plot(ax=ax, color="black", markersize=8, label="Settlements")

ax.set_title("Lokoja Wards and Settlements", fontsize=16)
ax.set_axis_off()

fig.savefig("month-03/week-10/my_map.png", dpi=300, bbox_inches="tight")
print("Map saved as my_map.png")