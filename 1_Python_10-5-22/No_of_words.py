a=open(r"file.txt")
no_words=0
pre=i=a.read(1)
while i!='':
      if(i==' ' or i=='\n'):
            if(pre!=' ' and pre!='\n'):
                  no_words+=1
      pre=i
      i=a.read(1)
if(pre!=' ' and pre!='\n'):
      no_words+=1
print(no_words,"word(s)")
