print("Part2")

# dictionaries are a key-value pair data structure equivalent to maps in js
# d = {'key': value, 'key2': value...}
d = {'name': 'John', 'age': 43}
print(d)
print('Dictionary key {}'.format(d['name']))

# tuples cannot be reassigned - immutable
t = (4, 7, 2)
print(t[0])

# set is a colection of unique elements
messageSet = 'Sets are mutable'
print(messageSet)
s1 = {1, 2, 3}
s2 = {1, 1, 1, 2, 2, 3, 3, 3}
print('Set {}, {}'.format(s1, s2))
toSet = set([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3])
print('list to set {}'.format(toSet))

'''
Comparison operators <. <=, ==, >=, >, !=
'''
if 1 < 2:
    print('Correct')

if 1 == 2:
    print('First')
elif 3 == 3:
    print('Middle')
else:
    print('Last')
