from decouple import config
import requests
import sys
import datetime
"""
https://api.github.com/repos/ryanheise/audio_service
Системные параметры (sys.argv) username repository start_date end_date
1. Вывести все коммиты в данном промежутке времени
2. Вывести все pull requests созданные в данном промежутке времени (key:created_at)
3. Вывести все issues созданные в данном промежутке времени (key:created_at)
"""


def send_request(url:str):
    """

    :param url: Ссылка на сайтб откуда будем брать данные
    :return: Данные в виде словарей
    """
    r = requests.get(url,headers={'Authorization': config('token')})
    return r.json()


def to_datetime(date:str):
    """

    :param date: Дата тип данных строка
    :return: Дата тип данных datetime
    """
    if 'T' not in date:
        # Для даты , которую мы  сами задаем в формате "год-месяц-день"
        result_date = datetime.datetime.strptime(date,'%Y-%m-%d')
        result_date = datetime.date(result_date.year,result_date.month,result_date.day)
    else:
        # Для даты , которую получаем из сайта в формате "год-месяц-день часы:минуты:секунды"
        result_date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
        result_date = datetime.date(result_date.year, result_date.month, result_date.day)
    return result_date

url = 'https://api.github.com/repos/ryanheise/audio_service'
def get_commits(url:str,start_date:str,end_date:str):
    """

    :param url: Ссылка для данных о коммитах
    :param start_date: Начало периода
    :param end_date: Конец периода
    :return: Все коммиты в данном промежутке времени. Самые активные пользователи.
    """
    commits = []
    active_users = {}
    list_of_authors = []
    url = url + '/commits?page=1&per_page=100'
    start_date = to_datetime(start_date)
    end_date = to_datetime(end_date)
    responses = send_request(url)
    for response in responses:
        # Перебираем список со словарями.
        commit_date = to_datetime(response['commit']['author']['date'])
        commit = response['commit']['message']
        author = response['author']['login']
        if start_date<=commit_date<=end_date:
            # Условие , что рассматриваемый коммит был написан в данном промежутке времени.
            commits.append(commit)
            if author not in list_of_authors:
                # Добавляем авторов коммитов, в новый пустой список, с условием , что этого автора еще нет в данном списке
                list_of_authors.append(author)
    for comitter in list_of_authors:
        # Перебираем список авторов коммитов.
        commit_count = 0
        for response in responses:
            # Перебираем список со словарями.
            if comitter == response['author']['login']:
                # Если автор из нашего списка совпадает с автором рассматриваемого коммита, увеличиваем счетчик.
                commit_count += 1
        active_users[comitter] = commit_count
    print(active_users)
    return commits,active_users

def get_pulls(url:str,start_date:str,end_date:str):
    """

        :param url: Ссылка для данных о pulls
        :param start_date: Начало периода
        :param end_date: Конец периода
        :return: Все pull requests созданные в данном промежутке времени (key:created_at)
        """
    pulls = []
    url = url + '/pulls'
    start_date = to_datetime(start_date)
    end_date = to_datetime(end_date)
    responses = send_request(url)
    for response in responses:
        # Перебираем список со словарями.
        pulls_date = to_datetime(response['created_at'])
        pulls_title = response['title']
        if start_date<=pulls_date<=end_date:
            # Условие , что рассматриваемый pull request был создан в данном промежутке времени.
            pulls.append(pulls_title)
    return pulls

def get_issues(url:str,start_date:str,end_date:str):
    """

        :param url: Ссылка для данных о issues
        :param start_date: Начало периода
        :param end_date: Конец периода
        :return: Все issues созданные в данном промежутке времени (key:created_at)
        """
    issues = []
    url = url + '/issues'
    start_date = to_datetime(start_date)
    end_date = to_datetime(end_date)
    responses = send_request(url)
    for response in responses:
        # Перебираем список со словарями.
        issues_date = to_datetime(response['created_at'])
        issues_title = response['title']
        if start_date<=issues_date<=end_date:
            # Условие , что рассматриваемый issues был создан в данном промежутке времени.
            issues.append(issues_title)
    return issues

def main():
    """

    :return: Запуск всех функций.
    """
    github_username = sys.argv[1]
    github_repository = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}'.format(github_username,github_repository)
    start_date = sys.argv[3]
    end_date = sys.argv[4]
    print(get_commits(url, start_date,end_date))
    print(get_pulls(url, start_date, end_date))
    print(get_issues(url, start_date, end_date))
main()


