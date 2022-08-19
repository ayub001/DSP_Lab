a=open("file.txt")
no_lines=0
empty_line=0
i=a.read(1)
if(i==''):
      print("Empty document.")
else:
      while i!='':
            if(i=='\n'):
                  no_lines+=1
            pre=i
            i=a.read(1)
            empty_line+=1
      if(empty_line==no_lines):
            print("{} empty lines.".format(no_lines))
      elif(pre=='\n'):
            print("{} lines.".format(no_lines))
      else:
            print("{} lines.".format(no_lines+1))
