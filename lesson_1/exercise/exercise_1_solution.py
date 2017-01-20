__author__ = 'sekely'
from getpass import getpass

username = input('please enter user name: ')
password = getpass('please enter password: ')

num1 = input('please provide 1st number: ')
num2 = input('please provide 2nd number: ')
print('the sum of those numbers is: %s' % str(float(num1) + float(num2)))
