count = 1
while count <= 5:
    print("Hello")
    count+=1
print(count)

i = 1
while i <=100:
    print(i)
    i += 1
    
j = 100
while j >=1:
    print(j)
    j -= 1

n = 1
while n <= 10:
    print(2*n)
    n += 1

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 0
while x < len(list):
    print(list[x])
    x += 1

tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
y = 0
z = int(input("Enter the number you want to search:"))
while y < len(list):
    if (z == tuple[y]):
        print("Found at index", y)
        break
    y += 1

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for x in list:
    print(x)

tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 16)
z = 16
index = 0
for y in tuple:
    if ( y == z ):
        print("number found at index", index)
    index += 1

for i in range(1, 101):
    print(i)

for i in range(100, 0, -1):
    print(i)

for i in range(11):
    print(2*i)

#sum of first n numbers
n=1
sum=0
while n<=5:
    sum = sum + n
    print(sum)
    n += 1

#factorial of first n numbers
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
    print(fact)