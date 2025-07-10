# A class object supports two kind of operations
# 1.) attribute references
# 2.) instantiation


class TestClass:
    """Doc of the class"""

    i = 1234

    def hello(self):
        return "hello world"


firstClass = TestClass()
print(firstClass.i)
print(firstClass.hello())


class Person:
    """Bio-robot"""

    organism = "animal"  # available to all instances of this class

    def __init__(self, name, surname):  # unique to each instance
        self.name = name
        self.surname = surname


person = Person(
    "Tarkan", "Mansuroğlu"
)  # this instance can either reach data attribute or methods an instance can't do anything else

print(person.name)
print(person.surname)


# Python inheritance built-in functions
# isinstance
# issubclass

# it is possible to have multiple base classes
# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>


# “Private” instance variables that cannot be accessed except from inside an object don’t exist in Python.
# However, there is a convention that is followed by most Python code:
# a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member).
# It should be considered an implementation detail and subject to change without notice.


# Name mangling
class Base:
    def __init__(self):
        self.__data = 123  # becomes _Base__data


class Derived(Base):
    def __init__(self):
        super().__init__()
        self.__data = 456  # becomes _Derived__data


# You can add a behavior to your class. Just like Rust
class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index = self.index - 1

        return self.data[self.index]


rev = Reverse("spam")

print(iter(rev))

for item in rev:
    print(item)
