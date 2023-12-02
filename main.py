from random import randint


def attack(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return f'{char_name} нанёс урон противнику равный {5 + randint(3,5)}'
    elif char_class == 'mage':
        return f'{char_name} нанёс урон противнику равный {5 + randint(5,10)}'
    elif char_class == 'healer':
        return f'{char_name} нанёс урон противнику равный {5 + randint(-3,-1)}'


def defence(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return f'{char_name} блокировал (10 + randint(5, 10)) урона'
    elif char_class == 'mage':
        return f'{char_name} блокировал (10 + randint(-2, 2)) урона'
    elif char_class == 'healer':
        return f'{char_name} блокировал (10 + randint(2, 5)) урона'


def special(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return f'{char_name}'
        f'применил специальное умение «Выносливость {80+25}»'
    elif char_class == 'mage':
        return f'{char_name}'
        f'применил специальное умение «Атака {5 + 40}»'
    elif char_class == 'healer':
        return f'{char_name}'
        f'применил специальное умение «Защита {10 + 30}»'


def start_training(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    elif char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    elif char_class == 'heale':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: ')
    print('attack — чтобы атаковать противника,')
    print('defence — чтобы блокировать атаку противника')
    print('или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        elif cmd == 'defence':
            print(defence(char_name, char_class))
        elif cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        print('Введи название персонажа, за которого хочешь играть:')
        print('Воитель — warrior, Маг — mage, Лекарь — healer: ')
        char_class = input('Введи назване персонажа')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя.')
            print('Сильный, выносливый и отважный.')
        elif char_class == 'mage':
            print('Маг — находчивый воин дальнего боя.')
            print('Обладает высоким интеллектом.')
        elif char_class == 'healer':
            print('Лекарь — могущественный заклинатель.')
            print('Черпает силы из природы, веры и духов.')
            print('Нажми (Y), чтобы подтвердить выбор')
            print('Любую другую кнопку, чтобы выбрать другого персонажа ')
            approve_choice = input('Подтверди выбор').lower()
    return char_class


def main() -> str:
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print('Здравствуй, ' + char_name + '!')
    print('Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))


main()
