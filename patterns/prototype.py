from copy import deepcopy


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		print(f'({self.x}, {self.y})')

	def move(self, x, y):
		self.x += x
		self.y += y

	def clone(self, move_x, move_y):
		obj = deepcopy(self)
		obj.move(move_x, move_y)
		return obj


p1 = Point(0, 0)
p1.__str__()
p1.move(3, 5)
p1.__str__()

p2 = p1.clone(2, 2)
p2.__str__()
