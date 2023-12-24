#WAP to accept a number and check for prime number or not.
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1,1):
    if n%i==0:
        sum=sum+1
if sum==2:
    print("It is a Prime number")
else:
    print("It is not a prime number")