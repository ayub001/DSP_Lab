n=input("Number                    : ")
b1=int(input("Base of Number            : "))
b2=int(input("0-if r's, 1-if (r-1)'s    : "))

def d_any(num,b1):
    y=int(num)
    res=''
    while y!=0:
        rem=y%b1
        if(rem<10):
            res=res + str(rem)
        elif(rem==10):
            res=res + 'A'
        elif(rem==11):
            res=res + 'B'
        elif(rem==12):
            res=res + 'C'
        elif(rem==13):
            res=res + 'D'
        elif(rem==14):
            res=res + 'E'
        elif(rem==15):
            res=res + 'F'
        y=y//b1
    return res[::-1]

def binhex_d(num,b1):
    d=0
    j=len(num)-1
    for i in num:
        if(i=='A'):
            ld=10
        elif(i=='B'):
            ld=11
        elif(i=='C'):
            ld=12
        elif(i=='D'):
            ld=13
        elif(i=='E'):
            ld=14
        elif(i=='F'):
            ld=15
        else:
            ld=int(i)
        d=d+(ld*(b1**j))
        j-=1
    return d

if(b2==0):
    print("r's complement of",n,"is  :",d_any((b1**len(n))-binhex_d(n,b1),b1))
elif(b2==1):
    print("r's complement of",n,"is  :",d_any(((b1**len(n))-1)-binhex_d(n,b1),b1))
else:
    print("Inalid Input!")
