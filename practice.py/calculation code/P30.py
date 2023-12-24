#WAP to Enter mark to get status of your division
m=int(input("Enter your marks :"))
if(m>=90):
    print("You have Passed with First Class Distinction")
else:
    if(m>=60):
        print("You have passed with Second Class Distinction")
    else:
        if(m>=35):
            print("You have just passed work hard next time")
        else:
            print("Failed")