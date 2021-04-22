# import random
# list = [["maksim"],[123456]]
#
# username = input()
# password = input()
# check_password = input("Check password: ")
#
# if password == check_password:
#     secret = random.randint(1000,9999)
#     print(secret)
#     secret_code = int(input())
#     if secret_code == secret:
#         list[0].append(username)
#         list[1].append(password)
#     else:
#         print("ВВЕДЕНЫЙ КОД НЕВЕРНЫЙ!")
# else:
#     print("Password dont match!")
#
# print(list)
# # print("Авторизация:")
# print("Please log in")
# count = 0
# tries = 0
# stop = None
# while tries < 3:
#     print(list[0])
#     count = 0
#     username = input()
#     password = input()
#     while count < len(list[0]):
#         print(count)
#
#         if username == list[0][count] and password == list[1][count]:
#             print("okay")
#             stop = "stop"
#             break
#         else:
#             print("not okay")
#         count += 1
#     if stop == "stop":
#         break
#     tries += 1



# import random
# list = [["maksim"],[123456]]
#
# username = input()
# password = input()
# check_password = input("Check password: ")
# if len(username) > 8 and len(password) >= 6:
#     if password == check_password:
#         secret = random.randint(1000,9999)
#         print(secret)
#         secret_code = int(input())
#         if secret_code == secret:
#             list[0].append(username)
#             list[1].append(password)
#         else:
#             print("ВВЕДЕНЫЙ КОД НЕВЕРНЫЙ!")
#     else:
#         print("Password dont match!")
#
# print(list)
# # print("Авторизация:")
# print("Please log in")
# count = 0
# tries = 0
# stop = None
# while tries < 3:
#     print(list[0])
#     count = 0
#     username = input()
#     password = input()
#     while count < len(list[0]):
#         print(count)
#
#         if username == list[0][count] and password == list[1][count]:
#             print("okay")
#             stop = "stop"
#             break
#         else:
#             print("not okay")
#         count += 1
#     if stop == "stop":
#         break
#     tries += 1

# numbers = [1 ,53, 4, 54 ,4 ,3 ,5]
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         print(numbers[i])
#     i += 1

# numbers = [1 ,53, 4, 54 ,4 ,3 ,5]
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 1:
#         print(numbers[i])
#     i += 1

# numbers = [1,7,6,5,8,9,10,12,14]
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))

# numbers = [1,7,6,5,8,9,10,12,14]
# max_number = 0
# i = 0
# while i < len(numbers):
#     if numbers[i] > max_number:
#         max_number = numbers[i]
#         print(max_number)
#     i += 1
# print(max_number)

# numbers = [1,7,6,5,8,9,10,12,14]
# i = 0
# summ = 0
# while i < len(numbers):
#     summ += numbers[i]
#     i += 1
# print(summ)

# numbers = [1,7,6,5,8,9,10,12,14]
# i = 0
# max_num = 0
# while i < len(numbers):
#     if numbers[i] > max_num:
#         max_num = numbers[i]
#     i += 1
# second = 0
# i = 0
# while i < len(numbers):
#     if numbers[i] > second and numbers[i] < max_num:
#         second = numbers[i]
#     i += 1
# print(max_num, second)

# print("HW")
# numbers = [1,7,6,5,8,9,9,9,10,12,14]
# prev_num = 0
# i = 0
# neighbors = 0
# while i < len(numbers):
#     if numbers[i] == prev_num:
#         neighbors += 1
#     prev_num = numbers[i]
#     i += 1
# print(neighbors)
# print("HW")

# numbers = [1,7,6,5,8,9,9,9,10,12,14,20,50]
# i = 0
# gt_ten = 0
# while i < len(numbers):
#     if numbers[i] > 10:
#         gt_ten += 1
#     i += 1
# print(gt_ten)

# numbers = [1,7,6,5,8,9,9,9,10,12,14,20,50,50]
# unik_numbers = []
# i = 0
# while i < len(numbers):
#     if numbers[i] not in unik_numbers:
#         unik_numbers.append(numbers[i])
#     i += 1
# print(unik_numbers)

# numbers = [1,7,6,5,8,9,9,9,10,12,14,20,50,2,3,50]
# unik_numbers = []
# i = 0
# while i < len(numbers):
#     if numbers[i] not in unik_numbers:
#         unik_numbers.append(numbers[i])
#     i += 1
# unik_numbers.sort()
# print(unik_numbers)



# # print("ДЗ")
# numbers = [1,7,6,5,8,9,9,9,10,12,14,20,25,50,2,3,50]
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 2
# print("способ2")
# print(list[::2])

# numbers = [1,7,6,5,8,9,9,9,10,12,14,65,20,100,25,50,2,3,50]
# # print(max(numbers))
# i = 0
# max_num = 0
# while i < len(numbers):
#     if numbers[i] > max_num:
#         max_num = numbers[i]
#     i += 1
# print(max_num)

# numbers = [1,7,6,5,8,9,9,9,10,12,14,65,20,100,25,50,2,3,50]
# numbers.reverse()
# print(numbers)
# print("способ2")
# print(numbers[::-1])
# print("способ3")
# numbers2 = []
# i = 0
# while i < len(numbers):
#     numbers2.insert(0,numbers[i])
#     i += 1
# print(numbers, numbers2)

# numbers = [101,7,6,5,1,8,9,9,9,10,12,14,65,20,100,25,50,1,2,3,50]
# i = 0
# max_number = 0
# while i < len(numbers):
#     if numbers[i] > max_number:
#         max_number = numbers[i]
#     i += 1
# print(max_number)
# print(numbers.index(max_number))


# numbers = [101,7,6,5,1,8,9,9,9,10,12,14,65,20,100,25,50,1,2,3,50]
# k = 13
# C = 5555
# i = 0
# numbers.insert(k,C)
# print(numbers)


# numbers = [101,7,6,5,1,8,9,9,9,10,12,14,65,20,100,25,50,1,2,3,50]
# k = 13
# del numbers[k]
# print(numbers)

# numbers = [101,-7,6,5,-1,8,9,9,-9,10,12,14,-65,20,100,25,-50,1,2,3,-50,0,-1]
# i = 0
# p_num = 0
# while i < len(numbers):
#     if numbers[i] >= 0:
#         p_num += 1
#     i += 1
# print("КОЛИЧЕСТВО ПОЛОЖИТЕЛЬНЫХ ЧИСЕЛ = ",p_num)

# numbers = [101,-7,6,5,-1,8,9,9,-9,10,12,14,-65,20,100,25,-50,1,2,3,-50,0,-1]
# i = 0
# o_num = 0
# while i < len(numbers):
#     if numbers[i] < 0:
#         o_num += 1
#     i += 1
# print("КОЛИЧЕСТВО ОТРИЦАТЕЛЬНЫХ ЧИСЕЛ = ",o_num)






