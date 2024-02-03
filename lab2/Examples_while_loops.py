#Example 1:
i = 1
while i < 6:
    print(i)
    i += 1

Output:
1
2
3
4
5

#Example 2:
i = 1
while i < 6:
    print(i)
    if (i == 3):
        break
    i += 1

Output:
1
2
3

#Example 3:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# Note that number 3 is missing in the result

Output:
1
2
3
4
5
6