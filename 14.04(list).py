my_list = ["honda", "honda", "bmw", "mercedes", "bugatti"]
# print(my_list.index("honda"))
# print(my_list.index("honda", 1,4))
print(my_list.count("honda"))
# my_list.sort()
# my_list.pop()
# my_list.pop(2)
# print(my_list)


# copy_my_list = my_list.copy()
# print(copy_my_list)


# list1 = [1,2,3]
# list2 = list1
# del list1[0]
# print(list2)

# list1 = [1,2,3]
# list2 = list1.copy()
# del list1[0]
# print(list2)


# my_list1 = [6,2,5,3,1]
# my_list1.sort()
# print(my_list1)


# my_list = ["honda", "honda", "bmw", "mercedes", "bugatti"]
# my_list.append("volkswagen")
# print(my_list)

# my_list = ["honda", "honda", "bmw", "mercedes", "bugatti"]
# my_list.insert(1,"ford")
# print(my_list)

# my_list.clear()
# print(my_list)

# my_list = ["honda", "honda", "bmw", "mercedes", "bugatti"]
# extend_list = ["ford", "cevrolet"]
# my_list.extend(extend_list)
# print(my_list)

# my_list = ["honda", "honda", "bmw", "mercedes", "bugatti"]
# my_list.extend("hello")
# print(my_list)


# my_list = ["honda", "honda", "bmw", "mercedes", "bugatti"]
# my_list.remove("honda")
# print(my_list)

# my_list = ["honda", "honda", "bmw", "mercedes", "bugatti"]
# my_list.remove("yhuhjij")
# print(my_list)
# print("СПЕЦИАЛЬНОЕ С ОШИБКОЙ")


# my_list = ["honda", "honda", "bmw", "mercedes", "bugatti"]
# my_list.reverse()
# print(my_list)

# my_list = ["honda", "honda", "bmw", "mercedes", "bugatti"]
# print(my_list[::-1])


# print("ЗАДАЧИ")


# list = [[],[]]
#
# while True:

#     username = input()
#     if username == "1":
#         break
#     password = input()
#     check_password = input("Check password: ")
#     if password == check_password:
#         list[0].append(username)
#         list[1].append(password)
#     print(list)

# import random
# list = [[],[]]
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
# # print(list)
# # print("Авторизация:")
# username = input()
# password = input()
# if username in list[0] and password in list[1]:
#     print("ВЫ УСПЕШНО ВОШЛИ В СИСТЕМУ!")
# else:
#     print("ПРОВЕРЬТЕ ВВЕДЕНЫЕ ДАННЫЕ")

# import random
# list = [[],[]]
# username = input()
# password = input()
# check_password = input("Check password: ")
# if password == check_password:
#     secret = random.randint(1000,9999)
#     print(secret)
#     secret_code = int(input())
#     if secret_code == secret:
#         list[0].append(username)
#         list[1].append(password)
#     else:
#         print("НЕВЕРНЫЙ КОД!")
# else:
#     print("ПАРОЛИ НЕ СОВПАДАЮТ!")
# print(list)
# print("Авторизация:")
# i = 0
# while i < 3:
#     username = input()
#     password = input()
#     if username in list[0] and password in list[1]:
#         print("ВЫ УСПЕШНО ВОШЛИ В СИСТЕМУ!")
#         break
#     else:
#         print("ПРОВЕРЬТЕ ВВЕДЕНЫЕ ДАННЫЕ")
#     i += 1
# print("ПОВТОРИТЕ ПОПЫТКУ ПОЗЖЕ")




