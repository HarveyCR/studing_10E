class Player:
    def __init__(self):
        self.name = "Main_Hero"
        self.age = "21"
        self.guild = "assassin"
        self.existence = "30"
        self.weapon = "sword"


class Enemy:
    def __init__(self):
        self.name = "Proto_Angelo"
        self.age = "6528"
        self.guild = "knight"
        self.existence = "500"
        self.weapon = "sword"


class Treasure:
    def __init__(self):
        self.count = "500"
        self.value = "rare"


def main():
    dante = Player()
    virgil = Player()
    dante.name = "Данте"
    virgil.name = "Вергилий"
    dante.weapon = "soparda_sword"
    virgil.weapon = "yamato"
    print(dante.name, virgil.name)


if __name__ == '__main__':
    main()
