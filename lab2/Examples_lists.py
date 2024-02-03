#Example 1:
thislist = ["apple", "banana", "cherry"]
print(thislist)

Output: ['apple', 'banana', 'cherry']

#Example 2:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

Output: banana

#Example 3:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

Output: ['apple', 'blackcurrant', 'cherry']

#Example 4:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

Output:
apple
banana
cherry

#Example 5:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

Output: Yes, 'apple' is in the fruits list

#Example 6:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

Output: 3

#Example 7:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

Output: ['apple', 'banana', 'cherry', 'orange']

#Example 8:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

Output: ['apple', 'orange', 'banana', 'cherry']

#Example 9:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

Output: ['apple', 'cherry']

#Example 10:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

Output: ["apple", "banana"]

#Example 11:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

Output: ["banana", "cherry"]

#Example 12:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

Output: []

#Example 13:
thislist = list(("apple", "banana", "cherry"))
print(thislist)

Output: ['apple', 'banana', 'cherry']