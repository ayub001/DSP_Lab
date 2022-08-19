s1=[]
no_ele = int(input("Enter the no of ele: "))
for i in range(0,no_ele):
    ele=input("Enter the element{}".format(i+1))
    s1.append(ele)
s2=[]
no_ele = int(input("\nEnter the no of ele: "))
for i in range(0,no_ele):
    ele=input("Enter the element{}".format(i+1))
    s2.append(ele)
s3=[]
if(len(s1)>len(s2)):
    flag=len(s2)
    k=1
elif(len(s1)==len(s2)):
    flag=len(s1)
    k=0
else:
    flag=len(s1)
    k=2
for i in range(0,flag):
    s3.append(s1[i]+s2[i])
    
if(k==1):
    for i in range(flag,len(s1)):
        s3.append(s1[i])
elif(k==2):
    for i in range(flag,len(s2)):
        s3.append(s2[i])

print("\nThe resultant str is: ",s3)
