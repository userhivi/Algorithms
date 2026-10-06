surname_coach = input('Введите вашу фамилию: ')
name_coach = input('Введите ваше имя: ')
print(f'Добро пожаловать, {name_coach}! Начинаем принимать зачёт')

n = int(input('Сколько спортсменов сдают зачёт: '))
k = int(input('Сколько подходов делает каждый: '))
list_surname = []
list_amount = []
cnt_amount = 0

for i in range(n):
    print(f'--- Спортсмен {i+1} ---')
    cnt = 0
    surname = input('Фамилия спортсмена: ')
    list_surname.append(surname)
    for j in range(k):
        result = int(input(f'Подход {j+1}: '))
        cnt += result
    list_amount.append(cnt)
    if cnt >= 30:
        cnt_amount += 1
        print(f'{surname}: всего {cnt} — норматив выполнен')
    else:
        print(f'{surname}: всего {cnt} — норматив не выполнен')

print('Итоговая таблица:')
for ind in range(len(list_surname)):
    print(f'{ind+1}. {list_surname[ind]} - {list_amount[ind]}')

print(f'Норматив выполнили: {cnt_amount} из {n}')
print(f'Всего подтягиваний группы: {sum(list_amount)}')
print(f'До свидания, {name_coach}!')



