__author__ = 'sekely'

'''
collecting, ordering, searching and presenting data is very important in computer science and programming.
keeping the data in a variable is nice, but how can you find it later?

examples:
1) if you are reading 1 million phone book entries, will you keep each record as a variable?
2) the user provides 1000 numbers - how can we sort them? how can we count how many numbers are there from each one?
3) user provides a username. how can we check if someone already provided that username
'''


'''
the dictionary:

dictionary is key:value based data structure.
think of it as... well, dictionary.
easy to search for values, easy to save data.
keys are unique
'''

d = {'a': 1,
     'b': 2}

d2 = dict()
d2['a'] = 1
d2['b'] = 2

# some useful dict methods
d.keys()    # return list of keys. see list below
d.values()  # return list of values
d.items()   # return list of tuples. on tuples, see below
len(d)      # return 2

# how to search in a dict? few ways
'a' in d       # return True
'a' in d             # return True
'a' in iter(d.keys())  # return True
d['a']               # return 1
d.get('a')           # return 1
d['c']               # KeyError!
d.get('c')           # return None


'''
the list
list is a container for ordered objects.
since it keeps the order of objects, it has many implications: Queues, Stacks and more.
you can access specific members by location, but take a note: list indices are starting from 0 to N-1

just think of it as a queue in a grocery store (FIFO) or rifle magazine (LIFO)
'''

l = [2, 1, 4, 3]
l.append(5)       # [2, 1, 4, 3, 5]
l[0]              # return 1
l[-1]             # return 5
l.pop()           # return 5, and the list will be [2, 1, 4, 3]
l.sort()          # sort the list, [1, 2, 3, 4].
len(l)            # return 4

# list slicing
# you can slice a list from index to index
l = [1, 2, 3, 4, 5]
l[2:4]               # return [3, 4]
l[1:]                # return [2, 3, 4, 5]
l[:-2]               # return [1, 2, 3]
l[1:-1:2]            # return [2, 4]
l[::2]               # return [1, 3, 5]

# search in list
l = ['a', 2, 'c', 4, 'd']
'a' in l       # True
5 in l         # False
l.index('c')   # return 2


'''
the tuple
Tuples are fixed size in nature whereas lists are dynamic.
In other words, a tuple is immutable whereas a list is mutable.
sometimes, when returning multiple values from a method, the returns are tuple
'''
a = (1, 1, 2, 3)
a.count(1)       # print 2

def test():
    return 1, 2
t = test()
type(t)          # tuple


'''
the set
set is unordered, unique entry container.
each object will appear exactly once, and the order is not guaranteed.

think of it as group of friends. the order doesn't matter, and each person is unique
'''

s = {1, 1, 1, 2, 3}
print(s)                  # {1, 2, 3}
s.add(4)                  # {1, 2, 3, 4}
s.add(2)                  # {1, 2, 3, 4}

# sets and arithmetic
s1 = {1, 2, 3}
s2 = {3, 4, 5}

s1.union(s2)         # union, {1, 2, 3, 4, 5}
s1 - s2              # the members of s1, that are not in s2 - {1, 2}
s2 - s1              # {4, 5}
s1.intersection(s2)  # intersection, the common. {3}
