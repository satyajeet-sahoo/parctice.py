#c*9/5+32 = f - celsius to fahrenheit
print(".......menu......\nfor fahenheit press f\nfor celsius press c")
print(".................")
ch=input("Enter the character :")
if ch in 'fF' :
     cles = float(input("Enter temperature in celsius :" ))
     fahr = cles*9/5+32   
     print("temperature in fahenheit is :",fahr)
elif ch in 'cC' :
     frh = float(input("enter temperature in fahenheit :"))
     cs= (frh-32)*(5/9)
     print("temperature in celsius is :",cs)
else :
     print("invalide input")