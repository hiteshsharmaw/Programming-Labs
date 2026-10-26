'''
#ques1
s=input()
rev=''
for i in s:
    rev=i+rev
print(rev)
'''

'''
#ques2-1
s=input()
rev=''
count=0
for i in s:
    rev=i+rev
for j in rev:
    if j!=' ':
        count+=1
    elif j==' ':
        break
print(count)
'''

'''
#ques2-2
s=input()
s=s+' '
count=0
for i in s:
    if i!=' ':
        count+=1
    else:
        if count>0:
            last=count
            count=0
print(last)
'''

'''
#ques3inbuilt
sentence=input()
word=input()
if word in sentence:
    print('Yes')
else:
    print('No')

print(sentence.count(word))
'''

'''
#ques3noninbuilt
sentence=input()+' '
word=input()
wnew=''
count=0
for i in sentence:
    if i!=' ':
        wnew+=i
    else:
        if wnew==word:
            count+=1
            wnew=''
        else:
            wnew=''
if count>0:
    print('Yes')
    print(count)
else:
    print('No')
'''

'''
#ques4
s=input().lower()
main='abcdefghijklmnopqrstuvwxyz'
mnew=''
for i in s:
    if i in main and i not in mnew:
        mnew+=i
if len(mnew)==len(main):
    print('Pangram')
else:
    print('Not a Pangram')
'''
'''
#ques4new
s=input().lower()
main='abcdefghijklmnopqrstuvwxyz'
count=0
for i in main:
    if i in s and i!=' ':
        count+=1
    elif i not in s :
        break

if count==len(main):
    print('Pangram')
else:
    print('Not a Pangram')
'''
'''
#ques5-1
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
#ques5-2
s=input()
shift=int(input())
main='abcdefghijklmnopqrstuvwxyz'
main2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mnew=''
for i in s:
    if i in main:
        j=main.index(i)
        mnew+=main[(j+shift)%26]
    else:
        j=main2.index(i)
        mnew+=main2[(j+shift)%26]
print(mnew)
'''
'''
#ques6
n=int(input())
s1=0
s2=0
s3=0
s4=0
s5=0
while n!=-1:
    if n==1 or n==2:
        s1+=1
    elif n==3 or n==4:
        s2+=1
    elif n==5 or n==6:
        s3+=1
    elif n==7 or n==8:
        s4+=1
    elif n==9 or n==10:
        s5+=1
    n=int(input())
t=s1+s2+s3+s4+s5
print('1-2:','#'*int(((s1/t)*100)//5),f"{(s1/t)*100:.2f}",'%')
print('3-4:','#'*int(((s2/t)*100)//5),f"{(s2/t)*100:.2f}",'%')
print('5-6:','#'*int(((s3/t)*100)//5),f"{(s3/t)*100:.2f}",'%')
print('7-8:','#'*int(((s4/t)*100)//5),f"{(s4/t)*100:.2f}",'%')
print('9-10:','#'*int(((s5/t)*100)//5),f"{(s5/t)*100:.2f}",'%')
'''
'''
#ques7
s=input()
rev=''
for i in s:
    rev=i+rev
if s==rev:
    print('Palindrome')
else:
    print('Not a Palindrome')
'''
'''
#ques8
n=int(input())
a=[]
for i in range(n):
    x=int(input())
    a.append(x)
print(a)
s=0
for i in a:
    s+=i
print(s)
p=1
for i in a:
    p*=i
print(p)    
smallest=a[0]
for i in a:
    if i<smallest:
        smallest=i
print(smallest)
'''
'''
#ques9
n=int(input())
a=[]
for i in range(n):
    x=int(input())
    a.append(x)
print(a)
sorted_list=[]
for i in range(n):
    largest=a[0]
    for j in a:
        if j>largest:
            largest=j
    sorted_list.append(largest)
    a.pop(a.index(largest))
print(sorted_list)  
'''
'''
#ques10try
s=input().lower()
main='abcdefghijklmnopqrstuvwxyz'
for i in s:
    word=''
    if i in main:
        word+=i
    elif i=='-':
        continue
'''
'''
# ques10
s = input()
a = s.split('-')

for i in range(len(a)):
    m = i
    for j in range(i+1, len(a)):
        if a[j] < a[m]:
            m = j

    t = a[i]
    a[i] = a[m]
    a[m] = t

s = ''
for i in range(len(a)):
    if i == 0:
        s = a[i]
    else:
        s = s + '-' + a[i]

print(s)
'''
'''
#ques11
s=input()
main='0123456789'
main1='abcdefghijklmnopqrstuvwxyz'
main2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d=0
a=0
u=0
l=0
sp=0

for i in s:
    if i in main:
        d+=1
    elif i in main1:
        a+=1
        l+=1
    elif i in main2:
        a+=1
        u+=1
    elif i!=' ':
        sp+=1

print('Digits:',d)
print('Alphabets:',a)
print('Special Characters:',sp)
print('Uppercase:',u)
print('Lowercase:',l)
'''
'''
#ques12
s=input()
snew=''
for i in s:
    if i not in snew:
        snew+=i
    else:
        continue
print(snew)
'''





























































