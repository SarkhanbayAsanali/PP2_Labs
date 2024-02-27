#Task 1:
import re

def text_match(text):
    sd = '^a(b*)$'
    if re.search(sd, text):
        return 'Found a match'
    else:
        return 'not matched' 
print(text_match("ab"))


#Task 2:
import re

def text_match(text):
    sd = '^abb$'
    ds = '^abbb$'
    if re.search(sd, text) or re.search(ds, text):
        print('Found a match')
    else:
        print('not matched')

text_match('abb')
text_match('abbb')
text_match('abbbb')

#Task 3:
import re

def low_case(text):
    sd = re.findall('[a-z]_',text)
    if sd:
        print(sd)
    else:
        print('no match')

low_case('Mfive_comp_')

#Task 4:
import re

def up_low(text):
    sd = re.findall('[A-Z][a-z]+', text)
    print(sd)

up_low('BmwMfive')

#Task 5:
import re

def a_b(text):
    x = 'a.*?b$'
    if re.search(x, text):
        print('Found a match')
    else:
        print('Not mached')
a_b('ahdgcwbevgvcb')

#Task 6:
import re

def space(text):
    x = re.sub("\s", ":", text)
    y = re.sub('\.', ':', x)
    z = re.sub('\,', ':', y)
    print(z)

space('zx d,s asz.ka.lp')

#Task 7:
import re

snake = "snake_case_asdfg"
capital = snake.upper()
camel = ""
i = 0
while(i != len(snake)):
    if(snake[i] == '_'):
        camel = camel + capital[i+1]
        i = i + 2
    else:
        camel = camel + snake[i]
        i = i + 1
print(camel)

#Task 8:
import re

text = "asdAsdaSd"
print(re.findall('[A-Z][^A-Z]*', text))

#Task 9:
import re

def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)
print(capital_words_spaces("DamirChert"))

#Task 10:
def camel_to_snake(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
print(camel_to_snake('QwertAsdf'))