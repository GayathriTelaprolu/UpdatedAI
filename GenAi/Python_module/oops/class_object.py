'''
#class and object
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name:{self.name}, age:{self.age}")
p_details=Person("Gayathri",23)
p2_details=Person("Gayathri",24)
p_details.display()
p2_details.display()
'''

#encapsulation
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposit(self,amount):
        if(amount>0):
            self.__balance+=amount
            print("New balance:",self.__balance)
        else:
            print("Invalid deposit amount")
    def withdraw(self,amount):
        if(0<amount<self.__balance):
            self.__balance-=amount
            print("New balance:",self.__balance)
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance
A1=BankAccount("Gayathri",1000)
print(A1.name)
A1.deposit(500)
A1.withdraw(400)
print(A1.get_balance())
'''
            
#inheitance
class Vehicles:
    def __init__(self,brand,wheels):
        self.brand=brand
        self.wheels=wheels
    def start_engine(self):
        print("the engine is started")
class Car(Vehicles):
    def __init__(self,brand,wheels,doors):
        super().__init__(brand,wheels)
        self.doors=doors
    def car_sound(self):
        print("car is moving")
class Bike(Vehicles):
    def __init__(self,brand,wheels,type):
        super().__init__(brand,wheels)
        self.type=type
    def bike_sound(self):
        print("bike is moving")
v0=Vehicles("Toyota",4)

v1=Car("Toyota",4,4)
v2=Bike("Honda",2,"sports")
v1.start_engine()
v1.car_sound()
v2.start_engine()
v2.bike_sound()

#polymorphism
class Shapes:
    
    def area(self):
        pass
class Rectangle(Shapes):
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w
class Circle(Shapes):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r**2
class Triangle(Shapes):
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def area(self):
        return 0.5*self.b*self.h
def caluclate_area(shape):
    print(f"Area of shape:{shape.area()}")
c=Circle(5)
t=Triangle(3,4)
r=Rectangle(2,3)
caluclate_area(c)
caluclate_area(t)
caluclate_area(r)

#abstraction
class CoffeeMachine:
    def __init__(self,water_level):
        self.water_level=water_level
    def make_coffee(self,coffee_type):
        if self.water_level>=10:
            print(f"Making {coffee_type} coffee")
        else:
            print("Not enough water")
        self.heat_water()
        self.grind_beans()
        self.brew_coffee()
    def heat_water(self):
        print("Heating water")
    def grind_beans(self):
        print("Grinding beans")
    def brew_coffee(self):
        print("Brewing coffee")
    def decrement_water_level(self,amount):
        self.water_level-=amount
        print(f"Water level after brewing:{self.water_level}")
    def __del__(self):
        print("Coffee machine object destroyed")
class Espresso(CoffeeMachine):
    def __init__(self,water_level,beans_level):
        super().__init__(water_level)
        self.beans_level=beans_level
    def make_coffee(self):
        if self.water_level>=10 and self.beans_level>=5:
            print("Making espresso coffee")
        else:
            print("Not enough water or beans")
c1=CoffeeMachine(10)
c1.make_coffee("espresso")
c1.decrement_water_level(5)
c2=Espresso(10,5)
c2.make_coffee()
c2.grind_beans()
c2.brew_coffee()
c2.decrement_water_level(5)


#using of constructor and destructorS
class CoffeeMachine:
    # Constructor: This is called when the CoffeeMachine object is created
    def __init__(self):
        self.water_level = 100  # Water level in percentage
        print("The coffee machine is now ready to brew! Water level is full.")

    # Method to make coffee
    def make_coffee(self, coffee_type):
        if self.water_level <= 0:
            return "Please refill water!"
        print(f"Making your {coffee_type}...")
        self.water_level -= 20  # Decrease water level
        print(f"{coffee_type} is ready! Water level is now {self.water_level}%.")

    # Destructor: This is called when the CoffeeMachine object is no longer needed
    def __del__(self):
        print("The coffee machine is now turned off. Cleaning up...")

# Using the Coffee Machine (Constructor is called here)
my_machine = CoffeeMachine()  # Outputs: "The coffee machine is now ready to brew!"

# Making coffee (calling the make_coffee method)
my_machine.make_coffee("Espresso")  # Outputs: "Making your Espresso..." and "Espresso is ready!"
my_machine.make_coffee("Latte")     # Outputs: "Making your Latte..." and "Latte is ready!"

# Once done with the machine (Destructor is called here when the object is deleted)
del my_machine  # Outputs: "The coffee machine is now turned off. Cleaning up..."

import sys
class Person:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=int(age)
        self.__salary=float(salary)
    def check_salary(self):
        if self.__salary<0:
            print("salary is not valid")
        else:
            print("salary is valid")
if len(sys.argv) < 4:
    print("Usage: python class_object.py <arg1> <arg2> <arg3>")
    sys.exit(1)
p1=Person(sys.argv[1],sys.argv[2],sys.argv[3])
#print(p1.self.__salary)
print(p1.name)
p1.check_salary()
'''

    

        

        
