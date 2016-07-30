__author__ = 'sekely'

# you can insert your own data!
x = input("please enter your name: ")
print('welcome to the first lesson, %s!' % x)

a = input('enter the first number: ')
b = input('enter the second number: ')

# what is the problem here?
print("the sum of these numbers is: %s" % (a + b))
print("and the average is: %s" % ((a + b) / 2.0))

# let's fix!
print("the sum of these numbers is: %s" % (int(a) + int(b)))
print("and the average is: %s" % ((int(a) + int(b)) / 2.0))

# can we do it a bit better?
