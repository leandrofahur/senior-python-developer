# Notes:
# 1. Deterministic: always returns the same output given the same input
# 2. No side effects: does not depend on outside world (resources)
# 3. No mutation: does not change the input

# pure function:
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by2([1, 2, 3]))

# map, filter, zip, reduce
