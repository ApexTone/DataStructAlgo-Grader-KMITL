"""
5 by 5 grid:  # bomb, - clickable
--#--
-#--#
--###
-----
---#-

12#21
1#45#
12###
-1343
--1#1
"""


def bomb_value(grid, row, col):
    if row < 0 or col < 0 or row > 4 or col > 4:  # out of range
        return 0

    elif grid[row][col] == '#':
        return 1

    else:
        return 0


def sum_bomb(grid, row, col):
    return bomb_value(grid, row - 1, col - 1) + bomb_value(grid, row - 1, col) + bomb_value(grid, row - 1, col + 1) \
           + bomb_value(grid, row, col - 1) + 0 + bomb_value(grid, row, col + 1) \
           + bomb_value(grid, row + 1, col - 1) + bomb_value(grid, row + 1, col) + bomb_value(grid, row + 1, col + 1)


if __name__ == '__main__':
    grid = []
    for _ in range(5):
        line = input()
        grid.append(line)
    for row in range(5):
        buffer_string = ''
        value = 0
        for col in range(5):
            if grid[row][col] == '-':
                value = sum_bomb(grid, row, col)
                # print(value)
                if value == 0:
                    buffer_string += '-'
                else:
                    buffer_string += str(value)
            else:
                buffer_string += '#'
        grid[row] = buffer_string
    for line in grid:
        print(line)
