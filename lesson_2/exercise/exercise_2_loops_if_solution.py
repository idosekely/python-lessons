import getpass
__author__ = 'sekely'


'''
1)
look back on exercise 1, on the user and password input.
write 2 methods:
the first method should accept user and password
the second one should check that the password is not "simple" password, and print warning.
simple password is "123456"

2) medium
write a short code that prints all the even numbers up to 20

3) hard
without running it, what does this code do?

for x in range(10):
    for y in range(10):
        print(x * y, end=' ')
    print()

HINTS:
print(x * y, end=' ') won't print in a new line
print() will just create a new line
'''

# 1)
username = input('please enter user name: ')
password = getpass.getpass('enter password: ')
if password == '123456':
    print("please don't use simple passwords")

# 2)
for x in range (20):
    if x % 2 == 0:
        print(x)

# 3) this will print the multiplication board
