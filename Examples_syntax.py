#Example 1:
print ("Hello World")

#Example 2:
#This is a comment.
print ("Hello, World!")

Output: Hello, World!

#Example 3:
"""This is a
multiline docstring."""
print ("Hello, World!")

Output: Hello, World!

#Example 4:
x = 5
y = "John"
print (x)
print (y)

Output: 
5
John

#Example 5:
x = "Python"
y = "is"
z = "awesome"
print (x, y, z)

Output: Python is awesome

#Example 6:
x = "Python "
y = "is "
z = "awesome"
print (x + y + z)

Output: Python is awesome

#Example 7:
x = 1
y = 2.8
z = 1j

print (type(x))
print (type(y))
print (type(z))

Output: 
<class 'int'>
<class 'float'>
<class 'complex'>

#Example 8:
x = 1
y = 35656222554887711
z = -3255522

print (type(x))
print (type(y))
print (type(z))

Output: 
<class 'int'>
<class 'int'>
<class 'int'>

#Example 9:
x = 1.10
y = 1.0
z = -35.59

print (type(x))
print (type(y))
print (type(z))

Output:
<class 'float'>
<class 'float'>
<class 'float'>

#Example 10:
x = 35e3
y = 12E4
z = -87.7e100

print (type(x))
print (type(y))
print (type(z))

Output:
<class 'float'>
<class 'float'>
<class 'float'>

#Example 11:
x = 3+5j
y = 5j
z = -5j

print (type(x))
print (type(y))
print (type(z))

Output:
<class 'complex'>
<class 'complex'>
<class 'complex'>

#Example 12:
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

Output:
1
2
3

#Example 13:
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

Output:
1.0
2.8
3.0
4.2

#Example 14:
x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)

Output:
s1
2
3.0

#Example 15:
a = "Hello, World!"
print(a[1])

Output: e

#Example 16:
b = "Hello, World!"
print(b[2:5])

Output: llo

#Example 17:
a = "Hello, World!"
print(a.strip())

Output: Hello, World!

#Example 18:
a = "Hello, World!"
print(len(a))

Output: 13

#Example 19:
a = "Hello, World!"
print(a.lower())

Output: hello, world!

#Example 20:
a = "Hello, World!"
print(a.upper())

Output: HELLO, WORLD!

#Example 21:
a = "Hello, World!"
print(a.replace("H", "J"))

Output: Jello, World!

#Example 22:
a = "Hello, World!"
b = a.split(",")
print(b)

Output: ['Hello', ' World!']