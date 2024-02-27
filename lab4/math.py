#Task 1:
def to_rad(n = int(input())):
    r = (n * 3.14)/180
    print(r)

to_rad()

#Task 2:
def area(h, a, b):
    d = a + b
    S = (d / 2)*h
    print(S)

area(5, 5, 6)

#Task 3:
import math
a=int(input())
b=int(input())
print(int((pow(b,2)*a)/(4*math.tan((math.pi/a)))),sep='')

#Task 4:
def prl(a, b):
    print(a * b)
prl(5, 6)