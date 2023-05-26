# file = open('test.txt')
# print(file.read())
# file.seek(0)

# print(file.readlines())

# file.close()

with open('test.txt', mode='w') as my_file:
    text = my_file.write('=)')
    print(text)
