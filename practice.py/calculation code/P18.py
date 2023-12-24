#WAP to accept the year in 4-digits and check the leap year or not
#Using Nested if condition
year=int(input('Enter the year in 4-digits format'))
if year%100==0:
    if year%400==0:
        print('Entered year is a leap year')
else:
    print('Entered year is not a leap year')