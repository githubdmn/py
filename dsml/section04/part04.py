print("Part 4")


def timestwo(num):
    return num * 2


print(timestwo(3))


# map

seq = [1, 2, 3, 4, 5]
seqmap = map(timestwo, seq)
print(seqmap)
print(list(seqmap))


lambda x: x * 2

print(list(map(lambda x: x * 3, seq)))

# filter - Return an iterator yielding those items
# of iterable for which function(item) is true.
# If function is None, return the items that are true.
print(list(filter(lambda x: x % 2 == 0, seq)))

# https://www.w3schools.com/python/python_ref_functions.asp
# https://www.w3schools.com/python/python_ref_string.asp
# https://www.w3schools.com/python/python_ref_list.asp
# https://www.w3schools.com/python/python_ref_dictionary.asp
# https://www.w3schools.com/python/python_ref_tuple.asp
# https://www.w3schools.com/python/python_ref_set.asp
# https://www.w3schools.com/python/python_ref_file.asp

out1 = "x" in ["x", "y", "z"]
print(out1)

example = [(1, 2), (3, 4), (5, 6)]
for a, b in example:
    print(a)
    print(b)
