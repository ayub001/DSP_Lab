a=open(r"file.txt")
n=int(input("Which line? "))
i=a.read(1)
if(n==0):
      print("Invalid Input!")
else:
      for j in range(n-1):
            while i!="\n" and i!='':
                  i=a.read(1)
            i=a.read(1)
      if(i=='' or i=="\n"):
            print("Line doesn't exist or Empty Line!")
      else:
            while i[len(i)-1]!="\n":
                  k=a.read(1)
                  if(k==''):
                        break
                  i=i+k
            print(i[0:len(i)-1])
