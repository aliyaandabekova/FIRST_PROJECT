# products1 = {'potato':2, 'tomato':3, 'pineapple':4}
# products2 = {'apple':22, 'carrot':33, 'melon':44}
#
# products1.update(products2)
# print(products1)
#
#
#
# """
# 2 словаря с одинаковыми переменными
# """
# dict1 = {'a':1, 'b':2,'c':3}
# dict2 = {'a':68439,'g':4}
# dict1.update(dict2)
# print(dict1)


users = [{'id':1,'user': 'digital', },
         {'id':2,'user': 'maksim', },
         {'id':3,'user': 'vova', },
         {'id':4,'user': 'begimai', },
         {'id':5,'user': 'aliya', },
         {'id':6,'user': 'bakyt',},
         {'id':7,'user': 'chingiz', },
         {'id':8,'user': 'jamilya',},
         {'id':9,'user': 'cholpon', },
         {'id':10,'user': 'erbol', }
         ]
posts = [{'id':1,'text':'hiring','status':'sponsored','keyword':'nic1'},
         {'id':2,'text':'text1','status':'pub'},
         {'id':3,'text':'text2','status':'pub'},
         {'id':4,'text':'text3','status':'pub'},
         {'id':5,'text':'text4','status':'pub'},
         {'id':6,'text':'text5','status':'pub'},
         {'id':7,'text':'Canada immigration','status':'sponsored','keyword':'interested!'}]
comments = [{'id':1,'user_id':1,'post_id':1,'comment':'This is not nic1'},
            {'id':2,'user_id':2,'post_id':1,'comment':'Hello this is nic1'},
            {'id':3,'user_id':3,'post_id':2,'comment':'looking good!'},
            {'id':4,'user_id':4,'post_id':2,'comment':'awesome!'},
            {'id':5,'user_id':5,'post_id':2,'comment':'LGTM'},
            {'id':6,'user_id':6,'post_id':3,'comment':'here we go!'},
            {'id':7,'user_id':6,'post_id':4,'comment':'not ok'},
            {'id':8,'user_id':6,'post_id':7,'comment':'interested!'},
            {'id':9,'user_id':6,'post_id':7,'comment':'woohoo!'},
            {'id':10,'user_id':6,'post_id':7,'comment':'interested!'}]
"""
1. Нужно найти все posts со статусом sponsored!
2. Найти комментарии к posts sponsored
3. Среди найденных комментариев найти те что содержат keyword из posts
"""


sortpost = []
def sort_post(posts):
    """

    :param posts: Список постов
    :return: Отфильтрованный список постов
    """
    for post in posts:
        if post['status'] == 'sponsored':
            # print(post)
            sortpost.append(post)
    return sortpost
posts = sort_post(posts)
# print(sortpost)

list_of_comment = []
def comment_to_post(posts, comments):
    """

    :param posts: Отфильтрованный писок постов
    :param comments: Список коментариев
    :return: Обновленный список постов с коментариями
    """
    for post in posts:
        post['comment'] = []
        for comment in comments:
            if post['id'] == comment['post_id']:
                post['comment'].append(comment['comment'])
        # print(post)
    return posts
posts = comment_to_post(posts,comments)
# print(posts)


def finally_list(posts):
    """

    :param posts: Список постов
    :return: Список постов с keyword в комментариях
    """
    for post in posts:
        for com in post['comment']:
            print(post['keyword'])
            if post['keyword'] not in com:
                post['comment'].remove(com)
    return posts
posts = finally_list(posts)
print(posts)

















