fio = input('Введите ваше ФИО: ').split()
print(f'Привет, {fio[1]}')

good_1 = input('Введите первый товар: ')
good_2 = input('Введите второй товар: ')
good_3 = input('Введите третий товар: ')
goods = [good_1, good_2, good_3]
print('Ваш список:', goods)
print('Товаров в списке:', len(goods))

goods.append('стакан')
print('Список после добавления подарка:',goods )

goods.sort()
print('Отсортированный список:', goods)
print(f'До свидания, {fio[1][0]}.{fio[2][0]}. {fio[0]}!')