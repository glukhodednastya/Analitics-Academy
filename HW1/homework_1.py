def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. \n'
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_umbrella():
    print(
        'Вдруг будет молнии удар⚡. \n'
        'В баре утке заказать хлеба 🍞 ломтик?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step3_bread()
    return step3_no_bread()

def step2_no_umbrella():
    print(
        'Его возьмет комар🦟. \n'
        'В баре утке заказать хлеба 🍞 ломтик?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step3_bread()
    return step3_no_bread()

def step3_bread():
    print('Это бога дар🎁')

def step3_no_bread():
    print('Она уже съела пять паст карбонар🍝')

if __name__ == '__main__':
    step1()
