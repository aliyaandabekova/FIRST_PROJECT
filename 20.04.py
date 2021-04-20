# dict1 = {1,2,3,4,5,2,4,3} # set-множества
# print(dict1)
# student = {"name":"Vova",
#            "last_name":"Zinkovsky",
#            "age":17,
#            "hobbies":["play","programming","reading"]
#            }

# student["hobbies"].append("english")
# student["hobbies"].extend(["football","finance"])
# print(student["hobbies"])


# print(student["hobbies"][0])


# name = student.pop("name")
# print(student)

#
# for i in student:
#     print(student[i])




# students = [{"name":"Vova",
#            "last_name":"Zinkovsky",
#            "age":17,
#            "scores":[1,2,3,4,5]  ,
#            "hobbies":['play','programming','reading']
#            },
#             {"name": "Begimai",
#              "last_name": "Zhumakova",
#              "age": 18,
#             "scores":[5,5,3,4,5],
#              "hobbies": ['pubg', 'programming', 'reading','walking']
#              },
#             {"name": "Aliya",
#              "last_name": "Andabekova",
#              "age": 18,
#                 "scores":[1,4,3,1,2]  ,
#              "hobbies": ['programming', 'reading','drawing']
#              },
#             {"name":"Cholpon",
#            "last_name":"Kaimova",
#            "age":16,
#             "scores":[5,2,4,4,5]  ,
#            "hobbies":['pubg','programming','reading','anime',]
#            },
#             {"name":"Bakyt",
#            "last_name":"Asanaliev",
#            "age":35,
#             "scores":[4,2,4,4,5]  ,
#            "hobbies":['play','programming','reading','footbal','history']
#            },
#             {"name":"Maksim",
#            "last_name":"Surovkin",
#            "age":22,
#             "scores":[1,1,1,1,1] ,
#            "hobbies":['programming','reading','traveling','cycling']
#            }
#             ]
#
# student_avg = []
# result = 0
# max = 0
# min = 5
# for student in students:
#     # print(student["scores"])
#     sum = 0
#
#     for score in student["scores"]:
#         sum += score
#
#     stud_avg = sum / len(student["scores"])
#
#     if stud_avg >= max:
#         max = stud_avg
#     if stud_avg <= min:
#         min = stud_avg
#
#     result += stud_avg
#     student_avg.append(stud_avg)
#
# # print(result)
# gen_avg = result / 6
# print("Среднее арифметическое студентов = ",student_avg)
# print("Общее среднее арифметическое = ",gen_avg)
# std = max - min
# print("Стандартное отклонение = ",std)


# лучшее решение
students = [{"name":"Vova",
           "last_name":"Zinkovsky",
           "age":17,
           "scores":[1,2,3,4,5]  ,
           "hobbies":['play','programming','reading']
           },
            {"name": "Begimai",
             "last_name": "Zhumakova",
             "age": 18,
            "scores":[5,5,3,4,5],
             "hobbies": ['pubg', 'programming', 'reading','walking']
             },
            {"name": "Aliya",
             "last_name": "Andabekova",
             "age": 18,
                "scores":[1,4,3,1,2]  ,
             "hobbies": ['programming', 'reading','drawing']
             },
            {"name":"Cholpon",
           "last_name":"Kaimova",
           "age":16,
            "scores":[5,2,4,4,5]  ,
           "hobbies":['pubg','programming','reading','anime',]
           },
            {"name":"Bakyt",
           "last_name":"Asanaliev",
           "age":35,
            "scores":[4,2,4,4,5]  ,
           "hobbies":['play','programming','reading','footbal','history']
           },
            {"name":"Maksim",
           "last_name":"Surovkin",
           "age":22,
            "scores":[1,1,1,1,1] ,
           "hobbies":['programming','reading','traveling','cycling']
           }
            ]
student_avg = []
std = 0

for student in students:
    sum1 = 0
    for score in student["scores"]:
        sum1 += score


avg_sum = sum(student_avg)
general_avg = avg_sum / len(student_avg)





