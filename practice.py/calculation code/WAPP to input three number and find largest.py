#to find largest number using nasted if else
a = int(input ("Enter first number :"))
b = int(input ("Enter second number :"))
c = int(input ("Enter third number :"))
if(a > b) :
     if a>c :
          print(a,"is larger than ",b,c)
     else :
          print(c,"is larger than ",a,b)
else :
     print(b,"is larger than ",a,c)

