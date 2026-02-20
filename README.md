# Conceptual Reflection - Part B: Refactor Point to Use Shapely
- The difference between the Lab 2 and 3 is that the internal representation of the Point class changed from storing raw lon and lat attributes to storing a geometry object created using Shapely. While the implementation shifted from manual coordinate handling (.lat and .long) to a professional geometry engine (.geometry), the external behavior of the class remained the same. The way we write the script is still the same such as to_tuple() and distance_to() and they still behave exactly as they did in Lab 2.
- Spatial computation now lives within Shapely. When we create a ShapelyPoint, it is not just storing coordinates but it is also creating a geometry object that will then handle operations like distance calculation that we did in this laboratory exercise.




