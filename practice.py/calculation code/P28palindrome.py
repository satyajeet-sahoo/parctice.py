n=int(input("Enter a number :"))
x=n
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(x==rev):
    print(rev," is a Palindrome")
else:
    print(rev," is Not a palindrome")