lis1=[]
n=int(input("\nEnter no elements: "))
for i in range(0,n):
    ele=int(input("Enter ele{}".format(i+1)))
    lis1.append(ele)
    
lis2=[]
n=int(input("\nEnter no elements: "))
for i in range(0,n):
    ele=int(input("Enter ele{}".format(i+1)))
    lis2.append(ele)

print("\n")
for i in range(0,len(lis1)):
        print(lis1[i],lis2[-i-1])
