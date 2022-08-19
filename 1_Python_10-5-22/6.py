sum=0
n=int(input("Enter How many times? "))
y=input("Enter the num: ")
for i in range(1,n+1):
    sum+=int(y*i)
    if i==n:
        break
    print(y*i,end=' + ')
print(y*n," = ",sum)
