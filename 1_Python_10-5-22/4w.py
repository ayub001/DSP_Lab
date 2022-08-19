n=int(input("Enter no of elements: "))
lis=[]
for i in range(0,n):
    ele=input("Enter elemenet{}:".format(i+1))
    lis.append(ele)
i=0
while i<n:
    print(lis[i])
    i+=2
