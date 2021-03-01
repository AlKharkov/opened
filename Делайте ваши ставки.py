was = set()


def do_bet(horse, summ):
    global was
    if summ <= 0 or horse < 1 or horse > 10 or horse in was:
        print('Что-то пошло не так, попробуйте еще раз')
    else:
        print(f'Ваша ставка в размере {summ} на лошадь {horse} принята')
        was.add(horse)
