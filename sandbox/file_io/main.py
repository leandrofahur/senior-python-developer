# file = open('test.txt')
# print(file.read())
# file.seek(0)

# print(file.readlines())

# file.close()

with open('test.txt', mode='r+') as my_file:
    text = my_file.write('Hey it\'s me!')
    print(my_file.readlines())
