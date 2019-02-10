print('hello World')
print('new line/n')

s = "Hello World"
# We can use this to print a string backwards
print(s[::-1])

# Three ways to perform string formatting are:
# C style with placeholders using the modulo % character
# The format() method.
# Newest method, introduced with Python 3.6, uses formatted string literals, called f-strings

x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))
print('I once caught a fish %s.' %'this \tbig')
print('I once caught a fish %r.' %'this \tbig')
print('Floating point numbers: %10.2f' %(13.144))

print('This is a string with {} insert'.format(x))

print(f"He said he wants {y}.")
