print("Hello World!")
num = [1,2,3,4,5]
def length(list):
    print(len(list))

length(num)

def elements(list):
    for item in list:
        print(item, end=" ")
    print('\n')

elements(num)


def factorial (n=5):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    
factorial()

def pkr_usd (pkr):
    usd = pkr * 280
    print(pkr , "PKR =" , usd , "USD")
pkr_usd(40)

def Odd_Even(num):
    if(num%2 == 0):
        print("Even")
    else:
        print("Odd")

Odd_Even(6)