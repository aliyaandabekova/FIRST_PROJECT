# def greetings(name):
#     name = "maksim"
#     print('Hello '+ name)
#
# def sum_of_3(a,b,c):
#     print(a+b+c)
# sum_of_3(1,2,3)


#
# def maximum_of_list(numbers):
#     return max(numbers)
#
# print(maximum_of_list([1,2,3,4,5]))
# print(maximum_of_list([20,30,40]))



def maximum_of_2():
    num1 = int(input())
    num2 = int(input())
    if num1 > num2:
        print(num1)
    else:
        print(num2)





"""
регистрация
"""
def register(username,password,confirm_password):
    if len(username) >= 8 and password == confirm_password and not password.isalpha():
        print("Успешно!")
        return username,password
    # else:
    #     print("Пароли не совпадают!")
try:
    username,password = register('HarryPotter', '1234', '1234')
    print('Регистрация завершена!')
except:
    print("Введите правильные данные!")





"""
авторизация
"""
def autorization():
    for i in range(3):

        saved_usename = input()
        saved_password = input()

        if saved_usename == username and saved_password == password:
            print("Вы успешно вошли в систему!")
            break
        else:
            print("Неверные данные!")
autorization()





