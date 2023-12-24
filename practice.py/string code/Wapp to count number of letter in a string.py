st = input("Enter the string : ").lower()

# type 1 with out function

st1,st2,='',''
D={}
for i in st:
     if i not in st1:
          st1+=i
print(st1)
for i in st1:
     c=0
     for j in st:
          if i==j :
               c+=1
     if c==1 :
          st2+=i
     D[i]=c
print(st2)
print(D) 

# type 2 with fuction

d={} 
stx=''
for i in st:
     if st.count(i)==1 or i ==' ':
          stx+=i
     else :
          d[i]=st.count(i)

print(stx)
print(d)
