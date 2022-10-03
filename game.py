import heroes
import enemies


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
    print("Главные герои")
    dante, virgil, nero = heroes.heroes()
    print(f"    * Имя - {dante.name} | Возраст - {dante.age} | Оружие - {dante.weapon}")
    print(f"    * Имя - {virgil.name} | Возраст - {virgil.age} | Оружие - {virgil.weapon}")
    print(f"    * Имя - {nero.name} | Возраст - {nero.age} | Оружие - {nero.weapon}")

    print("Враги")
    empuza, empuzes_queen, fury, Proto_Angelo = enemies.enemies()
    print(f"    * Имя - {empuza.name}| класс - {empuza.guild} | Возраст - {empuza.age} | Оружие - {empuza.weapon}")
    print(
        f"    * Имя - {empuzes_queen.name}| класс - {empuzes_queen.guild} | Возраст - {empuzes_queen.age} | Оружие - {empuzes_queen.weapon}")
    print(f"    * Имя - {fury.name}| класс - {fury.guild} | Возраст - {fury.age} | Оружие - {fury.weapon}")
    print(
        f"    * Имя - {Proto_Angelo.name}| класс - {Proto_Angelo.guild} | Возраст - {Proto_Angelo.age} | Оружие - {Proto_Angelo.weapon}")


if __name__ == '__main__':
    main()
