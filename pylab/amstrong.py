#check if a number is amstrong or not
num=int(input("Enter a number: "))
sum=0
temp=num
count=0
while temp>0:
    temp//=10
    count+=1
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**count
    temp//=10
if sum==num:
    print("The number is amstrong.")
else:
    print("The number is not amstrong.")
