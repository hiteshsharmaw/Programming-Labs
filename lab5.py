#ques1
'''
x=int(input('Enter the first number:'))
y=int(input('Enter the second number:'))
n=int(input('Enter the third number n to divide with:'))
sum=0
for i in range(x,y):
    if i%n==0:
        print(i, end=" ")
        sum+=1
print('The count of numbers dividible is :',sum)
'''

#ques2
'''
n=int(input('Enter the number:'))
mul=1
while n!=0:
    mul=mul*(n%10)
    n=n//10
print(mul)
    '''

#ques3
'''
n=int(input('Enter the limit:'))
x=0
lar=0
sml=0
while x!=-999:
    x=int(input('Enter the bill amt:'))
    if x>n:
        lar+=1
    elif x==-999:
        print()
    else:
        sml+=1
print('Total large bills:',lar)
print('Total small bills:',sml)
'''

#ques4
'''
n=int(input('Enter a first positive integer:'))
p=int(input('Enter a second positive integer:'))
r=1
i=1
power=0
while i!=p+1:
    r=n*r
    i=i+1
print(r)
'''
#ques5
'''
n=int(input('Enter a positive integer:'))
m=int(input('Enter second positive integer:'))
v=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if rev==m:
    print('Yes both the numbers are reverse of each other.')
else:
    print('No both the numbers are not reverse of each other.')
'''

#ques6
'''
n=int(input('Enter the power:'))
for i in range(n+1):
    print(2*i ,' ' ,end='')
    '''
    
#ques7
'''
n=int(input('Enter the integer:'))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print('Its a perfect number.')
else:
    print('Not a perfect number.')
'''

#ques8
'''
n=int(input('Enter the number of times to print star pattern:'))
for i in range(n+1):
    print('*'*i)
   ''' 
#ques9
'''
n=int(input('Enter a integer:'))
d=int(input('Pick a digit from 0 to 9:'))
sum=0
while n!=0:
    x=n%10
    n=n//10
    if x==d:
        sum+=1
print('No of times d appeared in n:',sum)
'''

#ques10
n=int(input('Enter a positive integer:'))
sum=0
for i in range(1,n+1):
    if n%i==0:
        print(i)
        sum+=1
print('The count of divisors is :',sum)