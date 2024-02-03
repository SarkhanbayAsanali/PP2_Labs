#Example 1:
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Note: the set list is unordered, meaning: the items will appear in a random order.

Output: {'apple', 'cherry', 'banana'}

#Example 2:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

Output:
apple
cherry
banana

#Example 3:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

Output: True

#Example 4:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

Output: {'orange', 'banana', 'cherry', 'apple'}

#Example 5:
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

Output: {'banana', 'cherry', 'apple', 'orange', 'mango', 'grapes'}

#Example 6:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

Output: 3

#Example 7:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

Output: {'apple', 'cherry'}

#Example 8:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

Output: {'apple', 'cherry'}

#Example 9:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal

Output:
apple
{'cherry', 'banana'}

#Example 10:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

Output: set()

#Example 11:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists

Output:
Traceback (most recent call last):
  File "demo_set_del.py", line 5, in <module>
    print(thisset) #this will raise an error because the set no longer exists
NameError: name 'thisset' is not defined

#Example 12:
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.

Output: {'apple', 'banana', 'cherry'}