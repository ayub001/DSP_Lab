a=open("file.txt")
count=0
while(1):
    k=a.read(1)
    if(k==' '):
        count+=1
    elif(k!=''):
        continue
    else:
        break
print(count,"Space(s)")
