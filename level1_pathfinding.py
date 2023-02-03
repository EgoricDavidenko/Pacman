import level1
import game_temp

player_mas = level1.boards.copy()

player_mas[game_temp.player_y - 1][game_temp.player_x - 1] = "y"

for i in range(33):
    player_mas[i].append(0)
    player_mas[i].insert(0, 0)
    for j in range(30):
        if player_mas[i][j] in [0, 1, 2]:
            player_mas[i][j] = 0


def path(i, j, last, prev_dir, first_time = False):
    if player_mas[i][j] != "x":
        if player_mas[i][j] != "y":
            if player_mas[i][j] == -1:
                player_mas[i][j] = last + 1
                if prev_dir == "left":
                    path(i + 1, j, last + 1, "down")
                    path(i - 1, j, last + 1, "up")
                    path(i, j - 1, last + 1, "left")
                if prev_dir == "right":
                    path(i + 1, j, last + 1, "down")
                    path(i - 1, j, last + 1, "up")
                    path(i, j + 1, last + 1, "right")
                if prev_dir == "up":
                    path(i - 1, j, last + 1, "up")
                    path(i, j - 1, last + 1, "left")
                    path(i, j + 1, last + 1, "right")
                if prev_dir == "down":
                    path(i + 1, j, last + 1, "down")
                    path(i, j - 1, last + 1, "left")
                    path(i, j + 1, last + 1, "right")
            else:
                return 0
        else:
            print(f"boards[{i}][{j}]")
            return 0
    else:
        if first_time:
            print(1)
            path(i - 1, j, last + 1, "up")
            print(2)
            path(i + 1, j, last + 1, "down")
            print(3)
            path(i, j - 1, last + 1, "left")
            print(4)
            path(i, j + 1, last + 1, "right")
            print(5)
        else:
            return 0

    return 0


path(16, 15, 0, "no", first_time=True)

player_mas[16][15] = "x"

for i in player_mas:
    print(i)