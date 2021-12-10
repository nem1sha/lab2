import csv


def rating(file_reader):
    anime_list = []
    for row in file_reader:
        if float(row['Rating Score']) > float(answers['Rating Score']) or answers['Rating Score'] == '':
            anime_list.append(row['Name'])
    return anime_list


def votes(file_reader):
    anime_list = []
    for row in file_reader:
        if float(row['Number Votes']) > float(answers['Number Votes']) or answers['Number Votes'] == '':
            anime_list.append(row['Name'])
    return anime_list


def genre(file_reader):
    anime_list = []
    for row in file_reader:
        answer = answers['Tags']
        series = row['Tags']
        for i in range(len(series)):
            for j in range(len(answer)):
                if series[i] == answer[j] or answer[j] == '':
                    anime_list.append(row['Name'])
    return anime_list


def content(file_reader):
    anime_list = []
    for row in file_reader:
        series = row['Content Warning']
        answer = answers['Content Warning']
        for i in range(len(series)):
            for j in range(len(answer)):
                if series[i] == answer[j] or answer[j] == '' or (series[i] == 'Unknown' and answer[j] == ''):
                    anime_list.append(row['Name'])
    return anime_list


def filter(file_reader):
    anime_list = []
    for row in file_reader:
        k = 0
        for i in ['Type', 'Episodes', 'StartYear', 'EndYear', 'Season', 'Studios']:
            if row[i] == answers[i] or answers[i] == '' or (row[i] == 'Unknown' and answers[i] == ''):
                k += 1
        if k == 6:
            anime_list.append(row['Name'])
    return anime_list


def finish(a, b, c, d, e):
    top_anime = list(set(a) & set(b) & set(c) & set(d) & set(e))
    return top_anime


keys = ['Rating Score', 'Number Votes', 'Tags',
        'Content Warning', 'Type', 'Episodes',
        'StartYear', 'EndYear', 'Season', 'Studios']

questions = ['Какой желаемый минимальный рейтинг для вас? ',
             'Какое минимальное количество голосов? ',
             'Какой(-ие) желаемый(-ые) жанр(ы)? ',
             'Какие предупреждения стоит исключить? ',
             'Какой формат показа (TV, Web, Movie, etc)? ',
             'Какое количество эпизодов? ',
             'Какой год начала показа? ',
             'Какой год окончания? ',
             'Какое количество сезонов? ',
             'Какая студия? ']

end_question = '>>>Если вам это не важно, нажмите "ENTER"'

response = []

for question in questions:
    print(question + '\n' + end_question)
    response.append(input())

answers = dict(zip(keys, response))


with open('anime.csv', 'r', encoding='utf-8') as file:
    file_reader = csv.DictReader(file, delimiter=",")

rating_score = rating(file_reader)
number_votes = votes(file_reader)
tags = genre(file_reader)
content_warning = content(file_reader)
others = filter(file_reader)

top_anime = finish(rating_score, number_votes, tags, content_warning, others)

with open('final.txt', 'w', encoding='utf-8') as file:
    for name in top_anime:
        file.write(name + '\n')


print('Отчёт по вашим критериям составлен в файле "final.txt".')