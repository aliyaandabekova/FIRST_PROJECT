# numbers = [1,2,3,4,5,6]
#
# for i in numbers:
#     print(i)


# numbers = [1,2,3,4,5,6]
#
# for i in range(100):
#     print(i)


# numbers = [1,2,3,4,5,6]
#
# numbers1 = range(100)
#
# print(type(numbers1))


# numbers = ["red","yellow","green","blue"]
#
# for i in range(len(numbers)):
#     print(i)

# numbers = ["red","yellow","green","blue"]
#
# for i in range(0,len(numbers),2):
#     print(i)

# for i in range(1,1000,2):
#     print(i)



# for i in range(0,1000,2):
#     print(i)


# import random
#
# random_numbers = random.sample(range(1,30),20)
# print(random_numbers)
# for i in random_numbers:
#     if i % 2 == 0:
#         print(i)

#
# import random
#
# random_numbers = random.sample(range(1,30),20)
#
# for i in range(len(random_numbers)):
#         print(random_numbers[i])

import random
#
# random_numbers = [1,2,3,4]
#
# for i in random_numbers:
#     print(i ** 2)

# random_numbers = [1, 2, 3, 4, "red", "99776", 6.3, 23.4, 30]
# for i in random_numbers:
#     if isinstance(i, int) or isinstance(i, float):
#         print(i ** 2)

# random_numbers = [1, 2, 3, 4, "red", "99776", [1, 2, 3], 6.3, 23.4, 30]
# sum = 0
# nested_sum = 0
# for i in random_numbers:
#     if isinstance(i,int) or isinstance(i,float):
#         sum += i
#     elif isinstance(i,list):
#         for j in i:
#             nested_sum += 1
# print(sum+nested_sum)


# string1 = "hello"
# print(string1[0])

# article = "fkrgjr njrjkkfk nrkkkfrkfkf mfkkfk krkrkrkrkrk; nfnkkdk kerkkrkkdlf kkfkkf Internet isfvii"
# ban_word = "Internet"
#
# if ban_word in article:
#     print("NOT OKAY")
# else:
#     print("OK")

# article = "fkrgjr njrjkkfk nrkkkfrkfkf mfkkfk krkrkrkrkrk; nfnkkdk kerkkrkkdlf kkfkkf Internet isfvii    "
# print(article.index("f"))

# article = article.capitalize()
# print(article)

# article = article.count("f")
# print(article)

# article = article.title()
# print(article)

# article = article.strip()
# print(article)

# article = article.startswith("fkrgjr")
# print(article)

# article = article.endswith("fkrgjr")
# print(article)

# print(article.find("f"))

# print(article.rindex("f"))
# print(article.rfind("f"))




article = "HELLo"

# print(article.isdigit())
print(article.isalpha())

# print(article.islower())
# print(article.isupper())

# article = article.lower()
# print(article)

# article = article.upper()
# print(article)



article = "Vasya nvirgiokfldll! Vasya jhgrufsjdk! Vasya jguiifjkld!"
# article = article.replace("Vasya","Petya")
# print(article)

# article = article.split()
# print(article)

# article = article.swapcase()
# print(article)

# article = article.replace("Vasya ","")
# print(article)


