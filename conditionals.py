# Finding odd or even
num = int(input("Enter a number:"))
if ((num % 2) == 0):
    print("The number is EVEN")
else:
    print("The number is ODD")

#Greater of Three numbers
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
num3 = int(input("Enter num3:"))

if (num1 >= num2 and num1 >= num3):
    print("Num1 is the greatest.")
elif (num2 >= num1 and num2 >= num3):
    print("Num2 is the greatest.")
else:
    print("Num3 is the greatest")

#Check if number is a multiple of 7
number = int(input("Enter a number:"))
if(number%7==0):
    print("The number is a multiple of 7")
else:
    print("The number is not a multiple of 7")