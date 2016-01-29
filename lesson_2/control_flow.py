__author__ = 'sekely'

'''
most of our programs are based on some decision making.
but how do we decide what to do?
how can we tell a certain piece of code to run few times?
'''

# we are using booleans to make a decision
# if... then... else

x = raw_input("please enter number: ")
x = int(x)

if x > 3:
    print x
else:
    print "your number is not big enough!"

# blocks of code are distinguish by using indentation.
# in python, the standard is using the TAB key, with 4 spaces

# the for loop
for x in range(5):
    print x

# the for loop iterates over the given data. we can use it in many forms
sentence = 'this is a sentence'
for c in sentence:
    print c

# the while loop
while x > 3:
    print x
    x = x - 1

# what was x? where did we set it?
# what happen if we'll change the ">" to ">=" ?
# why can we assign "x - 1" back into x?

# wrap it together
for c in sentence:
    if c == ' ':
        pass
    else:
        print c

# how can we do it shorter?
for c in sentence:
    if c != ' ':
        print c
