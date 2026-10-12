# Month 1 Summary — Lokoja River Buffer & Settlement Analysis

## 1. Question

### How many settlements fall within a 2,000 m flood-prone buffer of the river networks in Lokoja LGA?
I chose this question to transition from basic tool practice to addressing a core component of my Lokoja flood analysis: evaluating how proximity to major water bodies exposes local settlements to potential flooding hazards.

---
## 2. Numeric Prediction
Before running the geoprocessing and intersection operations, I formulated the following numeric prediction:
* **Total estimated settlements in buffer:** Approximately **60 to 70** settlement points out of the 127 settlements.

## 3. Operation

For this analysis, I:
1. Extracted **waterway and river data** for Lokoja using QuickOSM and verified the layer was set to a proper Projected CRS (**UTM Zone 32N / EPSG:32632**) for accurate metre-based measurement.
2. Created a **2,000 m Euclidean buffer** around the Lokoja river shapefile, ensuring that it is dissolved to ensure correct analysis. 
3. Performed a **spatial intersection** between the Lokoja settlement layer and the 2,000 m river buffer zone.

## 4. The Four Quality Checks

To ensure the integrity of the spatial operation, I performed four mandatory checks:

1. **Map Look:**
   * *Observation:* Visual inspection in QGIS confirmed that the 2,000 m buffer zone cleanly flanks both major river channels within Lokoja LGA. The resulting intersection points were verified to fall strictly within the polygon boundaries, with no stray points appearing outside the buffer zones. 

2. **Row Count vs. Prediction:**
   * *Observation:* My initial prediction estimated roughly 60 to 70 features. The final intersection layer yielded **90 features**. The actual count closely aligns with my prediction, validating that the spatial query captured the expected magnitude of riverside settlements.

3. **One Feature by Hand:**
   * *Observation:* I manually selected five different settlement points located near and away from the rivers in Lokoja and used the QGIS measuring tool to check its distance to the nearest riverbank channel. The measured distance gave correct results, with those that are away also showing figures higher than 2km. 

4. **Empty Geometry Check:**
   * *Observation:* I inspected the attribute table and ran a geometry validity check on the output intersection layer. There were **0 empty, null, or invalid geometries**, ensuring all resulting records contained valid point coordinates.

## 5. Limitations

While this buffer analysis successfully isolates near-river settlements, it has notable limitations:
* **Elevation Context Missing:** Proximity alone does not confirm actual flood risk; a settlement within 1,500 m of a river sitting on a high ridge faces very different risks than one on a low-lying floodplain.

  ## 6. What I Still Need

To advance this analysis, my next steps include:
* Integrating a **Digital Elevation Model (DEM)** for Lokoja to extract slope and elevation profiles.
* Combining the distance buffer with elevation thresholds to isolate true low-lying flood-prone areas from elevated terrain near the rivers.
  
## 7. Key Lesson

> **Buffering creates a zone around a spatial feature based on a specified distance. The result depends on both the input features and the coordinate reference system used.**

I now understand the basic concept of buffering and can apply it to:

- Rivers
- Streams
- Roads
- Buildings
- Drainage networks
- Flood-prone areas

This gives me a foundation for the next stages of my **Lokoja flood analysis project**.

---

## 8. Month 1 Takeaway

The main lesson from this exercise is that **buffer analysis is not just about choosing a distance**. I also need to consider:

1. **What feature am I buffering?**
2. **Is the feature dataset complete?**
3. **What distance is appropriate for the research question?**
4. **Is the layer using the correct CRS for distance-based analysis?**
5. **What other datasets should be combined with the buffer?**

This will help me move from simply performing GIS operations to understanding **why and when each operation is useful** in my flood analysis.
