
# Collection of key-value pairs.

student = {"name":"alice","age":20}


# access

print(student["name"])

print(student.get("age"))

# add property

student["grade"]="A"

print(student)

# update 

student["age"] = 25

print(student)

student.update({"age":"21"})

print(student)


# remove

student.pop("grade")

print(student)

del student["age"]
print(student)

# student.clear()
print(student)


print(student.keys())

print(student.values())

print(student.items())