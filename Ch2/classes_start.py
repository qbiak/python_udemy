#
# Example file for working with classes
#


class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, some_string):
        print("myClass method2" + some_string)


class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")

    def method2(self, some_string):
        print("anotherClass method2" + some_string)


def main():
    c = myClass()
    c.method1()
    c.method2("my new string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("my new string")


if __name__ == "__main__":
    main()
