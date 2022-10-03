import game


def enemies():
    empuza = game.Enemy()
    empuzes_queen = game.Enemy()
    fury = game.Enemy()
    Proto_Angelo = game.Enemy()
    empuza.name = "empuza"
    empuza.age = "10"
    empuza.guild = "small_demon"
    empuza.weapon = "сlaws"
    empuza.existence = "20"
    empuzes_queen.name = "empuzes_queen"
    empuzes_queen.age = "150"
    empuzes_queen.guild = "small_demon"
    empuzes_queen.weapon = "сlaws"
    empuzes_queen.existence = "200"
    fury.name = "fury"
    fury.age = "100"
    fury.guild = "middle_demon"
    fury.weapon = "сlaws"
    fury.existence = "300"
    Proto_Angelo.name = "Proto_Angelo"
    Proto_Angelo.age = "6528"
    Proto_Angelo.guild = "knight"
    Proto_Angelo.existence = "500"
    Proto_Angelo.weapon = "sword"
    return empuza, empuzes_queen, fury, Proto_Angelo
