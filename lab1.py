#ques1 
'''print('Hello JKLU!')
print('I am learning Python')'''

#ques2
'''name=input('Enter your name:')
branch=input('Enter your branch:')
print('Welcome!',name, 'to the', branch ,'branch of JKLU.')'''

#ques3
'''length=int(input('Enter the length(in meteres) of rectangle you want to find area of:'))
breadth=int(input('Enter the breadth(in meteres) of rectangle you want to find area of:'))
print('The area of rectangle is:', length*breadth,'m^2')'''

#ques4
'''length=int(input('Enter the length(in feet) of rectangle you want to find area of:'))
breadth=int(input('Enter the breadth(in feet) of rectangle you want to find area of:'))
print('The area of rectangle(in m^2) is:', (length*breadth)/(3.28*3.28),'m^2')'''

#ques5
'''x=int(input('Enter the first number:'))
y=int(input('Enter the second number:'))
if y>=0 and x>0:
    if y%x == 0:
        print('Y is divisible by X.')
    else: 
        print('Y is not divisible by X.')
else:
    print('Input Invalid!')'''
    
#ques6
'''number= int(input('Enter the number you want to check even or odd:'))
if number%2 ==0:
    print("Number is even.")
else:
    print('Number is odd.')'''
    
#ques7
'''radius=int(input('Enter the radius of circle(0-100 units):'))
if 0<=radius<=100:
    print('The area of Circle is:',(22/7)*radius*radius)
else:
    print('Invalid Input!')'''
    
#ques8
'''temp=float(input('Enter the temperature in Celsius:'))
print("The temperature in kelvin is:",273.15+temp)
print("The temperature in fahrenheit is:",(9/5)*(temp)+32)'''

#ques9
'''seconds=int(input('Enter the number of seconds to be converted into HH:MM:SS:'))
miniutes=int(seconds/60)
mins=seconds/60
second=int((mins-miniutes)*60)
hours=int(mins/60)
if 1<=seconds<=86400:
    print('HH:MM:SS :',hours,':',miniutes,':',second)
else:
    print('Invalid Input!!')'''

#ques10
#(a)
'''a=int(input('Enter the total number of day the particular student attended college:'))
b=int(input('Enter the total number of days college was open:'))
percentage=(a/b)*100
if percentage>=75:
    print('The student is eligible.')
else:
    print('The student is ineligible.')'''
    
#(b)
'''unitspast=int(input('Enter the old reading of the electricity meter:'))
unitspresent=int(input('Enter the present reading of the electricity meter:'))
units=unitspresent-unitspast
rate=int(input('Enter the rate of each electricity unit(KWH) passed:'))
print('The amount due to be paid is:',units*rate)'''

#(c)
pin=int(input('Enter your 4 digit ATM Pin:'))
if pin==1024:
    print('Access Granted!')
else:
    print('Access denied!,\nYour ATM pin is wrong. \nPlease re-enter your pin')
    
#1
''' The easiest program was the first one '''
#2
'''I already know the basic python so this was easy for me hence i didn't encounter a major error for this lab questions.'''
#3
'''Some spelling mistake was present i corrected it'''
#4
'''The seconds to HH:MM:SS conversion program was new for me and hence it took time for me to solve it'''
