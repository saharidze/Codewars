def tower_builder(floors):
    tower = []
    width = floors * 2 - 1
    for i in range(1, floors + 1):
        stars = "*" * (i * 2 - 1)
        line = stars.center(width)
        tower.append(line)
    return tower
