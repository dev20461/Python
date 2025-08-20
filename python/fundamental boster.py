

import datetime

print("welcome to the Interactive personal data collector!")

name=input("please Enter your name:\n")

age=int(input("please Enter your age:\n"))

height=float(input("please (Enter your in meters:\n"))

favouritenumber=int(input("please Enter your favouritenumber:\n"))

print("thank you! Here is the information we collected:\n")

print(f"name:{name},type:{name},memory address :{id(name)}")

print(f"age:{age}){type}:{age},memory address :{id(age)}")

print(f"height:{height}{type}:{height},memory address  :{id(height)}")

print(f"Faourite:{favouritenumber}){type}:{favouritenumber},memory address  :{id(favouritenumber)}")

currentyear=  datetime.datetime.now().year

userAge=currentyear-age

print(f" your birth is approximately:{userAge},(based on your {age}")

print(f"thank you for using the personal Data collector. Goodbye!" )

