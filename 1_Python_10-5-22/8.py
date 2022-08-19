str1=input("Enter the string: ")
str2=input("Enter the str which you wanna find: ")
str1=str1[::-1]
str2=str2[::-1]
l=len(str2)
flag=0

for i in range(0,len(str1)):
    if(str2 == str1[i:i+l]):
        print("The string is at {}th index position".format(len(str1)-(i+l)))
        flag=1
        break
if(flag==0):
    print("It is not found")
