__author__ = 'sekely'

'''
we are using variables almost everywhere in the code.
variables are used to store results, calculations and many more.

this of it as the famous "x" from highschool
x = 5, right?

the only thing is, that in Python "x" can store anything
'''

# try this code:
x = 5
y = x + 3

print y

# what about this? will it work?
x = 'hello'
y = ' '
z = 'world!'
w = x + y + z
print w

# you can insert your own data!
x = raw_input("please enter your name: ")
print 'welcome to the first lesson, %s!' %x
