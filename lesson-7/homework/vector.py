from math import *
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __rmul__(self, number):
        return Vector3D(self.x * number, self.y * number, self.z * number)
    
    def magnitude(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalize(self):
        magnitude = self.magnitude()
        return Vector3D(round(self.x / magnitude, 3), round(self.y / magnitude, 3), round(self.z / magnitude, 3))
    
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print(v1)
v3 = v1 + v2
print(v3)
v4 = v2 - v1
print(v4)
dot_product = v1 * v2
print(dot_product)
v5 = 3 * v1
print(v5)
print(v1.magnitude())
v_unit = v1.normalize()
print(v_unit)
