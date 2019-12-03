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