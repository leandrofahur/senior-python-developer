from functools import reduce

# Notes:
# 1. Deterministic: always returns the same output given the same input
# 2. No side effects: does not depend on outside world (resources)
# 3. No mutation: does not change the input

# # pure function:
# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list


# print(multiply_by2([1, 2, 3]))


# map, filter, zip, reduce
def multiply_by2_map(item):
    return item*2


my_list = [1, 2, 3]
your_list = [10, 20, 30]

# map: apply a function to every item in an iterable
print('map:\n')
print(list(map(multiply_by2_map, my_list)))
print(list(map(lambda item: item*2, my_list)))
print(my_list)  # my_list is not changed
print('\n')


# filter: filter out items from an iterable
def only_odd(item):
    return item % 2 != 0


print('Filter:\n')
print(list(filter(only_odd, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(my_list)  # my_list is not changed
print('\n')


# zip: zip together two or more iterables
print('zip:\n')
print(list(zip(my_list, your_list)))
print(my_list)  # my_list is not changed
print(your_list)  # your_list is not changed
print('\n')


# reduce: reduce an iterable to a single value
def accumulator(acc, item):
    print(acc, item)
    return acc + item


print('reduce:\n')
print(reduce(accumulator, my_list, 0))
print(my_list)  # my_list is not changed
print('\n')

# lambda expression
print('lambda:\n')
print(reduce(lambda acc, item: acc + item, my_list, 0))
print(my_list)  # my_list is not changed
