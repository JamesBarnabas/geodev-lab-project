# Week 11: Crs, Spatial Join and Spatial operations

## What this folder contains
-  my_crs.py: Here I explored the crs of my road layers, settlment layers. 
- Calculated the Road length of my study area which was 2787.5 km.  
- Additionally, I calculated the area of each wards in square kilometres and also the Lokoja Total Area. 
- What i discovered was that my crs was already in 32632 projection, and there was no need for projection again. 

- my_count.py: Here I used the sjoin and groupby to check every settlements per ward, and printed out the results. 
- However, 125 out of 127 was the only total counted settlments, i used a figure to check it and discovered the two settlements were out of the ward boundary. 

- my_reach.py: I answered one of my research questions on flooding. 
- Using the nearest distance analysis, I checked for how far each settlements are to the rivers shapefile.  
- Further, created a figure to show the wards, rivers, and a settlment distance coloured by how far they are to the river/streams. 

- my_validity.py: Here i check the validity of my wards layer (polygon) and it was valid. There was no invalid geometries. 

- Saved my nearest distance layer to my proceseed folder and also a week_11 png. to shwo n image of the map of the settlements nearest distance to the rivers.

- One limitation of my method is that the nearest distance doesn't take into consideration the terrain and geomorphology of the land, hence one cannot be certain that the distance is an absolute distance. 