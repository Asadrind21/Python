def show(n):
    if(n == 0 ):
        return
    print(n)
    show(n-1)

#show(5)

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)

print(fact(5))

def sum(n):
    if (n == 0):
        return 0
    return sum(n - 1) + n
print(sum(4))

alphabets = ['a', 'b', 'c', 'd', 'e']

def print_list(list, i=0):
    if (i == len(list)):
        return 
    print(list[i])
    print_list(list, i+1)

print_list(alphabets)