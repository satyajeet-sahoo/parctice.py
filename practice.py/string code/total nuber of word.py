while(True):
     s = input ( 'enter the string :')
     space = 0
     for i in s:
          if i.isspace():
               space+=1
     print('total no of word is ',len(s)-space)