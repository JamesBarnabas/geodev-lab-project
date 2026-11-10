# Week 10: Geopandas, layers as tables

## What this folder contains
-  my_explore.py: Here i looked at my wards table, and i discovered that the clipping had added some other lga wards into the layer. 
- I cleaned it using lga, and turned it into cleaned_wards, which now allows my number of wards to fall within the correct number of wards in Lokoja LGA which is 10 instead of 25. 
- I also explored the columns, and rows to get a general description of what i have in my data using geopandas. 

- my_points.py: I imported a filling stations data that had longitude and latitude and converted it into points, i made sure to set the crs to the crs of the wards geopackage layer. 

- my_join.py: I joined the wards attriubute on the filling stations to my wards layer, which allows me to get some other information from my cleaned_wards layer, and added it to my petrol filling stations layers. This allowed me to learn about spatial join. 
- Note: The spatial join doesn't give any information about the project, just a way to learn how the join works. 

- My_map.py: Displays the map i did showing the settlements in Lga, layered above the ward shapefile. coloured by ward colours. 