def calculation(a,b):
    summ=a+b
    sub=a-b
    return summ,sub

a=int(input("Enter num1: "))
b=int(input("Enter num2: "))

a,b=calculation(a,b)
print(a,',',b)
