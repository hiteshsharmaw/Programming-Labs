#ques1

'''x1=int(input('Enter the value of x coordinate of the circle:'))
y1=int(input('Enter the value of y coordinate of the circle:'))
r=int(input('Enter the value of radius of the circle:'))
x2=int(input('Enter the value of x coordinate of the point:'))
y2=int(input('Enter the value of y coordinate of the point:'))
distance=(((x2-x1)**2)+((y2-y1)**2))**(1/2)
print(distance)
if distance>r:
    print('Point lies out of the circle.')
elif distance==r:
    print('Point lies on the circle.')
else:
    print('Point lies inside the circle.')'''

#ques2

'''side=int(input('Enter the side of a regular pentagon:'))
area=((5)*(side)**2)/(4*0.7265)
print('Area of pentagon is:',area)'''

#ques3

'''a1=int(input('Enter the angle number1:'))
a2=int(input('Enter the angle number2:'))
a3=int(input('Enter the angle number3:'))
if a1+a2+a3==180:
    if a1<90 and a2<90 and a3<90:
        print('These angles form an acute angled triangle.')
    elif a1>90 or a2>90 or a3>90:
        print('These angles form an obtuse angled triangle.')
    elif a1==90 or a2==90 or a3==90:
        print('These angles form a right angled triangle.')
else:
    print('These angles can not form a triangle.')'''
 
#ques4   
 
'''x=int(input('Enter a 4 digit number:'))
a=x//1000
print(a)
b=x//100-a*10
print(b)
c=x//10-(a*100+b*10)
print(c)
d=x-(a*1000+b*100+c*10)
print(d)
print('The sum of first two digits is :',a+b)
print('The sum of last two digits is :',c+d)
if a+b==c+d:
    print('The sums are also equal.')
else:
    print('The sums are not equal.')'''

#ques5
'''x=int(input('Enter a 5 digit number:'))
a=x//10000
print(a)
b=x//1000-a*10
print(b)
c=x//100-(a*100+b*10)
print(c)
d=x//10-(a*1000+b*100+c*10)
print(d)
e=x-(a*10000+b*1000+c*100+d*10)
print(e)
m=max(a,b,c,d,e)
print("The largest number among them is",m)
l1=[a,b,c,d,e]
print('The element is on',(l1.index(m)+1),'th position')'''


#ques6
'''a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
c=int(input('Enter the third number:'))
d=input('Enter a,b or c to be printed with new values:')
if d=='a':
    print('The value of a is:',c)
elif d=='b':
    print('The value of b is:',a)    
elif d=='c':
    print('The value of c is:',b)  ''' 
    
#ques7
'''x=int(input('Enter a 3 digit number:'))
a=x//100
print(a)
b=x//10-a*10
print(b)
c=x-(a*100+b*10)
print(c)
if x%(a+b+c)==0:
    print('The number is a Harshad Number.')
else:
    print('The number is not a Harshad Number.') '''   
    
#ques8
'''v=int(input('Enter the intial volume of the tank.'))
n=int(input('Enter the number of days after which you want to know the water in the tank.'))
x=0.95
print('The water after n days in tank is :',(v*x +10)) '''

#ques9
a1=int(input('Enter the coeff 1 of first straight line ax1+by1=c1:'))
b1=int(input('Enter the coeff 2 of first straight line ax1+by1=c1:'))
c1=int(input('Enter the coeff 3 of first straight line ax1+by1=c1:'))
a2=int(input('Enter the coeff 1 of second straight line ax2+by2=c2:'))
b2=int(input('Enter the coeff 2 of second straight line ax2+by2=c2:'))    
c2=int(input('Enter the coeff 3 of second straight line ax2+by2=c2:'))
x=(b1*c2-b2*c1)/(a2*b1-a1*b2)
y=(a1*c2-a2*c1)/(a1*b2-a2*b1)
print(f"Their point of intersection is(x,y):,{x:.2f},{y:.2f}")



























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    































