#WAPP to calculate the sum of natural number
num = int(input("Enter a number: "))  
  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   # use while loop to iterate untill zero  
   while(num > 0):  
       sum += num  
       num -= 1  
   print("The sum is",sum)  