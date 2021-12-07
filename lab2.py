import csv

def rating(file_reader):
    animes = []
    for row in file_reader:
        if float(row['Rating Score']) > float(answers['Rating Score']) or answers['Rating Score'] == '':
            animes.append(row['Name'])
    return animes

def votes(file_reader):
    animes = []
    for row in file_reader:
        if float(row['Number Votes']) > float(answers['Number Votes']) or answers['Number Votes'] == '':
            animes.append(row['Name'])
    return animes

def genre(file_reader):
    animes = []
    for row in file_reader:
        t = answers['Tags']
        r = row['Tags']
        for i in range(len(r)):
            for j in range(len(t)):
                if r[i] == t[j] or t[j] == '':
                    animes.append(row['Name'])
    return animes

def content(file_reader):
    animes = []
    for row in file_reader:
        r = row['Content Warning']
        c = answers['Content Warning']
        for i in range(len(r)):
            for j in range(len(c)):
                if r[i] == c[j] or c[j] == '' or (r[i] == 'Unknown' and c[j] == ''):
                    animes.append(row['Name'])
    return animes

def filter(file_reader):
    animes = []
    for row in file_reader:
        k = 0
        for i in ['Type', 'Episodes', 'StartYear', 'EndYear', 'Season', 'Studios']:
            if row[i] == answers[i] or answers[i] == '' or (row[i] == 'Unknown' and answers[i] == ''):
                k += 1
        if k == 6:
            animes.append(row['Name'])
    return animes

def finish(a, b, c, d, e):
    final = []
    for f in a:
        for g in b:
            for h in c:
                for i in d:
                    for j in e:
                        if a[f] == b [g]:
                            if b[g] == c[h]:
                                if c[h] == d[i]:
                                    if d[i] == e[j]:
                                        final.append(a[f])
    return final



answers = {
    'Rating Score': '',
    'Number Votes': '',
    'Tags': '',
    'Content Warning': '',
    'Type': '',
    'Episodes': '',
    'StartYear': '',
    'EndYear': '',
    'Season': '',
    'Studios': ''
            }
#1
print('Введите желаемый минимальный рейтинг (если вам это не важно, нажмите "ENTER"): ')
answers['Rating Score'] = input()

#2
print('Укажите минимальное количество голосов (если вам это не важно, нажмите "ENTER"):')
answers['Number Votes'] = input()

#3
print('Укажите желаемый(-ые) жанр(ы) (если вам это не важно, нажмите "ENTER"):')
answers['Tags'] = input()

#4
print('Какие предупреждения стоит исключить?(если вам это не важно, нажмите "ENTER")')
answers['Content Warning'] = input()

#5
print('Формат показа (TV, Web, Movie, etc) (если вам это не важно, нажмите "ENTER"):')
answers['Type'] = input()

#6
print('Количество эпизодов (если вам это не важно, нажмите "ENTER"):')
answers['Episodes'] = input()

#7
print('Год начала показа (если вам это не важно, нажмите "ENTER"):')
answers['StartYear'] = input()

#8
print('Год окончания (если вам это не важно, нажмите "ENTER"):')
answers['EndYear'] = input()

#9
print('Сезоны (если вам это не важно, нажмите "ENTER"):')
answers['Season'] = input()

#10
print('Студия (если вам это не важно, нажмите "ENTER"):')
answers['Studios'] = input()

with open('anime.csv', 'r', encoding='utf-8') as file:
    file_reader = csv.DictReader(file, delimiter=",")

rating_score = rating(file_reader)
number_votes = votes(file_reader)
tags = genre(file_reader)
content_warning = content(file_reader)
others = filter(file_reader)

final = finish(rating_score, number_votes, tags, content_warning, others)

with open('final.txt', 'w', encoding='utf-8') as file:
    for name in final:
        file.write(name + '\n')
