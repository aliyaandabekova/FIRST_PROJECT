"""
Дан сложный список категорий товаров ( словарей) для каждой категории существует
соответствующий список словарей каждого обьекта товара конкретной категории.
Требуется узнать:
1.Самую дорогую категорию товаров.
2. Самую популярную категорию товаров
3. Товар с наименьшей и наибольшей стоимостью.
Каждый ответ выводить в таком формате: {
‘most_popular_category’:’total_popularity’
}
"""

import pprint
data = [
    {'dress':[
                {'name':'louis vuitton',
                'popularity':500,
                 'price':1000
                },
                {'name':'versace',
                'popularity':21,
                 'price':888
                },
                {'name':'supreme',
                'popularity':57,
                 'price':765
                },
    ]
    },
    {'jeans':[
                {'name':'adidas',
                'popularity':42,
                 'price':2300
                },
                {'name':'armani',
                'popularity':678,
                 'price':110
                },
                {'name':'casio',
                'popularity':230,
                 'price':3000
                },
    ]
    },
    {'t-shirt':[
                {'name':'tom ford',
                'popularity':999,
                 'price':5000
                },
                {'name':'lacoste',
                'popularity':777,
                 'price':230
                },
                {'name':'luxury',
                'popularity':876,
                 'price':2300
                },
    ]
    }
]

# # pprint.pprint(data)
# pprint.pprint(data[0]['dress'][0]['price'])


# list1 = ['dress', 'jeans','t-shirt']
#
# i = 0
# category_price = {}
#
# for category in data:
#     category_sum = 0
#     key = list1[i]
#     category_value = category[key]
#     for product in category_value:
#         category_sum += product['price']
#     # print(category_sum)
#     category_price[key] = category_sum
#     i += 1
# # print(category_price)
# print(max(category_price.values()),category_price)



# list2 = ['dress', 'jeans','t-shirt']
# i = 0
# category_popularity = {}
# for category in data:
#     category_popularity_sum = 0
#     key = list2[i]
#     category_popularity_value = category[key]
#     for product in category_popularity_value:
#         category_popularity_sum += product['popularity']
#     category_popularity[key] = category_popularity_sum
#     i += 1
# print(category_popularity)
# print(max(category_popularity.values()))

# list1 = ['dress', 'jeans','t-shirt']
#
# i = 0
# j = 0
# for category in data:
#     for price in category:
#         print(dress['price'])
#         i += 1
#     j += 1


list1 = ['dress', 'jeans','t-shirt']
i = 0
price_list = []

for category in data:
    # print(category)
    key = list1[i]
    value = category[key]
    # print(value)
    for product in value:
        price_list.append(product['price'])
    i += 1
print(price_list)
print(max(price_list),min(price_list) )


file1 = open('test.txt','w')
file1.write(str(max(price_list)))























