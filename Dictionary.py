
# key value pair 


student = {"name":"dev","age":17}


# access

print(student["name"])


print(student.get("age"))


# add

print(student)

student["grade"] = "B"

print(student)


# update

student["grade"] = "c"

print(student)


student.update({"age":45})


print(student)

# delete


del student["grade"]

print(student)


# student.clear()

# print(student)


# 

print(student.keys())

print(student.values())

print(student.items())