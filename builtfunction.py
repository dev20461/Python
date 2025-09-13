# function are used to reuse the same logic often in whole program

# using function we are following DRY (Do not repeat yourself)  principal

# print function is used to log the output

print("hey")


# input function is used to take input from user

# input("enter something")



# to check length we are using len 

word = "python"

print("length od the word",len(word))


number=[3,9,7,2,1,8,6,5]

print("sorted number are in ascending order",sorted(number))


# descending order

print("reversed",sorted(number,reverse=True))


# # sum method used to perform addition

# num7=80

# num8=90

# # result =  sum(num7+num8)

# print("total of two  number",result)


# type 

greet="hey"

print("type of greet",type(greet))


num=20

print("type of num",type(num))


# type casting used for convert data to other data type


# int() convert to decimal number

num="80"

print("type of num",type(num))


newNum = int(num)


print("type of num",type(newNum))


# integer to  float


num=40

print("type of num",type(num))



decimalNum = float(20)

print("type of decimalNum",type(decimalNum))



scores = [80,50,20,40,7,10,90,60]

print("max scores",max(scores))


# minimum find the minimum value

print("minimum scores",min(scores))






# range (start,end,step) , end is exclusive will not count 

# for i in range(1,5):
#     print(i)







# deep copy (by value )


e=7

e=f

print(a)

print(b)

e=20

print(f)



# shallow copy  (by reference)


number7= [2,4,8,74,7,9]

# print(number7)

number8=number4

number9[5]=3

print(number7)