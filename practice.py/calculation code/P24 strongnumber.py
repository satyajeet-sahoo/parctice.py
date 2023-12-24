#WAP to accept a number and check whether it is a strong number or not.ex 145=1!+4!+5!
num=int(input("Enter a number:"))
sum=0
n=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    sum=sum+f
    num=num//10
if(sum==n):
    print("The number ",n,"is a strong number")
else:
    print("The number ",n," is not a strong number")
