class Car:
	def __init__(self):
		self.__wheels = list()
		self.__engine = None
		self.__body = None

	def set_body(self, body):
		self.__body = body

	def attach_wheel(self, wheel):
		self.__wheels.append(wheel)

	def set_engine(self, engine):
		self.__engine = engine

	def specification(self):
		print("body: %s" % self.__body.shape)
		print("engine horsepower: %d" % self.__engine.horsepower)
		print("tire size: %d\'" % self.__wheels[0].size)


# parts
class Wheel:
	size = None


class Engine:
	horsepower = None


class Body:
	shape = None


class Director:
	__builder = None

	def set_builder(self, builder):
		self.__builder = builder

	def get_car(self):
		car = Car()

		body = self.__builder.get_body()
		car.set_body(body)

		engine = self.__builder.get_engine()
		car.set_engine(engine)

		i = 0
		while i < 4:
			wheel = self.__builder.get_wheels()
			car.attach_wheel(wheel)
			i += 1

		return car


class BuilderInterface:
	def get_wheels(self): pass

	def get_engine(self): pass

	def get_body(self): pass


class JeepBuilder(BuilderInterface):
	def get_wheels(self):
		wheel = Wheel()
		wheel.size = 22
		return wheel

	def get_engine(self):
		engine = Engine()
		engine.horsepower = 400
		return engine

	def get_body(self):
		body = Body()
		body.shape = 'SUV'
		return body


class NissanBuilder(BuilderInterface):
	def get_wheels(self):
		wheel = Wheel()
		wheel.size = 16
		return wheel

	def get_engine(self):
		engine = Engine()
		engine.horsepower = 100
		return engine

	def get_body(self):
		body = Body()
		body.shape = 'hatchback'
		return body


d = Director()
d.set_builder(JeepBuilder())
print(d)
d.get_car()
d.get_car().specification()

d2 = Director()
d2.set_builder(NissanBuilder())
d2.get_car()
d2.get_car().specification()
