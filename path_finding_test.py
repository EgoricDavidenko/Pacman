boards = [[1, 1, 1, 1, 1, 1, 1],
          [1, -1, -1, -1, "x", -1, 1],
          [1, -1, -1, -1, -1, 1, 1],
          [1, -1, 1, 1, 1, -1, 1],
          [1, -1, "y", 1, -1, 1, 1],
          [1, -1, -1, -1, -1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1]]

player_mas = boards.copy()

for i in range(len(player_mas)):
    for j in range(len(player_mas)):
        if player_mas[i][j] == 1:
            player_mas[i][j] = 9999

def path(i, j, last, prev_dir, first_time = False):
    print(123)
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

path(1, 4, 0, "no", first_time=True)
for i in player_mas:
    print(i)
