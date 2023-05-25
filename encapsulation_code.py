#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Car:
    def init(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year


my_car = Car("Toyota", "Camry", 2021)

print(my_car.get_make())  # Output: Toyota
print(my_car.get_model())  # Output: Camry
print(my_car.get_year())  # Output: 2021

my_car.set_make("Honda")
my_car.set_model("Accord")
my_car.set_year(2022)

print(my_car.get_make())  # Output: Honda
print(my_car.get_model())  # Output: Accord
print(my_car.get_year())  # Output: 2022


# In[2]:


# Python program to
# demonstrate protected members

# Creating a base class
class Base:
	def __init__(self):

		# Protected member
		self._a = 2

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling protected member of base class: ",
			self._a)

		# Modify the protected variable:
		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)


# In[4]:


class Car:
    def init(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year


my_car = Car()

print(my_car.get_make())  # Output: Toyota
print(my_car.get_model())  # Output: Camry
print(my_car.get_year())  # Output: 2021

my_car.set_make("Honda")
my_car.set_model("Accord")
my_car.set_year(2022)

print(my_car.get_make())  # Output: Honda
print(my_car.get_model())  # Output: Accord
print(my_car.get_year())  # Output: 2022


# In[5]:


class Car:
    def init(self):
        self._make = ""
        self._model = ""
        self._year = 0

    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year


my_car = Car()

my_car.set_make("Toyota")
my_car.set_model("Camry")
my_car.set_year(2021)

print(my_car.get_make())  # Output: Toyota
print(my_car.get_model())  # Output: Camry
print(my_car.get_year())  # Output: 2021


# In[ ]:




