def creators(central_star, planets=8, alive=True):
    return f'Система звезды {central_star}.\nКоличество планет: {planets}.\nЖизнь есть!' if alive \
        else f'Система звезды {central_star}.\nКоличество планет: {planets}.\nЖизни нет.'
