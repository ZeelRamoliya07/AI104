"""
Create a class for representing any 2-D point or vector. The methods inside this class include
its magnitude and its rotation with respect to the X-axis. Using the objects define functions for
calculating the distance between two vectors, dot product, cross product of two vectors. Extend
the 2-D vectors into 3-D using the concept of inheritance. Update the methods according to 3-
D.
"""
import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def angle_with_x_axis(self):
        return math.degrees(math.atan2(self.y, self.x))
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def distance(self, other):
        diff = self - other
        return diff.magnitude()
    
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y
    
    def cross_product(self, other):
        return self.x * other.y - self.y * other.x
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance_to(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"


class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def distance(self, other):
        diff = self - other
        return diff.magnitude()
    
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross_product(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

def vector_menu():
    x, y, z = map(float, input("Enter x, y, z: ").split())
    vec = Vector3D(x, y, z)
    print("Magnitude:", vec.magnitude())

vector_menu()
