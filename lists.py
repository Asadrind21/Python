#insertion
list = []
print(list)
list.append(input("Enter the name of your fav movie: "))
list.append(input("Enter the name of your fav movie: "))
list.append(input("Enter the name of your fav movie: "))
print(list)

#Palindrome
palindrome = [1,2,3,2,1]
palindrome_copy = palindrome.copy()
palindrome_copy.reverse()
print(palindrome_copy)
if (palindrome_copy == palindrome):
    print("The list is a Palindrome")
else:
    print("Not palindrome")
