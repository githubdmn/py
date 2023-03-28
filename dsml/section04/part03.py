print('Part3 - loops')

seq = [1, 2, 3, 4, 5]

for item in seq:
    print(item)

i = 1
while i < 5:
    print('i is {}'.format(i))
    i = i + 1


# range - generator of numerical values
for item in range(0, 5):
    print(item)

print(list(range(0, 5)))

######## LIST COMPREHENSION #########
# List comprehension offers a shorter syntax
# when you want to create a new list based on the values of an existing list

x = list(range(0, 5))
out = []
for i in x:
    out.append(i**2)
print(out)

out_comprehension = [num ** 2 for num in x]
print(out_comprehension)


def myName(name='Default'):
    print('Hello {}'.format(name))


myName('John')
myName()


def square(num):
    '''
    This is a docstring.
    This provides info for the function.
    '''
    return num**2


print(square(4))
