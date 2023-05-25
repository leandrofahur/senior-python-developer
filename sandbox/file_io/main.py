file = open('test.txt')
print(file.read())
file.seek(0)

print(file.readlines())

file.close()
