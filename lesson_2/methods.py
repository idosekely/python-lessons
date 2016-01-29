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
"x + 5" is the definition.
if x = 2, the return value is 7
'''

def multiply_by_3(x):
    c = x * 3
    return c  # can we make it shorter?

# how to run a method?

multiply_by_3(5)  # will return 15

def sum_2(x, y):
    print "the sum is: %s" % x + y
    return x + y

a = sum_2(1, 3)  # will print "the sum is: 4" and will return 4 into a

# what about this?
a = sum_2("hello ", "world!")

# more advance methods
def sum_3(x, y=5):
    return x + y

sum_3(4)      # return 9
sum_3(1, 3)   # return 4

# follow carefully on the positional arguments and the keyword arguments
def test(a=1, b=5):
    print a
    print b

test()
test(1, 2)
test(5)
test(b=3)
test(b=1, a=5)

# you can create general methods that can accept anything!
def foo(*args, **kwargs):
    print args
    print kwargs

foo()
foo(1, 2, 3)
foo(1, 2, 3, c=4)
foo(1, 2, 3, c=4, 5)  # error! you can't pass positional arguments after keyword argument
