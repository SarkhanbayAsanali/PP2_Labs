#Task 1:
import os

path = "C://Users//jokis//Desktop//github//lab5"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")
print(dir_list)

#Task 2:
import os

path=r'C:\Users\jokis\Desktop\github\lab6'

print(os.access(path,os.F_OK))
print(os.access(path,os.R_OK))
print(os.access(path,os.W_OK))
print(os.access(path,os.X_OK))

#Task 3:
import os
print("Test a path exists or not:")
path = r'C:\Users\jokis\Desktop\github\lab6\dir-and-files\a.txt'
print(os.path.exists(path))
path = r'C:\Users\jokis\Desktop\github\lab6\dir-and-files\work.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))

#Task 4:
import os

with open(r'C:\Users\jokis\Desktop\github\lab6\dir-and-files\work.txt') as path:
    lines=len(path.readlines())

print(lines) 

#Task 5:
import os
items = ['Mango', 'Orange', 'Apple', 'Lemon']
file = open('work.txt','w')
file.writelines(items)
file.close()

#Task 6:
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

#Task 7:
import os
with open("work.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)

#Task 8:
import os

path = r'C:\Users\jokis\Desktop\github\lab6\dir-and-files\delete.txt'

if os.path.exists(path):
    os.remove(path)
else:
    print("file doesn't exists")