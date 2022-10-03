import game


def heroes():
    dante = game.Player()
    virgil = game.Player()
    nero = game.Player()
    dante.name = "Данте"
    virgil.name = "Вергилий"
    nero.name = "Неро"
    dante.weapon = "sparda_sword"
    virgil.weapon = "yamato"
    nero.weapon = "scarlet_qween"
    dante.age = "44"
    virgil.age = "44"
    nero.age = "21"
    dante.guild = "demon"
    virgil.guild = "demon"
    nero.guild = "half-demon"
    return dante, virgil, nero
