import game


def enemies():
    empuza = game.Enemy()
    empuzes_queen = game.Enemy()
    fury = game.Enemy()
    Proto_Angelo = game.Enemy()
    empuza.name = "Импуза"
    empuza.age = "10"
    empuza.guild = "Малый демон"
    empuza.weapon = "Когти"
    empuza.existence = "20"
    empuzes_queen.name = "Королева Импуз"
    empuzes_queen.age = "150"
    empuzes_queen.guild = "Малый демон"
    empuzes_queen.weapon = "Когти"
    empuzes_queen.existence = "200"
    fury.name = "Ярость"
    fury.age = "100"
    fury.guild = "Сильный демон"
    fury.weapon = "Когти"
    fury.existence = "300"
    Proto_Angelo.name = "Прото-Анжело"
    Proto_Angelo.age = "6528"
    Proto_Angelo.guild = "Рыцарь"
    Proto_Angelo.existence = "500"
    Proto_Angelo.weapon = "Электрический меч"
    return empuza, empuzes_queen, fury, Proto_Angelo
