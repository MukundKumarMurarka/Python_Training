"""
Inheritance :- Derive a new class from exixting class.
               the class from which a class is derived is known as parent class, and class the which is derived
               we can use all the variables and method of parent class in the chil class but the viceversa is not true
                if we declare init method in parent class and child class both and creating the objects of child class
                then it will first check that init method is in the child class or not if it is availablr then object
                will call thw init method of child class. if there is no any init method in child class then object will
                call init method of parent class.

"""


# ecample without init method
class Vehical:
    wheel_car = 4
    milage_car = 20

    def car_detail(self):  # instance method
        print("the car has ", Vehical.wheel_car, " wheel and gives milage of ", Vehical.milage_car, " km")


class Bike(Vehical):  # bike is derived class and vehical is parent class
    wheel_bike = 2
    milage_bike = 50

    def bike_detail(self):  # instance method of child class
        print("the bike has ", Bike.wheel_bike, " wheel and gives milage of ", Bike.milage_bike, " km")


car = Vehical()  # creating object of parent class
bike1 = Bike()  # creating objects of child class
car.car_detail()  # calling instance method of parent class
bike1.car_detail()  # Calling instance method of parent class by object of child class
bike1.bike_detail()  # calling instance method of child class by objects of child class


# inheritance example using constructor in parent class and child class both
class Phone:
    def __init__(self, cost, ram, os):
        self.cost = cost
        self.ram = ram
        self.os = os
        print("this is phone class")

    def phone_detail(self):
        print(self.cost, " ", self.ram, " ", self.os)


class iphone(Phone):
    def __init__(self, cost_iphone, ram_iphone, os_iphone):
        self.cost_iphone = cost_iphone
        self.ram_iphone = ram_iphone
        self.os_iphone = os_iphone
        print("this is iphone class")

    def iphone_detail(self):
        print(self.cost_iphone, " ", self.ram_iphone ," ", self.os_iphone)


phone1 = Phone(10000, 8, "android")
iphone1 = iphone(20000, 4, "ios")

iphone1.iphone_detail()

phone1.phone_detail()
