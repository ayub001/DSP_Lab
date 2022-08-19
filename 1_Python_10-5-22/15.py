lis1=[]
n=int(input("\nEnter no elements: "))
for i in range(0,n):
    ele=input("Enter ele{} ".format(i+1))
    lis1.append(ele)
    
lis2=[]
n=int(input("\nEnter no elements: "))
for i in range(0,n):
    ele=input("Enter ele{} ".format(i+1))
    lis2.append(ele)

lis3=[]
for i in range(0,len(lis1)):
    for j in range(0,len(lis2)):
        lis3.append(lis1[i]+lis2[j])

print(lis3)
