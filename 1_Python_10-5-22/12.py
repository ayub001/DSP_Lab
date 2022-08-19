str=input("Enter the String: ")
char=0
digits=0
symbols=0
for i in range(0,len(str)):
    if(str[i].isalpha()):
        char+=1
    elif(str[i].isdigit()):
        digits+=1
    else:
        symbols+=1

print("Char = ",char)
print("Digits = ",digits)
print("Symbols = ",symbols)
