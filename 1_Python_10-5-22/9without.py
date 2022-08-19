str1=input("Enter the string: ")
splt=input("Enter the split char: ")
str1=str1+splt
mem=-1
print("\nDisplaying each substring\n")
for i in range(0,len(str1)):
    if(str1[i]==splt):
        print(str1[mem+1:i])
        mem=i
