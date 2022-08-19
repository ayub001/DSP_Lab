s1=input("Enter s1: ")
s2=input("Enter s2: ")
flag=0
for i in s1:
    if i in s2:
        continue
    else:
        print("False")
        flag=1
        break
if(flag==0):
    print("True")
