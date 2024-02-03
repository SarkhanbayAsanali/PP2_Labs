#Example 1:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

Output: ('apple', 'banana','cherry')

#Example 2:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

Output: banana

#Example 3:
thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant"
# the value is still the same:
print(thistuple)

Output: ('apple', 'banana', 'cherry')

#Example 4:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

Output:
apple
banana
cherry

#Example 5:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

Output: Yes, 'apple' is in the fruits tuple

#Example 6:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

Output: 3

#Example 7:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

Output:
Traceback (most recent call last):
  File "demo_tuple_del.py", line 3, in <module>
    print(thistuple) #this will raise an error because the tuple no longer exists
NameError: name 'thistuple' is not defined

#Example 8:
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

Output: ('apple', 'banana', 'cherry')