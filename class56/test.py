class Employee:
    increment = 5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees +=1

    def increase_salary(self):
        # self.salary = self.salary*Employee.increment
        self.salary = self.salary*self.increment

    @classmethod
    def change_increment(cls, amount):
        cls.increment=amount


abhilasha = Employee("abhilasha", "gehi", 10000000)
print(Employee.no_of_employees)
rohan = Employee("rohan","kapoor",145256)

# print(abhilasha.fname)
# print(rohan.fname)
# print(abhilasha.salary)
# abhilasha.increase_salary()
# print(abhilasha.salary)

# Employee.change_increment(2)
# abhilasha.increase_salary()
# print(abhilasha.salary)
print(Employee.no_of_employees)














# class Employee:
#     increment = 5

#     def __init__(self, fname, lname, salary, increment):
#         self.fname = fname
#         self.lname = lname
#         self.salary = salary
#         self.increment = increment

#     def increase_salary(self):
#         # self.salary = self.salary*Employee.increment
#         self.salary = self.salary*self.increment


# abhilasha = Employee("abhilasha", "gehi", 10000000, 2)
# # rohan = Employee("rohan","kapoor",145256)

# # print(abhilasha.fname)
# # print(rohan.fname)
# print(abhilasha.salary)
# abhilasha.increase_salary()
# print(abhilasha.salary)
