n=input("Number             : ")
b1=int(input("Base of Number     : "))
b2=int(input("Base of Result Num : "))

def d_any(num,b2):
    y=int(num)
    res=''
    while y!=0:
        rem=y%b2
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
        elif(rem==16):
            res=res + 'G'
        elif(rem==17):
            res=res + 'H'
        elif(rem==18):
            res=res + 'I'
        elif(rem==19):
            res=res + 'J'
        elif(rem==20):
            res=res + 'K'
        elif(rem==21):
            res=res + 'L'
        elif(rem==22):
            res=res + 'M'
        elif(rem==23):
            res=res + 'N'
        elif(rem==24):
            res=res + 'O'
        elif(rem==25):
            res=res + 'P'
        elif(rem==26):
            res=res + 'Q'
        elif(rem==27):
            res=res + 'R'
        elif(rem==28):
            res=res + 'S'
        elif(rem==29):
            res=res + 'T'
        elif(rem==30):
            res=res + 'U'
        elif(rem==31):
            res=res + 'V'
        elif(rem==32):
            res=res + 'W'
        elif(rem==33):
            res=res + 'X'
        elif(rem==34):
            res=res + 'Y'
        elif(rem==35):
            res=res + 'Z'
        y=y//b2
    print("Converted Number   :",res[::-1],"of base-{}".format(b2))
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
        elif(i=='G'):
            ld=16
        elif(i=='H'):
            ld=17
        elif(i=='I'):
            ld=18
        elif(i=='J'):
            ld=19
        elif(i=='K'):
            ld=20
        elif(i=='L'):
            ld=21
        elif(i=='M'):
            ld=22
        elif(i=='N'):
            ld=23
        elif(i=='O'):
            ld=24
        elif(i=='P'):
            ld=25
        elif(i=='Q'):
            ld=26
        elif(i=='R'):
            ld=27
        elif(i=='S'):
            ld=28
        elif(i=='T'):
            ld=29
        elif(i=='U'):
            ld=30
        elif(i=='V'):
            ld=31
        elif(i=='W'):
            ld=32
        elif(i=='X'):
            ld=33
        elif(i=='Y'):
            ld=34
        elif(i=='Z'):
            ld=35
        else:
            ld=int(i)
        d=d+(ld*(b1**j))
        j-=1
    return d

decimal=binhex_d(n,b1)
d_any(decimal,b2)
