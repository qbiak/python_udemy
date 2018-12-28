class ShapeInterface:
	def draw(self):
		pass


class Circle(ShapeInterface):
	def draw(self):
		print('Circle.draw')


class Square(ShapeInterface):
	def draw(self):
		print('Square.draw')


# invalid example
class Triangle:
	@staticmethod
	def draw():
		print('Triangle.draw')


class ShapeFactory:
	@staticmethod
	def get_shape(type):
		if type == 'circle':
			return Circle()
		if type == 'square':
			return Square()
		if type == 'triangle':  # only for testing purpose
			return Triangle
		assert 0, 'Could not find shape ' + type


s = ShapeFactory.get_shape('square')
print(s)
s.draw()

t = ShapeFactory.get_shape('triangle')
print(t)
t.draw()
