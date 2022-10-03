import game


def heroes():
    dante = game.Player()
    virgil = game.Player()
    nero = game.Player()
    dante.name = "Данте"
    virgil.name = "Вергилий"
    nero.name = "Неро"
    dante.weapon = "Меч спарты"
    virgil.weapon = "Ямато"
    nero.weapon = "Алая королева"
    dante.age = "44"
    virgil.age = "44"
    nero.age = "21"
    dante.guild = "Демон"
    virgil.guild = "Демон"
    nero.guild = "Полудемон"
    return dante, virgil, nero
