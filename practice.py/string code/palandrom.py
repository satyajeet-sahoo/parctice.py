str = input('enter the string : ')

# if else type
if str == str[::-1] :
     print('it is a palandrom number')
else :
     print('no it not a palandrum  number ')
 
# for loop type
s='' 
for i in str :
     s=i+s 
if str == s:
     print('yes it is palandrum')
     
