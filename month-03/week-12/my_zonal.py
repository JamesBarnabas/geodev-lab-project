import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

# wards_new = gpd.list_layers("data/processed/cleaned_wards.gpkg")
# print (wards_new)
with rasterio.open ("data/processed/my_ndvi.tif") as src:
    wards = gpd.read_file("data/processed/cleaned_wards.gpkg", layer = "clipped").to_crs(src.crs)
    means = []
    for geom in wards.geometry:
        cells, _ = mask(src, [geom], crop=True, filled=False)
        means.append(float(cells.mean()))
wards["mean_ndvi_m"] = np.round(means,1)
print (wards[["ward", "mean_ndvi_m"]])