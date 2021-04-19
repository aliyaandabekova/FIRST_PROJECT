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



names = ["vladimir", "aliya", "begimay", "erbol", "cholpon", "jamilya", "bakyt"]
salaries =  [0,10000,20000,30000]

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
