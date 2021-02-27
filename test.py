def creators(star, planet=8, alive=True):
    n = "ь есть!"
    if not alive:
        n = "и нет."
        return "Система звезды " + star + ".\nКоличество планет: " + str(planet) + ".\nЖизн" + n
