# file = open('text.txt')
# print(file.read())
# print(file.read(5))

# print(file.readline())
# print(file.readline())

# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# lst = file.readlines()
# print(lst)
# for i in lst:
#     print(i)

# file.close()

# Instead of using above open and close methods we can use:-
with open('text.txt', 'r') as file:
    content = file.readlines()
    with open('text.txt', 'w') as writer:
        for line in content:
            writer.write(line)
        for line in reversed(content):
            writer.write(line)


with open('text.txt', 'r') as file:
    print(file.read())
