#lab4

#ques1
'''
salary=int(input('Enter your salary:'))
service=int(input('Enter the years of sevice:'))
if service>5:
    print('Your bonus is:',salary*0.05)
else:
    print('You are ineligible for bonus.')
    '''
   
#ques2
'''
password=int(input('Enter your password:'))
if password=='s3cr3t!P@ssw0rd':
    print('Welcome!')
else:
    print('Wrong Password!')
    '''
    
#ques3
'''shape=input('Enter the name of the shape you want to find area of :')
if shape=='square':
    a=int(input('Enter the side of the square:'))
    print('The area of square is:' ,f"{ a*a:.3f}")
elif shape=='circle':
    r=int(input('Enter the radius of the circle:'))
    print('The area of circle is:',f"{3.14*r*r:.3f}")
elif shape=='rectangle':
    l=int(input('Enter the length of the rectangle:'))
    b=int(input('Enter the breadth of the rectangle:'))
    print('The area of rectangle is :',f"{l*b:.3f}")
elif shape=='triangle':
    h=int(input('Enter the height of triangle:'))
    b=int(input('Enter the base of the triangle:'))
    print('The area of triangle is:',f"{0.5*b*h:.3f}")'''
   
#ques4

'''h=int(input('Enter the hours:'))
m=int(input('Enter the miniutes:'))
m+=15
if m<60 and 0<h<24:
    print('HH:MM =',h,':','0'+str(m))
elif m>=60 and 0<h<24 and m%60<10:
    print('HH:MM =',h+m//60, ':','0'+str(m%60))'''
    
    
   
#ques5
'''
k=int(input('Enter the kilometeres you want to travel:'))
period=(input('Enter the period of the day:(day or night):'))
taxi_d=33.58+37.89*k
taxi_n=33.58+43.17*k
bus=4.32*k
train=2.88*k
if k>=100 and period=='day':
    smallest=train
    if taxi_d<smallest:
        print('Price to travel with cheapest transport is :',taxi_d)
    elif bus<smallest:
        print('Price to travel with cheapest transport is :',bus)
    else:
        print('Price to travel with cheapest transport is :',train)
elif k>=100 and period=='night':
    smallest=train
    if taxi_n<smallest:
        print('Price to travel with cheapest transport is :',taxi_n)
    elif bus<smallest:
        print('Price to travel with cheapest transport is :',bus)
    else:
        print('Price to travel with cheapest transport is :',train)
elif 100>k>=20 and period=='day':
    smallest=taxi_d
    if bus<smallest:
        print('Price to travel with cheapest transport is :',bus)
    else:
        print('Price to travel with cheapest transport is :',taxi_d)

elif 100>k>=20 and period=='night':
    smallest=taxi_n
    if bus<smallest:
        print('Price to travel with cheapest transport is :',bus)
    else:
        print('Price to travel with cheapest transport is :',taxi_n)
elif k<20 and period=='day':
    print('Price to travel with cheapest transport is :',taxi_d)
elif k<20 and period=='night':
    print('Price to travel with cheapest transport is :',taxi_n)
    '''
#ques6
'''h=int(input('Enter the number of holidays:'))
playtime=h*127+(365-h)*63
if playtime>30000:
    print('Tom can not sleep well and needs',playtime-30000,'hours more.')
else:
    print('Tom can sleep well.')
    
   '''
    
#ques7
'''
budget=int(input('Enter the budget :'))
season=input('Enter the season:')

if budget<=100:
    if season=='summer':
        print('You will spend ',budget*0.3,'BGN in Bulgaria.')
    if season=='winter':
        print('You will spend ',budget*0.7,'BGN in Bulgaria.')
        
if budget<=1000:
    if season=='summer':
        print('You will spend ',budget*0.4,'BGN in Bulgaria.')
    if season=='winter':
        print('You will spend ',budget*0.8,'BGN in Bulgaria.')
    
if budget>1000:
    if season=='summer':
        print('You will spend ',budget*0.9,'BGN in Bulgaria.')
    if season=='winter':
        print('You will spend ',budget*0.9,'BGN in Bulgaria.')
    '''
   
#ques8
'''
for i in range(6,1001,10):
    print(i)
   '''
#ques9
'''
n=int(input('Enter no of times u want to repeat typing numbers:'))
s=0
for i in range(n):
    i=int(input('Enter the number:'))
    s+=i
print('Sum of n numbers is:',s)
  '''
    
#ques10
n=int(input('Enter the number to print table of :'))
for i in range(1,21):
    print(n,'X',i ,'=',n*i)
    
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   