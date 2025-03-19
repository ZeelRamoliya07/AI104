import math

# Function to calculate Distance between two 3D points
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

# Input 10 3D points
points = []
for i in range(10):
    x, y, z = map(int, input(f"Enter the coordinates for point {i+1} (x, y, z): ").split())
    points.append((x, y, z))

# Find the nearest neighbor for each point
nearest_neighbors = []
for i in range(10):
    point = points[i]
    min_dist = None
    nearest = None
    
    for j in range(10):
        if i != j:
            dist = distance(point, points[j])
            if min_dist is None or dist < min_dist:
                min_dist = dist
                nearest = points[j]
    
    nearest_neighbors.append((point, nearest))

# Output the result
for point, neighbor in nearest_neighbors:
    print(f"Point {point} -> Nearest neighbor: {neighbor}")
