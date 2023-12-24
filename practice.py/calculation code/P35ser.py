#WAP to print the series 1 4 9 16 .....n
n=int(input("Enter the number: "))
print("The  series is :")
for i in range(1,n+1,1):
    s=i**2
    print(s,end=' ,')