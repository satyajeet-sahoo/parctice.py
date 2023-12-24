st1 = input('enter the first string : ')
st2 = input('enter the second string : ')

for i in range (0,len(st2)):
    c=0
    for j in range (0,len(st1)):
           if st2[i]==st1[j] :
               c+=1
    if c>0:
        print(st2[i],"is",c,"time")
