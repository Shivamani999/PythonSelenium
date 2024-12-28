# print("Hello world")
#
# a = 3
# print(a)
#
# b, c, d = 10, 4.5, "Shiva"
# print(d)
# print("Value of b var is:", b)
# print("{} {}".format(d, b))
# print(type(d))
#
# values = [1, 2, "shiva", 4.5]
# print(type(values))
# print(values[-1])
# print(values[1:3])  # last index excludes
# values.insert(3, "mani")
# print(values)
# values.append(0.34)
# print(values)
# values[2] = "SHIVA"
# print(values)
#
# val = (1, 2, "shiva", 4.5)
# print(type(val))
# print(val[1])
# print(val)
#
# student = {
#     "firstname": "Shivamani",
#     "surname": "Konam",
#     "age": 24
# }
# print(student.get("firstname"))
# print(student['firstname'])
# print(student['firstname'].upper())
#
# boolean = "True"
# if boolean == "True":
#     print("True")
# else:
#     print("False")
#
# obj = [1, 2, 3, 4, 5]
# for i in obj:
#     if i % 2 == 0:
#         print(i ** 2)
#
# sum = 0
# for j in range(0, 6):
#     sum += j
# print(sum)
#
# for k in range(0, 10, 3):
#     print(k)
#
# it = 10
# while it > 1:
#     print(it)
#     it -= 1
#
# while it > 1:
#     if it == 9:
#         it -= 1
#         continue
#     elif it == 3:
#         break
#     print(it)
#     it -= 1
#
#
# def add_two(abi, bdi):
#     print(abi + bdi)
#
#
# add_two(2, 4)
#
#
# def mul_two(q, l):
#     return q * l
#
#
# print(mul_two(2, 5))

# class Calculator:
#     num = 100  # class var
#
#     def __init__(self, a, b):
#         print("Iam called Automatically and this is constructor")
#         self.a = a
#         self.b = b
#
#     def getdata(self):
#         print("Executing in class")
#
#     def sum(self):
#         return self.a + self.b
#
#
# obj1 = Calculator(10, 2)
# obj1.getdata()
# print(obj1.sum())

str1 = " Shivamani konam "
print(str1[1])
print(str1[0:5])
print("This is " + str1)
var = str1.split(" ")
print(var)
str2 = str1.strip()
print(str2)
str3 = str1.replace(" ", "")
print(str3)

try:
    with open('textfile.txt', 'r') as reader:
        print(reader.read())

except Exception as e:
    print(e)

finally:
    print("finally block")
