n=int(input("Enter the no of elements: "))
str_list=[]
lis=[]
for i in range(0,n):
    ele=input("Enter str{}: ".format(i+1))
    str_list.append(ele)
print(str_list)

for i in range(0,n):
    if(str_list[i]=='' or str_list[i]=='None'):
        lis.append(str_list[i])
for i in range(0,len(lis)):
    str_list.remove(lis[i])
print(str_list)
