with open("practice.txt", "w") as f:
    f.write("Hi Everyone \nwe are learning file I/O \nusing Java. \nI like programming in Java.")

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w+") as f:
    f.write(new_data)


def check_for_word():
    with open("practice.txt", "r") as f:
        data = f.read()
        word = "learning"
        if (data.find(word) != -1):
            print("Word found")
        else:
            print("Word not found")

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print("Word found in", line_no)
                return
            line_no += 1
        return -1

count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    print(nums)
    
    for val in nums:
        if (int(val) % 2 == 0):
            count += 1
    
print(count)