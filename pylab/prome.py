#prime factors of a number using flag and for loops
from re import I


num=int(input("Enter a number: "))
for i in range(2,num):
    if num%i==0:
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
        if flag==0:
            print(i)
