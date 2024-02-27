#Task 1:
def squares(end_point):
    current = 1
    while(current ** 2 <= end_point):
        yield current ** 2
        current += 1
print(*squares(16))

#Task 2:
class evennumbers():
    def __init__(self, n):
        self.n = n
        self.even = 0
        self.end_point = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.even > self.end_point:
            raise StopIteration()
        x = self.even
        self.even += 2
        return x

n = int(input())
for i in evennumbers(n):
    print(i)

#Task 3:
class divisible():
    def __init__(self, end):
        self.current = 0
        self.end_point = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.end_point + 12:
            raise StopIteration()
        self.current += 12
        return self.current - 12
        
n = int(input())
for i in divisible(n):
    print(i)


#Task 4:
def square(a,b):
    for i in range(a,b+1):
        yield i ** 2

print(*square(4,8))

#Task 5:
def gen(n):
    i=0
    while n>i:
        yield n
        n=n-1
for i in gen(int(input())):
    print(i)