a=input("Enter a binary String: ")
pr_st=0
for i in a:
    if(pr_st==0 and i=='1'):
        pr_st=1
    elif(pr_st==1 and i=='0'):
        pr_st=0
    elif(pr_st==1 and i=='1'):
        pr_st=2
    elif(pr_st==2 and i=='0'):
        pr_st=3
    elif(pr_st==3 and i=='0'):
        pr_st=4
    elif(pr_st==3 and i=='1'):
        pr_st=5
    elif(pr_st==4 and i=='1'):
        pr_st=2
    elif(pr_st==5 and i=='0'):
        pr_st=3
    elif(pr_st==5 and i=='1'):
        pr_st=2
    else:
        continue

if(pr_st==5):
    print("YES:)")
else:
    print("No!")
