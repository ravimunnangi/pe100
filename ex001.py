#exercise 1
a=2
a=4
a=6
print('exercise 1:', a+a+a)

#exercise 2
#Variable names must start with a letter or an underscore. Everything else will throw a SyntaxError.

#exercise 3
#variable to be defined before use

#exercise 4
a="1"
b=2
print('exercise 2:', int(a)+b)
letters =['a','b','c','d','e','f','g','h','i','j']
print(letters[1])
#list slicing is upper-bound exclusive
print('printing from 4th to 6th character', letters[3:6])
print('print first 3 characters', letters[:3])
print('print second character from last', letters[-2])
print('print last 3 items',letters[-3:])
print('print alternate characters',letters[::2])

#exercise 11 - print a list from 1 to 20
my_range = range(1,21)
print(list(my_range))
print([i*10 for i in my_range])
print([str(i) for i in my_range])
print(list(map(str, my_range)))
#Map, filter, reduce
#Map - applies a function to all the items on the input_list - map(function, input_list)
print(list(map(lambda x:str(x),my_range)))

a = ["1", 1, "1", 2]
print('list after removing duplicates - but order may not be preserved', list(set(a)))

from collections import OrderedDict
print('list after removing duplicates - order preserved', list(OrderedDict.fromkeys(a)))
#python collections - read about them

dict_var = {'a':1, 'b':2}
dict_var = dict(a=1, b=2)
print(dict_var)
#A dict  function is another way to create a dictionary. dict  is also used to convert other objects to a dictionary.
print(dict_var['b'])
print(dict_var['a'] + dict_var['b'])
dict_var['c'] = 3
print(dict_var)

import functools
print(functools.reduce(lambda a,b : a +b ,list(dict_var.values())))
print(sum(dict_var.values()))

dict_var = dict((key, value) for key, value in dict_var.items() if value <= 1)
print(dict_var)

keys_list = ['a','b','c']

from pprint import pprint
dict_var1={}
for i, key in enumerate(keys_list):
    dict_var1[key] = [x for x in range(i*10 + 1, i*10 + 11)]
pprint(dict_var1)

print(dict_var1['b'][2])
for key, value in dict_var1.items():
    print(key, " has value ", value)

for x in range(ord('a'), ord('z') + 1):
    print(chr(x))

import string
for letter in string.ascii_lowercase:
    print(letter)

for i in range(1,11):
    print(i)

def acceleration(v2,v1,t2,t1):
    return (v2-v1)/(t2-t1)

print(acceleration(10,5,3,1))

from math import pi

def lvc(h, r=10):
    return ((4 * pi * r**3)/3) - (pi * h**2 * (3*r - h)/3)

print(lvc(2))

inp_str = 'hello how are you'
print('count of words in string ', len(inp_str.split(' ')))

import re
word_count = 0
with open('words1.txt','r') as inp_file:
    for line in inp_file:
        word_count = word_count + len(re.split(' |,',line))
print('no fo words in the file', word_count)

import string
with open('words2.txt','w') as out_file:
    for ch in string.ascii_lowercase:
        out_file.write(ch + '\n')

a = [1,2,3]
b = (4,5,6)

for i, j in zip(a,b):
    print(i + j)

a = [ch for ch in string.ascii_lowercase]
lis_a = a[::3]
lis_b= a[1::3]
lis_c = a[2::3]
for ch1, ch2, ch3 in zip(lis_a, lis_b, lis_c):
    print(ch1 + ch2 + ch3)

import os
os.makedirs('letters',exist_ok=True)

for ch in string.ascii_lowercase:
    with open('letters/' + ch + '.txt', 'w') as ch_file:
        ch_file.write(ch)

import glob
chrs = ''
file_pattern = 'letters/*.txt'
file_list = glob.glob(file_pattern)
file_list.sort(key=os.path.getctime)
for file in file_list:
    with open(file, 'r') as ch_file:
        chrs = chrs + ch_file.read()

chrs_list = [ch for ch in chrs]
print(chrs_list)

python_list = [ch for ch in chrs_list if ch in 'python']
print(python_list)

#cannot use keywords for variable names

print(type("Hey".replace("ey","i")[-1]))

fn = input("your first name: ")
ln = input("your last name: ")
print("you first name is %s and your last name is %s" % (fn, ln))

