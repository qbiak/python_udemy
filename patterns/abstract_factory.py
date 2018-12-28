# abstract shape classes
class Shape2DInterface:
	def draw(self):
		pass


class Shape3DInterface:
	def build(self):
		pass


# concrete shape classes
class Circle(Shape2DInterface):
	def draw(self):
		print('Circle.draw')


class Square(Shape2DInterface):
	def draw(self):
		print('Square.draw')


class Sphere(Shape3DInterface):
	def build(self):
		print('Sphere.draw')


class Cube(Shape3DInterface):
	def build(self):
		print('Cube.draw')


# abstract shape factory
class ShapeFactoryInterface:
	def get_shape(sides):
		pass


# concrete shape factories
class Shape2DFactory(Shape2DInterface):
	@staticmethod
	def get_shape(sides):
		if sides == 1:
			return Circle()
		if sides == 4:
			return Square()
		assert 0, 'Bad 2D shape. Shape not defined for ' + sides + 'sides.'


class Shape3DFactory(Shape3DInterface):
	@staticmethod
	def get_shape(sides):
		if sides == 1:
			return Sphere()
		if sides == 6:
			return Cube()
		assert 0, 'Bad 3D shape. Shape not defined for ' + sides + 'sides.'


circle = Shape2DFactory.get_shape(1)
print(circle)
circle.draw()

cube = Shape3DFactory.get_shape(6)
print(cube)
cube.build()
