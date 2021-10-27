"""
multilevel inheritance :- Multilevel inheritance we deive a child at different level
                        for example derive a child class by parent class and again derive a child class making child class as parent class.
"""


# example of multilevel inheritance
class Board:  # grand Parent class
    def board_detail(self):  # instance method of grand parent child
        print("this is cbse board")


class Collage(Board):  # parent class derive a class by using board as a parent class
    collage_name = "RIMT University"

    def collage_detail(self):  # instance method of Collage class
        super().board_detail()  # calling method of paret class
        print(self.collage_name, " is not affliated with cbse board ")


class School(Collage):  # derive a class using Collage as a parent class
    school_name = "high school "

    def school_detail(self):  # instance method of School class
        super().collage_detail()
        print(self.school_name, " is  affiliated with cbse board")


school = School()
school.school_detail()
