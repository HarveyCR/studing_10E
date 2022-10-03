import game


def treasure():
    blood_coins = game.Treasure()
    golden_spheres = game.Treasure()
    purple_spheres = game.Treasure()
    blue_spheres = game.Treasure()
    blood_coins.kind = "Кровавые монетки"
    golden_spheres.kind = "Золотые сферы"
    purple_spheres.kind = "Фиолетовые сферы"
    blue_spheres.kind = "Синие сферы"
    blood_coins.ability = "Отсутствует"
    golden_spheres.ability = "Воскрешение"
    purple_spheres.ability = "Увеличение полоски демона"
    blue_spheres.ability = "Увеличение ХП"
    return blood_coins, golden_spheres, purple_spheres, blue_spheres
