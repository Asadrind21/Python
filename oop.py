class Students:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(self.name, ", your average marks are", sum/3)

s1 = Students("Asad", [20,10,30])

s1.average()

class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited from your account.")
        print("Remaining balance is:", self.balance)
    
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited into your account.")
        print("Remaining balance is:", self.balance)
    
acc1 = Account(1000, 1234)
print(acc1.balance)
print(acc1.acc_no)
acc1.debit(500)
acc1.credit(500)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(10)
print(c1.radius)
print(c1.area())
print(c1.perimeter())

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role:", self.role, "Dept:", self.dept, "Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "60000")

e1 = Employee("Engineer", "Electrical", "50000")
e1.showDetails()
e2 = Engineer("Jack", 30)
e2.showDetails()

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, o2):
        return self.price > o2.price

o1 = Order("Pencil", 10)
o2 = Order("Chips", 20)
print(o2.price > o1.price)