__author__ = 'sekely'

'''
methods are the base to every program.
these are functional pieces of code, that we'll probably want to reuse.
methods in python are very easy to define, using the "def" keyword
methods can return one result, many results or no results.

this of methods as the defenition of "f(x)" in high school.
for example, f(x) = x + 5
"f" is the name of the function
"x" is the input
"x + 5" is the defenition.
if x = 2, the return value is 7
'''

def multiply_by_3(x):
    c = x * 3
    return c  # can we make it shorter?

# how to run a method?

multiply_by_3(5)  # will return 15