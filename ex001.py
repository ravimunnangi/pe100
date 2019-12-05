#exercise 1
a=2
a=4
a=6
print(a+a+a)

#exercise 2
#Variable names must start with a letter or an underscore. Everything else will throw a SyntaxError.

#exercise 3
#variable to be defined before use

#exercise 4
a="1"
b=2
print(int(a)+b)
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