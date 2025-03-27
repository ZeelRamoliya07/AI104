# Create a class for representing any 2-D point or vector. The methods inside this class include
# its magnitude and its rotation with respect to the X-axis. Using the objects define functions for
# calculating the distance between two vectors, dot product, cross product of two vectors. Extend
# the 2-D vectors into 3-D using the concept of inheritance. Update the methods according to 3-
# D.

import math

# Class representing a 2D vector
class Vector2D:
    def _init_(self, x, y):
        self.x = x
        self.y = y
    
    #magnitude of the vector
    def magnitude(self):
        return math.sqrt(self.x*2 + self.y*2)
    
    # angle with respect to the x-axis
    def angle_with_x_axis(self):
        return math.degrees(math.atan2(self.y, self.x))
    
    # distance between two vectors
    def distance(self, other):
        return math.sqrt((self.x - other.x)*2 + (self.y - other.y)*2)
    
    # dot product of two vectors
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y
    
    # cross product of two vectors
    def cross_product(self, other):
        return self.x * other.y - self.y * other.x

# Extending 2D vector into a 3D vector
class Vector3D(Vector2D):
    def _init_(self, x, y, z):
        super()._init_(x, y)
        self.z = z
    
    #  magnitude
    def magnitude(self):
        return math.sqrt(self.x*2 + self.y2 + self.z*2)
    
    # dot product of two 3D vectors
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    # cross product of two 3D vectors
    def cross_product(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )


def main():
    choice = int(input("Enter 2 for 2D vector, 3 for 3D vector: "))
    
    if choice == 2:
        x1, y1 = map(int, input("Enter x and y for first vector: ").split())
        x2, y2 = map(int, input("Enter x and y for second vector: ").split())
        v1 = Vector2D(x1, y1)
        v2 = Vector2D(x2, y2)
    
        print("Magnitude of v1:", v1.magnitude())
        print("Magnitude of v2:", v2.magnitude())
        print("Angle of v1 with x-axis:", v1.angle_with_x_axis())
        print("Distance between v1 and v2:", v1.distance(v2))
        print("Dot product of v1 and v2:", v1.dot_product(v2))
        print("Cross product of v1 and v2:", v1.cross_product(v2))
    
    elif choice == 3:
        x1, y1, z1 = map(int, input("Enter x, y, and z for first vector: ").split())
        x2, y2, z2 = map(int, input("Enter x, y, and z for second vector: ").split())
        v3 = Vector3D(x1, y1, z1)
        v4 = Vector3D(x2, y2, z2)
    
        print("Magnitude of v3:", v3.magnitude())
        print("Magnitude of v4:", v4.magnitude())
        print("Dot product of v3 and v4:", v3.dot_product(v4))
        cross_v3_v4 = v3.cross_product(v4)
        print("Cross product of v3 and v4:", (cross_v3_v4.x, cross_v3_v4.y, cross_v3_v4.z))
    
    else:
        print("Invalid choice!")

# Run the program
if __name__== "__main__":
    main()