#rearrange a string in ascii order using any built in functions
string=input("enter a string: ")
string=sorted(string)
print(string)
#rearrange a string without using any built in functions
string=list(string)
for i in range(len(string)):
    for j in range(i+1,len(string)):
        if ord(string[i])>ord(string[j]):
            temp=string[i]
            string[i]=string[j]
            string[j]=temp
string="".join(string)
print(string)
#rearrange a string in alphabetical order without using sort() or ord()
string=list(string)
siz=0
while string[siz]!=" ":
    siz+=1
for i in range(siz):
    for j in range(i+1,len(string)):
        if string[i]>string[j]:
            temp=string[i]
            string[i]=string[j]
            string[j]=temp
string="".join(string)
print(string)
