

# def functionName (parameter):
#     return

# optional: parameter and return value in function




# example 

def greet():
    print("hey")


greet()    


# with parameter 


def add(a,b):
    print(a+b)


add(15,20)


# with return value

def square(num):
    return num*num


result = square(6)

print(result)


# with default parameter


def createAccount(name,amount=1000):
    print("account created of ",name, "and total balance ",amount)



createAccount("dev")


createAccount("akshat",2000)