surname_commission = input("Введите вашу фамилию: ")
name_commission = input("Введите ваше имя: ")
print(f'Добро пожаловать, {name_commission}! Начинаем приём заявок')

cnt_all = 0
cnt_approved = 0
while True:
    surname = input('Фамилия абитуриента (или "завершить", чтобы закончить приём): ')
    if surname == 'завершить':
        break
    score = int(input('Балл абитуриента: '))
    is_olympic = input('Есть ли диплом олимпиады? (да/нет): ').lower()
    if (score >= 220) or (is_olympic == 'да' and score >= 180):
        cnt_approved += 1
        print(f'{surname}: заявка одобрена')
    else:
        print(f'{surname}: заявка отклонена')
    cnt_all += 1

print(f'Рассмотрено абитуриентов: {cnt_all}')
print(f'Зачислено: {cnt_approved}')
print(f'До свидания, {surname_commission}!')