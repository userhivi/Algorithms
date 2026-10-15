name_org = input('Введите ваше имя: ')
print(f'Здравствуйте, {name_org}! Открываем зрительское голосование')

film_list = ['дюна', 'аватар', 'матрица', 'интерстеллар', 'шрек']
print('Фильмы в программе фестиваля:', end=' ')
print(*film_list, sep=', ')

vote = set()
dict = {film: 0 for film in film_list}
all_film_everyone = []

while True:
    film =[]
    correct_film = set()

    name = input('Имя зрителя (или "стоп", чтобы закончить): ')

    if name == 'стоп':
        break

    if name.lower() in vote:
        print(f'{name}, вы уже голосовали, второй голос не засчитан')
        continue
    vote.add(name.lower())

    film = input('Какие фильмы вам понравились (через запятую): ').lower().replace(' ','').split(',')

    for i in range(len(film)):
        if film[i].lower() in film_list:
            correct_film.add(film[i].lower())
            continue
        else:
            print(f'Фильма «{film[i]}» нет в программе, голос не засчитан')
    all_film_everyone.append(correct_film)

    for j in correct_film:
        dict[j] += 1
    print()


    print(f'Спасибо, {name}! Засчитано голосов: {len(correct_film)}')

mx_value = 0
print('Итоги голосования')
print(f'Проголосовало зрителей: {len(vote)}')

for key, value in dict.items():
    print(f'{key} - {value}')
    if value > mx_value:
        mx_value = value
        mx_key = key
print(f'Победитель: {mx_key} ({mx_value})')

if all_film_everyone:
    all_liked = set(film_list)
    for c in all_film_everyone:
        all_liked &= c
    if all_liked:
        print('Понравились всем: ', end='')
        print(*all_liked, sep=', ')
    else:
        print('Понравились всем: таких нет')

no_votes = []
for k in film_list:
    if dict[k] == 0:
        no_votes.append(k)
if no_votes:
    print('Не выбрал никто: ', end='')
    print(*no_votes, sep=', ')
else:
    print('Не выбрал никто: таких нет')

print(f'До свидания, {name_org}!')
