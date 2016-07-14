__author__ = 'sekely'

# this is a comment. we use it for code documentation.

'''
this is comment block.
everything between those markers,
is considered
as a string, or block
'''

1 + 1  # these are pure integers, complete numbers. the result is '2'

3 / 1  # division ot integers will produce an integer. in that case, '3'.

5 / 3  # what is the result in that case?

1.0 + 1.0  # these are float numbers. they represent numbers with floating point. the result is '2.0'

5.0 / 3.0  # what about now?

'''
so the result of two integers is integer.
the result of two floats, is float.
what about integer and float?

try it!
'''

'this is a string'
"this is also a string"

# is there any difference? (no!)
# calling to "print" will always reproduce a string output!

1 == 5  # this is boolean. it has only two results - True or False.

1 != 5  # now it's True!


# Summary
# math and operands
5 / 3      # 1
5.0 / 3    # 1.6666666666666667
5.0 // 3   # 1.0
5 % 3      # 2
5 ** 3     # 125

# strings and some string manipulation
len('hello')                          # 5
print(('hello ' + 'world'))              # 'hello world'
print(('this is %s format' % 'string'))  # 'this is string format'
print(('My Name'.upper()))               # 'MY NAME'
print(('My Name'.lower()))               # 'my name'

# boolean expression and algebra
not False       # True
not True        # False
False and True  # False
True and True   # True
True or False   # True
False or False  # False
5 == 5          # True
3 != 5          # True
5 < 3           # False
5 <= 5          # True
