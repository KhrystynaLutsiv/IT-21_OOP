class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        # Implementing reverse multiplication for scalar * vector
        return self.__mul__(scalar)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

# Example usage
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print("v1 =", v1)
print("v2 =", v2)

print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)
print("2 * v1 =", 2 * v1)
print("v2 * 3 =", v2 * 3)
