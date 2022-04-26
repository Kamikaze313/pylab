n = int(input("Enter the limit: "))
m = int(input("Enter the number: "))
li=[]
li2=[]
word=[]
for i in range(0,n):
  li.append(int(input("Enter the {0} number: ".format(i+1))))
for i in li:
  while(i>0):
    word.append(i%10)
    i//=10
  li2.append(word)
  word=[]
li=[]
ii=[]
for i in li2:
  a=0
  ii=i
  for j in i[::-1]:
    if(j==m):
      pass
    else:
      a=a*10+j
      j//=10
  if(a!=0):
    li.append(a)
print(li)