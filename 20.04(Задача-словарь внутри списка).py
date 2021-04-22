list1 = [1,2,3]
tuple1 = (1,2,3)
# students = [1,2,3,4]
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
           },
            {"name":"test1",
           "last_name":"Zinkovsky",
           "age":17,
           "scores":[1,2,3,4,5]  ,
           "hobbies":['play','programming','reading']
           },
            {"name": "test2",
             "last_name": "Zhumakova",
             "age": 18,
            "scores":[5,5,3,4,5],
             "hobbies": ['pubg', 'programming', 'reading','walking']
             },
            {"name": "test3",
             "last_name": "Andabekova",
             "age": 18,
                "scores":[1,4,3,1,2]  ,
             "hobbies": ['programming', 'reading','drawing']
             },
            {"name":"test4",
           "last_name":"Kaimova",
           "age":16,
            "scores":[5,2,4,4,5]  ,
           "hobbies":['pubg','programming','reading','anime',]
           },
            {"name":"test5",
           "last_name":"Asanaliev",
           "age":35,
            "scores":[4,2,4,4,5]  ,
           "hobbies":['play','programming','reading','footbal','history']
           },
            {"name":"test6",
           "last_name":"Surovkin",
           "age":22,
            "scores":[] ,
           "hobbies":['programming','reading','traveling','cycling']
           }
            ]

# Найти общее среднее арифметическое
# Найти среднее по студенту
# ****Найти стандартное отклонение (разница между максимальным средним и минимальным)****



student_avg = []
std = 0


for student in students:
    sum1 = 0
    for score in student['scores']:
        sum1 += score
    try:
        student_avg.append(sum1 / len(student['scores']))
    except ZeroDivisionError:
        student_avg.append(0)


avg_sum = sum(student_avg)
general_avg = avg_sum / len(student_avg)
k = 0
max_avg = 0
min_avg = 5
for stud_avg in student_avg:
    if stud_avg > max_avg:
        max_avg = stud_avg
    elif stud_avg < min_avg:
        min_avg = stud_avg
    k += 1

std = max_avg - min_avg

dict_loop = 0

import pprint

for student in students:
    student['avg'] = student_avg[dict_loop]
    dict_loop += 1
pprint.pprint(students)

