def re_fun(n):
    if(n<=1):
        return 1
    else:
        return n + re_fun(n-1)

print(re_fun(10))
