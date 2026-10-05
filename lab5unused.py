'''
#1
x=int(input("Give First Number:"))
y=int(input("Give Second Number:"))
n=int(input("Give Third Number(N):"))
for i in range(x+1,y+1):
    if i%n==0:
        print(i)


#2
n=int(input("Give A Positive Integer:"))
sum=0
i=1
while n!=0:
    y=n%10
    n=n//10
    i+=1
    sum+=y
print(sum)


#3
N=int(input("Give A Positive Integer:"))
i=0
n=0
c=0
d=0
e=0
while n!=-999:
    n=int(input("Give A Integer:"))
    if n%N==0:
        c+=1
    elif n==-999:
        e+=1
    else:
        d+=1
    i+=1
print("No. Divisible By N:",c)
print("No. Not Divisible By N:",d)


#4
n=int(input("Give A positive Integer:"))
multiply=1
for i in range(1,n+1):
    multiply*=i
print(multiply)


#5
n=int(input("Give A Positive Integer:"))
rev=0
v=n
while n>0:
    digit=n%10
    rev=rev*10 + digit
    n=n//10
print(rev)

if rev==v:
    print("Pallindrome")
else:
    print("Not A Pallindrome")


#6
n=int(input("Give Positive Number For Fibonacci Series:"))
a=1
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c
'''

#7
n=int(input("Give Integer No.:"))
if n<=1:
    print("Invalid.")
else:
    f=0
    for i in range(2,n):
        if n%i==0:
            f=1
            break
if f==0:
    print("Prime.")
else:
    print("Not Prime.")











