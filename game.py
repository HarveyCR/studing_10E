class Player:
    def __init__(self):
        self.name = "Main Hero"
        self.age = "21"
        self.guild = "assassin"
        self.existence = "30"


class Enemy:
    def __init__(self):
        self.name = "Proto Angelo"
        self.age = "6528"
        self.guild = "knight"
        self.existence = "500"


class Treasure:
    def __init__(self):
        self.count = 500


def main():
    a = Player()
    a.name = "Данте"
    print(a.name)


if __name__ == '__main__':
    main()
