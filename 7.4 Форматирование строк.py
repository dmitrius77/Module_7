team1 = 'Мастера кода'
team1_num = 5
team2 = 'Волшебники данных'
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
#challenge_result = 'Победа команды Волшебники данных!'

print('В команде %s участников: %s,' % ('Мастера кода', 5))
print('Итого сегодня в командах участников: %s' %(team1_num), 'и', (team2_num))
print('Итого сегодня в командах участников: %s' %('5'), 'и', ('6'))

print("Команда Волшебники данных решила задач: {}".format ("42!"))
print("Волшебники данных решили задачи за {}".format(team2_time), 'c!')

print(f'Команды решили {score_1} и {score_2} задач.')
print(f"Сегодня было решено {score_1 + score_2} задач, в среднем по {(team1_time + team2_time) / (tasks_total)} секунды на задачу!.")

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(result)