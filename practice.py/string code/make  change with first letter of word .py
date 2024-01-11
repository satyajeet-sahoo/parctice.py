st = input('Enter the string : ')
st2=st.split(" ")
for i in range(len(st2)) :
     if st2[i].startswith("o") or st2[i].startswith('O'):#can put any starting letter of word which u want to revers in a paragraph 
          st2[i]=st2[i][::-1]
          print(st2[i],end=' ')
     else :
          print(st2[i],end=' ')
     
