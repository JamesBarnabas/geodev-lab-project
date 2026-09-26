# Month 1 Summary — Buffer Analysis

## 1. Question

### What does a 2,000 m distance from a road show?

I chose this question because, going forward, I may want to understand:

- How many buildings fall within a flood-prone area.
- How far buildings are from a river channel or stream.
- How buffer analysis can be used to identify areas within a specific distance of a spatial feature.

I therefore wanted to understand how **buffer analysis** works before applying it to my flood analysis.

---

## 2. Operation

For this exercise, I:

1. Used an **OpenStreetMap road shapefile**.
2. Created a **2,000 m buffer** around the roads.
3. Checked the resulting buffer to understand how the distance was applied.
4. Dissolved the buffer to understand how overlapping road buffers can be combined.

### Basic Idea

```text
Road
  ↓
2,000 m Buffer
  ↓
Area within 2,000 m of the road
```

The purpose was not to determine the final buffer distance for my flood analysis, but to understand how the operation works.

---

## 3. Expected

I expected the buffer to create a **2,000 m zone around the available roads**.

I also wanted to see:

- The areas covered by the road buffers.
- Buildings located within the buffered areas.
- How the buffer behaves when roads are close to each other.
- What happens when the buffers are dissolved.

This was mainly a learning exercise before applying the same concept to **rivers, streams, and other drainage features**.

---

## 4. What I Observed

One of the things I noticed was that the roads did not cover **all parts of the LGA**.

As a result, some areas did not have a buffer, particularly areas with:

- Lower levels of development.
- Fewer mapped roads.
- Limited road coverage in the OpenStreetMap dataset.

This helped me understand an important concept:

> **A buffer can only be created around the features that exist in the input dataset.**

If a road, river, or stream is missing from the dataset, the resulting buffer will also be missing in that location.

---

## 5. Limitations

At this stage, there are still some limitations:

- I have not yet obtained the **river and stream data** needed for the next stage.
- I have not started the **DEM analysis** yet.
- The current exercise was based only on the available **OpenStreetMap road data**.
- The **2,000 m distance** was used only as a learning example and is not yet the final distance I will use in the flood analysis.

---

## 6. What I Still Need

My next step is to obtain reliable:

- **River data**
- **Stream data**
- **Drainage network data**

I will then test appropriate buffer distances around these features based on the research question and available data.

This will become more useful when combined with the **DEM analysis**, because I will be able to examine the relationship between:

```text
Rivers + Streams
       ↓
Elevation / DEM
       ↓
Flood-prone areas
       ↓
Buildings and other exposed features
```

---

## 7. Additional Learning — Geographic CRS

I also tried creating the buffer while the layer was still in a **geographic coordinate reference system (CRS)**.

The buffer was created, but the result appeared as a large circular/ring-like feature and the process continued loading.

The issue was that the geographic CRS uses **degrees** as its coordinate units rather than metres.

This helped me understand why distance-based analysis should generally be performed using an appropriate **projected CRS**, where distances can be measured in units such as metres.

### Geographic CRS

```text
Coordinates → Degrees
Example     → EPSG:4326
```

### Projected CRS

```text
Coordinates → Metres
Example     → UTM
```

For example:

```text
2,000 metres  → Meaningful distance for a buffer
2,000 degrees → Not a meaningful distance for this analysis
```

---

## 8. Key Lesson

> **Buffering creates a zone around a spatial feature based on a specified distance. The result depends on both the input features and the coordinate reference system used.**

I now understand the basic concept of buffering and can apply it later to:

- Rivers
- Streams
- Roads
- Buildings
- Drainage networks
- Flood-prone areas

This gives me a foundation for the next stages of my **Lokoja flood analysis project**.

---

## 9. Month 1 Takeaway

The main lesson from this exercise is that **buffer analysis is not just about choosing a distance**. I also need to consider:

1. **What feature am I buffering?**
2. **Is the feature dataset complete?**
3. **What distance is appropriate for the research question?**
4. **Is the layer using the correct CRS for distance-based analysis?**
5. **What other datasets should be combined with the buffer?**

This will help me move from simply performing GIS operations to understanding **why and when each operation is useful** in my flood analysis.