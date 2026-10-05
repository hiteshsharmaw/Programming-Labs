#ques1
'''
print('     ',end=" ")
for i in range(1,10):
    print(f'{i:4}',end='  ')
print('-'*60)
print()

for j in range(1,10): 
    print(j,'|',end='   ')
    for i in range(1,10):
        print(f'{i+j:3}',end='   ')
    print()
''' 
    
#ques2
'''
n=int(input())
i=0
while i!=1001:
    if i%n==0 and i%4!=0:
        print(i, end=' ')
    i=i+1
'''
'''
#ques3a
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end=' ')
        j=j+1
    print()
    i=i+1
'''
#ques3b
'''
n=int(input())
i=n
while i>0:
    j=1
    while i>=j:
        print('*',end=" ")         
        j=j+1
    print()
    i=i-1
'''
#ques3c
'''
n=int(input())
i=1
while i<=n:
    j=1
    while i>=j:
        print('*',end=" ")         
        j=j+1
    print()
    i=i+1
'''

#ques4
'''
n=int(input())
octalnum=''
while n>0:
    digit=n%8
    octalnum=str(digit)+octalnum
    n=n//8
print(octalnum)
'''

#ques5
'''
n=int(input('Enter the total data frequency:'))
data=int(input())
largest=data
for i in range(n-1):
    data=int(input())
    if data>largest:
        seclarge=largest
        largest=data
print()
print(largest)
print(seclarge)
'''       
    
#ques6 
'''   
n=int(input())
for i in range(1,n+1):
    sum=0
    digit=i
    for j in range(i):
        sum+=(digit%10)**len(str(i))
        digit=digit//10
    if sum==i:
        print(i)
'''

#ques7
'''
print(f"{'N':<5}{'N^2':<7}{'N^3':<8}{'Square Root':<10}")

for i in range(1,16):
    print(f"{i:<5}{i**2:<7}{i**3:<8}{i**(1/2):.4f}")
'''   

#ques8
'''
n=int(input())
for i in range(1,n+1):
    print(' '*(n+1-i),end='')
    for j in range(i):
        print(i,end=' ')
    print()
'''

#ques9
'''
n=int(input())
sum=1
for i in range(1,n+1):
    for j in range(i):
        print(sum,end=' ')
        sum+=1
    print()
'''

#ques10

n=int(input())
for i in range(1,((n+1)//2)+1):
    print(' '*(n+1-i),end='')
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(((n+1)//2)-1,0,-1):
    print(' '*(n+1-i),end='')
    for j in range(i):
        print('*',end=' ')
    print()
        










































