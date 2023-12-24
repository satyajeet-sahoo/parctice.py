# Write a python program to write day in month, years and days
days = int( input("Enter the numberof days : "))
d = days
yr = days // 365
days = days % 365
month = days // 30
days = days % 30
week = days // 7
days = days % 7
if days >=1 :
    print(d, "Days is ", yr , "year ,",month,"months ,",week,"weeks and",days,"days")
else :
    print(d, "Days is ", yr , "year ,",month,"months ,",week,"weeks")
