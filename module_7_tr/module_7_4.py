# "Форматирование строк".
team1_num = 5  # количество участников первой команды Мастера кода
team2_num = 6  # количество участников второй команды Волшебники данных
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

# метод %
print("Соперничество двух команд - Мастера кода и Волшебники данных.\n"
      "В команде Мастера кода участников: %d!" % team1_num,"\n"
        "Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))
# метод format()
print("Команда Волшебники данных решила задач: {} !".format(score_2), "Мастера кода - {}".format(score_1))
print(
    "Волшебники данных решили задачи за {team2}с! Мастера кода - {team1}c.".format(team2=team2_time, team1=team1_time))
# метод f-строк
print(f'Команды решили {score_1} и {score_2} задач\n'
      f'Результат битвы: {challenge_result}\n'
      f'Сегодня было решено {score_1 + score_2} задач, в среднем по {time_avg} секунды на задачу!')
