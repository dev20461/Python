

marks = int(input("please enter your marks to check grades\n"))

if(marks>=70):
    print("you have achieved A grade")

elif(marks>=66):
    print("you have achieved B grade")

elif(marks>=55):
    print("you have achieved C grade")

elif (marks>35):
    print("you have achieved D grade")

elif(marks>=28):
    print("you have passed this exam with F grade")

else:
    print("you have failed this exam")    
    