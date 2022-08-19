#print(lis[::2])
n=int(input("Enter no of Elements: "))
lis=[]
for i in range(n):
    ele=input("Enter element{}: ".format(i+1))
    lis.append(ele)
for i in range(0,n,2):
    print(lis[i])
