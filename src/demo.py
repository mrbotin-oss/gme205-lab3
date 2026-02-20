from spatial import Point 

p = Point("A", 121.0, 14.6) 
print(p.id, p.geometry.x, p.geometry.y) 
print("Tuple:", p.to_tuple())

q = Point("B", 122, 13.6)
d = p.distance_to(q)
print("Distance from A to B:", d)

