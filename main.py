#
# class Student:
#     amount_of_students = 0
#
#
#     def __init__(self, name, age, height = 160):
#         self.name = name
#         self.age = age
#         self.height = height
#         Student.amount_of_students += 1
#
#     def happy_birthday(self):
#         print("Greetings! you have HB")
#         self.age += 100
#
#
#     def __str__(self):
#         return f"<Student age={self.age} height={self.height}>"
#
#
# s1 = Student("Alex",28, 180)
# s1.happy_birthday()
# print(s1)
#
# s2 = Student("Bob",18)
# print(s2)
#
# s3 = Student("Jane",17, 150)
# print(s3)
#
# print("Amount", Student.amount_of_students)
#
#
# class Circle:
#
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calc_area(self):
#         return 3.14 * (self.radius ** 2)
#
#
#
# circle_10 =Circle(10)
# print(circle_10.calc_area())
#
# circle_3 =Circle(3)
# print(circle_3.calc_area())


import  random

class Student:


    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("time to study")
        self.progress += 0.12
        self.gladness -= 3


    def to_sleep(self):
        print("time to sleep")
        self.gladness += 3


    def to_chill(self):
        print("time to relax")
        self.gladness += 5
        self.progress -= 0.05

    def is_alive(self):
        if self.progress < -0.5:
            print("Too lazy...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Genius! passed!")
            self.alive = False

    def end_of_day(self):
        print(
            f"gladness - {self.gladness}\n"
            f"progress - {round(self.progress, 2)}"
        )

    def live(self, day):
        print(
            f"Day #{day} of {self.name} life"
        )
        magic = random.randint(1, 3)
        if magic == 1:
            self.to_study()
        elif magic == 2:
            self.to_sleep()
        elif magic == 3:
            self.to_chill()

        self.end_of_day()
        self.is_alive()


bob = Student("bob")
for day in range (365):
    if bob.alive == False:
        break
    bob.live(day)