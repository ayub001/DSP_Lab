s1=input("Enter STR1: ")
s2=input("Enter STR2: ")
s3=''
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
    s3=s3+s1[i]+s2[-(i+1)]
if(k==0):
    print("The resultant str is: ",s3)
elif(k==1):
    print(s3+s1[flag:len(s1)])
else:
    #print(s3+s2[len(s2)-flag-1::-1])
    print(s3+s2[-(flag+1):-len(s2)-1:-1])
