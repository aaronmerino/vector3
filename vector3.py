from __future__ import annotations
import math

class Vec3:

    def __init__(self, x: float=0, y: float=0, z: float=0):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return math.sqrt(self.x * self.x
                        + self.y * self.y
                        + self.z * self.z)

    def dot(self, v: Vec3):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def normalize(self):
        len = self.length()

        if (len > 0):
            invLen = 1 / len
            self.x = self.x * invLen
            self.y = self.y * invLen
            self.z = self.z * invLen
    
    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

if __name__ == "__main__":
    vector1 = Vec3(2,2,2)
    print(vector1)
    print(vector1.length())
    vector1.normalize()
    print(vector1)