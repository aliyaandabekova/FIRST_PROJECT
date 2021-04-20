# numbers = [10, 20, 30, 40]
# for number in numbers:
#     print(number)

# numbers = [10, 20, 30, 40,2,3,5,3,3,1,90]
# for number in numbers:
#     if number % 2 == 0:
#         print(number)


# try:
#     # успешно
#     print("1" + "1")
# except TypeError:
#     # при наличии ошибки
#     print("except")
# finally:
#     # всегда
#     print("finally")


# try:
#     # успешно
#     print("1" + 1)
# except Exception:
#     # при наличии ошибки
#     print("except")
# finally:
#     # всегда
#     print("finally")



# names = ["vladimir", "aliya", "begimay", "erbol", "cholpon", "jamilya", "bakyt"]
# salaries =  [0,10000,20000,30000]

# print(names.index("erbol"))

# i = 0
# while i < len(salaries):
#     try:
#         salaries[i] *= 2
#     except TypeError:
#         salaries[i] = 0
#     i += 1
# print(salaries)


# i = 0
# while i < len(names):
#     try:
#         salaries[i] *= 2
#     except IndexError:
#         salaries.append(0)
#     i += 1
# print(salaries)
#
# print("ДЗ")
# a = 6
# b = 5
# c = 4
# if a == b == c:
#     print("РАВНОСТОРОННИЙ ТРЕУГОЛЬНИК")
# elif a == b or a == c or b == c:
#     print("РАВНОБЕДРЕННЫЙ ТРЕУГОЛЬНИК")
# else:
#     print("РАЗНОСТОРОННИЙ ТРЕУГОЛЬНИК")





# numbers = [2,4,6]
# i = 0
# while i < len(numbers):
#     if  numbers[i] % 2 == 0:
#         print("ЕСТЬ ЧЕТНОЕ")
#     else:
#         print("ЕСТЬ НЕЧЕТНОЕ")
#     i += 1

# a,b, c = 1,2,3
# if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
#     print("even")
# if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
#         print("odd")


# days = [1]
# distance = [10]
# y = 5
# i = 1
# j = 10
# while i < y:
#     i += 1
#     days.append(i)
#     j = j + 10/100
#     distance.append(j)
# print(days)
# print(distance)


x,y = 10,20

i = 1
while x <= y:
    x = x + (x * 0.1)
    i += 1
print(x,i)
