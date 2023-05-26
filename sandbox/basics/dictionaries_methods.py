dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

print("dictionary['a']: ", dictionary['a'])
print("dictionary: ", dictionary)

my_list = [
    {
        'a': 1,
        'b': 2,
        'c': 3,
    },
    {
        'a': 4,
        'b': 5,
        'c': [6, 7, 8],
    },
    {
        'a': None,
    }
]

print("my_list: ", my_list)
print("my_list[0]: ", my_list[0])
print("my_list[1]['c']: ", my_list[1]['c'])
print("my_list[1]['c'][1][1]: ", my_list[1]['c'][1])

# add:
dictionary['e'] = 5
print("add dictionary: ", dictionary)

my_list[2]['a'] = 'something'
print("add my_list: ", my_list)

print("dictionary.keys(): ", dictionary.keys())
print("dictionary.items(): ", dictionary.items())
print("dictionary.values(): ", dictionary.values())

print("\n\n")

for key in dictionary:
    print("key: ", key)

for value in dictionary.values():
    print("value: ", value)

for items in dictionary.items():
    print("Items: ", items)