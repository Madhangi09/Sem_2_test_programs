#1fibonacci
n=int(input())
num1=0
num2=1
next_number=num2
count=1
while count<=n:
    print(next_number,end=" ")
    count+=1
    num1, num2=num2, next_number
    next_number=num1+num2
print()

#2odd or even
n=int(input("Enter the number of Elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the element:")))
odd=0
even=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("The number of odd numbers:",odd)
print("The number of even numbers:",even)
