"""Кейс-задача №1: программа для стилистического преобразования чисел.

Запрашивает у пользователя дату рождения, определяет день недели,
проверяет год на високосность, считает возраст и печатает дату
в консоль в виде цифр, нарисованных звёздочками (*), как на
электронном табло.
"""

from datetime import date

WEEKDAYS = [
    'Понедельник', 'Вторник', 'Среда', 'Четверг',
    'Пятница', 'Суббота', 'Воскресенье',
]

DIGITS = {
    '0': [' *** ', '*   *', '*   *', '*   *', ' *** '],
    '1': ['  *  ', ' **  ', '  *  ', '  *  ', ' *** '],
    '2': [' *** ', '*   *', '  ** ', ' *   ', '*****'],
    '3': [' *** ', '*   *', '  ** ', '*   *', ' *** '],
    '4': ['*   *', '*   *', '*****', '    *', '    *'],
    '5': ['*****', '*    ', ' *** ', '    *', '**** '],
    '6': [' *** ', '*    ', '**** ', '*   *', ' *** '],
    '7': ['*****', '    *', '   * ', '  *  ', '  *  '],
    '8': [' *** ', '*   *', ' *** ', '*   *', ' *** '],
    '9': [' *** ', '*   *', ' ****', '    *', ' *** '],
    '.': ['     ', '     ', '     ', '     ', '  *  '],
}


def read_birthday():
    """Последовательно запрашивает день, месяц и год рождения."""
    while True:
        try:
            day = int(input('Введите день рождения: '))
            month = int(input('Введите месяц рождения: '))
            year = int(input('Введите год рождения: '))
            birthday = date(year, month, day)
        except ValueError as exc:
            print(f'Некорректный ввод: {exc}. Попробуйте снова.\n')
            continue
        if birthday > date.today():
            print('Дата рождения не может быть в будущем. Попробуйте снова.\n')
            continue
        return birthday


def get_day_of_week(birthday):
    """Возвращает название дня недели, на который выпала дата."""
    return WEEKDAYS[birthday.weekday()]


def is_leap_year(year):
    """Определяет, является ли год високосным."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def calculate_age(birthday):
    """Считает полных лет пользователю на текущий момент."""
    today = date.today()
    age = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1
    return age


def pluralize_years(age):
    last_two = age % 100
    last = last_two % 10
    if 11 <= last_two <= 14:
        return 'лет'
    if last == 1:
        return 'год'
    if 2 <= last <= 4:
        return 'года'
    return 'лет'


def print_date_as_stars(birthday):
    """Печатает дату в формате дд.мм.гггг звёздочками, как на табло."""
    date_str = birthday.strftime('%d.%m.%Y')
    rows = ['' for _ in range(5)]
    for char in date_str:
        pattern = DIGITS[char]
        for i in range(5):
            rows[i] += pattern[i] + '  '
    print('\n'.join(rows))


def main():
    birthday = read_birthday()

    print(f'\nДень недели: {get_day_of_week(birthday)}')

    leap = is_leap_year(birthday.year)
    print(f'{birthday.year} — високосный год: {"да" if leap else "нет"}')

    age = calculate_age(birthday)
    print(f'Возраст: {age} {pluralize_years(age)}')

    print('\nВаша дата рождения на электронном табло:')
    print_date_as_stars(birthday)


if __name__ == '__main__':
    main()
