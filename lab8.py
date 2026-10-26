'''
#ques1
s=input()
vowels='aeiouAEIOU'
main='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
v=0
c=0
d=0
sp=0
o=0
for i in s:
    if i in vowels:
        v+=1
    elif i in main:
        c+=1
    elif i in '0123456789':
        d+=1
    elif i==' ':
        sp+=1
    else:
        o+=1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('Spaces:',sp)
print('Others:',o)
'''
'''
#ques2
s=input()
mnew=''
for i in range(len(s)):
    if i%2==0:
        mnew+=s[i].upper()
    else:
        mnew+=s[i].lower()
print(mnew)
'''
'''
#ques3
s=input()
main='abcdefghijklmnopqrstuvwxyz'
main1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
main2='0123456789'
l=0
u=0
d=0
sp=0
for i in s:
    if i in main:
        l=1
    elif i in main1:
        u=1
    elif i in main2:
        d=1
    elif i!=' ':
        sp=1
t=l+u+d+sp
if len(s)<8:
    print('WEAK')
elif t==4:
    print('STRONG')
elif t==2 or t==3:
    print('MODERATE')
else:
    print('WEAK')
'''
'''
#ques4
s=input()
k=input()
count=0
snew=''
for i in range(len(s)):
    if s[i]==k:
        count+=1
    snew+=str(i)+' '
print('Count:',count)
if count==0:
    print('Positions: -1')
else:
    print('Positions:',mnew)
'''
'''
#ques5
s=input()+' '
count=0

for i in s:
    if i!=' ':
        count+=1
    elif count>0:
        print(count,end=' ')
        count=0
'''
'''
#ques6
s=input()

if len(s)==10 and s[0:2]=='RJ':
    print(True)
else:
    print(False)
'''
'''
#ques7
s=input()
rev=''
count=0

for i in s:
    rev=i+rev

for i in range(len(s)//2):
    if s[i]!=rev[i]:
        count+=1

print('Changes needed:',count)
'''
'''
#ques8
s=input()
snew=''
for i in s:
    if i not in snew:
        snew+=i
    else:
        continue
print(snew)
'''
'''
#ques9
s=(input()).lower()
key=int(input())
new_s=''
a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in s:
    a.index(i)
    new_s+=a[(a.index(i)+key)%26]
print(new_s)
'''
'''
#ques10
s=input()
count=1
m=1
mnew=s[0]
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        count=1
    if count>m:
        m=count
        mnew=s[i]
print(mnew,m)
'''













































































































































































































































