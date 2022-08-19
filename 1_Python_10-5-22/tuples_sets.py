Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================================ RESTART: Shell ================================
##Inserting elements in Tuples using list...
t=(1,2,3,4) 
x=list(t)
x[0]=100
t=tuple(x)
print(t)
(100, 2, 3, 4)

================================ RESTART: Shell ================================
s={1,2,3,4,5}
print(s)
{1, 2, 3, 4, 5}
s1={8,9,6}
s-s1
{1, 2, 3, 4, 5}
s1-s
{8, 9, 6}
s1.union(s)
{1, 2, 3, 4, 5, 6, 8, 9}
s.union(s1)
{1, 2, 3, 4, 5, 6, 8, 9}
s.intersection(s1)
set()
s1.intersection(s)
set()
s2={10,23,21,35,56}
s3={20,10,35,64,30}
s2.union(s3)
{64, 35, 10, 20, 21, 23, 56, 30}
s2.intersection(s3)
{10, 35}
s2.difference(s3)
{56, 21, 23}
s3.difference(s2)
{64, 20, 30}
