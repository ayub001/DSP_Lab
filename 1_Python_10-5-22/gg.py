import re

a=open("file.txt")

b=re.findall("(born [0-3]?[0-9] [A-Z][a-z][a-z]+ [0-9][0-9][0-9][0-9])|([A-Z][a-z][a-z]+ [0-3][0-9], [0-9][0-9][0-9][0-9])|([0-3]?[0-9] [A-Z][a-z][a-z]+ [0-9][0-9][0-9][0-9])",a.read())

t=b[0]
print(t)
for i in t:
    if(i!=''):
        print(i)
