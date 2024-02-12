#Example 1:

def my_function():
    print("Hello from a function")

my_function()

Output:
Hello from a function

#Example 2:

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

Output:
Emil Refsnes
Tobias Refsnes
Linus Refsnes

#Example 3:

def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

Output:
I am from Sweden
I am from India
I am from Norway
I am from Brazil

#Example 4:

def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

Output:
15
25
45

#Example 5:

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)

Output:
Recursion Example Results
1
3
6
10
15
21