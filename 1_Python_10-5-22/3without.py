x=int(input("Enter a Decimal Number: "))
y=x
res=''
while x!=0:
    res=res+str(x%8)
    x=x//8
print("Octal num of {} is ".format(y),res[::-1])
