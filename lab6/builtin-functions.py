#Task 1:
print(eval(('*').join(input().split())))

#Task 2:
import re
def upperandlower(text):
    cnt1 = 0
    cnt2 = 0
    for i in text:
        if i.isupper():
            cnt1 = cnt1 + 1
        elif i.islower():
            cnt2 = cnt2 + 1
    print(cnt1)
    print(cnt2)

upperandlower('QWErty')

#Task 3:
def palindrom(text):
    text1 = text[::-1]
    if text1 == text:
        print('palindrom')
    else:
        print('not palindrom')

palindrom('oiu')
palindrom('asa')

#Task 4:
import time
def square(x,y):
    x1 = x ** (1/2)
    time.sleep(y/1000)
    print(f'Square root of {x} after {y} miliseconds is {x1}')

square(25100, 2123)

#Task 5:
mylist = [True, True, True]
x = all(mylist)
print(x)