def count_deaf_rats(town_square: list[str]):
    for y in range(len(town_square)):
        line = town_square[y]
        print(line)
        for x in range(len(line)):
            char = line[x]
            if char == "P":
                piper = (x, y)
                break

    rat_dict = {"↘": (1, 1),
                "↓": (0, 1),
                "↙": (-1, 1),
                "→": (1, 0),
                "←": (-1, 0),
                "↗": (1, -1),
                "↑": (0, -1),
                "↖": (-1, -1)
                }

    def measure_distance(x, y):
        return ((x - piper[0]) ** 2 + (y - piper[1]) ** 2) ** 0.5

    result = 0
    for y in range(len(town_square)):
        line = town_square[y]
        for x in range(len(line)):
            char = line[x]
            if char in rat_dict.keys():
                original_distance = measure_distance(x, y)
                next_x = rat_dict[char][0] + x
                next_y = rat_dict[char][1] + y
                next_distance = measure_distance(next_x, next_y)
                if next_distance > original_distance:
                    result += 1
    return result
