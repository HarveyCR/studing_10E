import treasure, enemies, Nero_story, Dante_story, Vergil_story, heroes


class Player:
    def __init__(self):
        self.name = "Main_Hero"
        self.age = "21"
        self.guild = "assassin"
        self.existence = "10"
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
        self.kind = "blood_coins"
        self.ability = "nothing"


def main():
    print("Выбиртите героя")
    # print("Главные герои")
    dante, virgil, nero = heroes.heroes()
    print(
        f"    1. Имя - {dante.name} | Возраст - {dante.age} | Оружие - {dante.weapon}| Происхождение - {dante.guild}| Количество ХП - {dante.existence}")
    print(
        f"    2. Имя - {virgil.name} | Возраст - {virgil.age} | Оружие - {virgil.weapon}| Происхождение - {virgil.guild}| Количество ХП - {virgil.existence}")
    print(
        f"    3. Имя - {nero.name} | Возраст - {nero.age} | Оружие - {nero.weapon}| Происхождение - {nero.guild}| Количество ХП - {nero.existence}")

    # print("Враги")
    # empuza, empuzes_queen, fury, Proto_Angelo = enemies.enemies()
    # print(f"    * Имя - {empuza.name}| класс - {empuza.guild} | Возраст - {empuza.age} | Оружие - {empuza.weapon}")
    # print(
    #     f"    * Имя - {empuzes_queen.name}| класс - {empuzes_queen.guild} | Возраст - {empuzes_queen.age} | Оружие - {empuzes_queen.weapon}")
    # print(f"    * Имя - {fury.name}| класс - {fury.guild} | Возраст - {fury.age} | Оружие - {fury.weapon}")
    # print(
    #     f"    * Имя - {Proto_Angelo.name}| класс - {Proto_Angelo.guild} | Возраст - {Proto_Angelo.age} | Оружие - {Proto_Angelo.weapon}")
    #
    # print("Награды")
    # blood_coins, golden_spheres, purple_spheres, blue_spheres = treasure.treasure()
    # print(f"    * Название - {blood_coins.kind}| способность - {blood_coins.ability}")
    # print(
    #     f"    * Название - {golden_spheres.kind}| способность - {golden_spheres.ability}")
    # print(
    #     f"    * Название - {purple_spheres.kind}| способность - {purple_spheres.ability} ")
    # print(
    #     f"    * Название - {blue_spheres.kind}| способность - {blue_spheres.ability} ")
    a = input()
    if "1" in a:
        Dante_story.main()
    elif "2" in a:
        Vergil_story.main()
    elif "3" in a:
        Nero_story.main()
    else:
        print("Вы выбрали несужествуюзий вариант")


if __name__ == '__main__':
    main()
