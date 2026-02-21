# Tools
- Python, VS Code, GitHub, Shapely 

# Overview of the Laboratory
- The focus of this exercise is to integrate the Shapely geometry library, adopt structured dictionary-based attributes, and implement inheritance to support shared spatial abstraction.

# Conceptual Reflection - Part B: Refactor Point to Use Shapely
- The difference between the Lab 2 and 3 is that the internal representation of the Point class changed from storing raw lon and lat attributes to storing a geometry object created using Shapely. While the implementation shifted from manual coordinate handling (.lat and .long) to a professional geometry engine (.geometry), the external behavior of the class remained the same. The way we write the script is still the same such as to_tuple() and distance_to() and they still behave exactly as they did in Lab 2.
- Spatial computation now lives within Shapely. When we create a ShapelyPoint, it is not just storing coordinates but it is also creating a geometry object that will then handle operations like buffer or distance calculation that we did in this laboratory exercise.


# Conceptual Reflection - Part C:  Designing a Spatial Hierarchy (Inheritance)
- In real-world terms, SpatialObject represents the idea of a spatial entity in a GIS system. SpatialObject is considered an abstraction because it hides its specific meaning like it does not define whether the object is a parcel, point, or building. It only tells us that this object exist and has geometry.  
- Inheritance allows us to define a class that inherits all the methods and properties from another class. So if a new spatial methods such as distance_to() is added to the base class, every subclass automatically receives that functionality. So instead of writing codes multiple times, we can easily define it once.
- This is a structural decision because it defines how the data is organized, not what the object does. When we write the script, our only goal is on how to store the data of our object, which does not change behavior of our object.
- If we add a new method in our base class, SpatialObject, all subclasses automatically has those new methods. This hierarchical design makes the spatial system more scalable because shared spatial structure and behavior are defined once in the SpatialObject base class and automatically inherited by all subclasses. Instead of defining geometry storage, bounding box logic, and spatial methods separately in classes like point, parcel, or building, these common features exist in one centralized location. As a result, when a new spatial type such as road or boundary is added, it can simply inherit from SpatialObject and immediately gain all shared spatial capabilities without rewriting code.


# Reflection - Challenge Exercise
## Challenge 1  — from_dict() (Data → Object Boundary) 
- from_dict() should delegate validation to the constructor because the constructor is the single source of truth for enforcing object invariants. The constructor’s job is to ensure that every Point object is valid at the moment it is created. from_dict() is simply an alternative way to construct a Point from structured data. Its job is not to enforce rules, but to pass the data to the constructor and let the constructor enforce them.
## Challenge 2 — as_dict() (Structured Output)
- as_dict() is implemented inside the object because converting a Point into a structured dictionary is part of the object’s responsibility. The Point class knows its own internal structure — including that coordinates are stored inside a geometry object (from Shapely) — and therefore it is the correct place to define how the object should be represented externally.
- as_dict() produces a data representation, not an internal object structure. It separates internal geometry engine representation from external data exchange format
## Challenge 3 — intersects() in SpatialObject (Inheritance) 
- intersects() represents a shared spatial behavior, it determines whether two objects in space overlap. Both Point and Parcel can perform this operation, but the logic does not depend on the specific type of the object — it only depends on the geometry. If it were duplicated in each subclass, you would have repeated code and higher risk of errors or inconsistent behavior.
- If for example another subclass like building is added from our base class SpatialObject, no changes are required to support intersects(). With the reason being that the method is already defined in the base class and inheritance automatically gives building access to intersects().