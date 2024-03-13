#store the words in a python dictionary
dict = {
    "table" : ["a piece of furniture", "list of facts and figures"],
    "cat" : "a small animal"
}

print(dict)

#sets
classrooms = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(classrooms))


#adding marks in dict
marks = {}
marks.update({"Maths" : int(input("Enter Maths marks: "))})
marks.update({"Python" : int(input("Enter Python marks: "))})
marks.update({"DSA" : int(input("Enter DSA marks: "))})

print(marks)