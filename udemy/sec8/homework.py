import math


class Line:
	def __init__(self, coor1, coor2):
		self.x = coor2[0] - coor1[0]
		self.y = coor2[1] - coor1[1]

	def distance(self):
		return math.sqrt(self.x**2 + self.y**2)

	def slope(self):
		return self.y / self.x


class Cylinder:
	def __init__(self, height=1, radius=1):
		self.circle_area = math.pi * radius**2
		self.circle_circuit = 2 * math.pi**2
		self.height = height

	def volume(self):
		return self.circle_area * self.height

	def surface_area(self):
		return (2 * self.circle_area) + (self.circle_circuit * self.height)


line1 = Line((3, 2), (8, 10))
print(line1.distance())
print(line1.slope())

cylinder1 = Cylinder()
cylinder2 = Cylinder(2, 3)
print(cylinder1.volume())
print((cylinder1.surface_area()))
print(cylinder2.volume())
print((cylinder2.surface_area()))
