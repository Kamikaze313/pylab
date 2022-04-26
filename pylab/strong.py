def fact(digit):
    if digit==0:
        return 1
    else:
        return digit*fact(digit-1)
num=int(input("Enter a number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=fact(digit)
    temp//=10
if sum==num:
    print("The number is strong number.")
else:
    print("The number is not strong number.")

