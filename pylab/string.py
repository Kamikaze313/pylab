#basic string functions
string=input("Enter a string: ")
#reverse string in for loop
for i in range(len(string)-1,-1,-1):
    print(string[i],end="")
print()
#reverse string in while loop
i=len(string)-1
while i>=0:
    print(string[i],end="")
    i-=1
print()
#reverse string in recursion
def reverse(string,i):
    if i<0:
        return
    print(string[i],end="")
    reverse(string,i-1)
reverse(string,len(string)-1)
print()
