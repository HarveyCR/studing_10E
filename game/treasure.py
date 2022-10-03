import game


def treasure():
    blood_coins = game.Treasure()
    golden_spheres = game.Treasure()
    purple_spheres = game.Treasure()
    blue_spheres = game.Treasure()
    blood_coins.kind = "blood_coins"
    golden_spheres.kind = "golden_spheres"
    purple_spheres.kind = "purple_spheres"
    blue_spheres.kind = "blue_spheres"
    blood_coins.ability = "nothing"
    golden_spheres.ability = "resurrection"
    purple_spheres.ability = "more the shape of a demon"
    blue_spheres.ability = "more existence"
    return blue_spheres, golden_spheres, purple_spheres, blue_spheres
