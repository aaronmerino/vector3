import math

class Vec3:

    def __init__(self, x: float=0, y: float=0, z: float=0):
        self.vec3 = (x,y,z)

    def length(self):
        return math.sqrt(self.vec3[0] * self.vec3[0]
                        + self.vec3[1] * self.vec3[1]
                        + self.vec3[2] * self.vec3[2])

    def normalize(self):
        len = self.length()

        if (len > 0):
            invLen = 1 / len
            self.vec3 = (self.vec3[0] * invLen, self.vec3[1] * invLen,
                        self.vec3[2] * invLen)

    def __str__(self):
        return "(" + str(self.vec3[0]) + ", " + str(self.vec3[1]) + ", " + str(self.vec3[2]) + ")"

if __name__ == "__main__":
    vector1 = Vec3(2,2,2)
    print(vector1)
    print(vector1.length())
    vector1.normalize()
    print(vector1)