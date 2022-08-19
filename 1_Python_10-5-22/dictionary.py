Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

d={}
print(d)
{}

d.type(d)
type(d)
<class 'dict'>

d={"Name":"royal","id":100}
print(d)
{'Name': 'royal', 'id': 100}

d=dict([(1,2),(3,4)])
print(d)
{1: 2, 3: 4}

type(d)
<class 'dict'>
len(d)
2

d["id"]=1
print(d)
{1: 2, 3: 4, 'id': 1}

d["contact"]=9876554
print(d)
{1: 2, 3: 4, 'id': 1, 'contact': 9876554}

del(d['id'])
print(d)
{1: 2, 3: 4, 'contact': 9876554}

d.pop("contact")
9876554
print(d)
{1: 2, 3: 4}

d.keys()
dict_keys([1, 3])

d.values()
dict_values([2, 4])

d.items()
dict_items([(1, 2), (3, 4)])

print(d[1])
2

d.get(d[1])
print(d)
{1: 2, 3: 4}


