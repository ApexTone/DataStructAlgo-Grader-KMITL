"""
*** Fun with Drawing ***
Enter input : 2
.*.*.
*+*+* -> top half
.*+*. -> bottom half (1 Fill)
..*..

*** Fun with Drawing ***
Enter input : 5
....*.......*....
...*+*.....*+*...
..*+++*...*+++*..
.*+++++*.*+++++*.
*+++++++*+++++++* -> top half (max fill 7)
.*+++++++++++++*. -> bottom half (13 fill)
..*+++++++++++*..
...*+++++++++*...
....*+++++++*....
.....*+++++*.....
......*+++*......
.......*+*.......
........*........

*** Fun with Drawing ***
Enter input : 7
......*...........*......
.....*+*.........*+*.....
....*+++*.......*+++*....
...*+++++*.....*+++++*...
..*+++++++*...*+++++++*..
.*+++++++++*.*+++++++++*.
*+++++++++++*+++++++++++* -> top half (max fill 11)
.*+++++++++++++++++++++*. -> bottom half (21 fill)
..*+++++++++++++++++++*..
...*+++++++++++++++++*...
....*+++++++++++++++*....
.....*+++++++++++++*.....
......*+++++++++++*......
.......*+++++++++*.......
........*+++++++*........
.........*+++++*.........
..........*+++*..........
...........*+*...........
............*............
"""
# max_cols: 2->5=2+1+2 5->17=8+1+8 7->25=12+1+12    (4n-3)
# max_rows: 2->4 5->13 7->19    (3n-2)


def loop_print(number=0, character='.'):
    for _ in range(number):
        print(character, end="")


def top_half(n):  # 2->2 5->5 7->7
    fill = None
    for row in range(n):
        spaces = n-(row+1)
        if row == 0:  # 0, 1 3 5 7 ... 2n-3 (n=row)
            fill = 0
        else:
            fill = 2+((row-1)*2-1)
        # print(fill)
        # fs * fill *? bs fs * fill *?
        loop_print(spaces, '.')
        print('*', end="")  # *
        loop_print(fill, '+')
        if fill > 0 and fill != 2*n-3:  # *?
            print('*', end="")
        loop_print(spaces, '.')
        loop_print(spaces-1, '.')
        print('*', end="")  # *
        loop_print(fill, '+')
        if fill > 0:  # *?
            print('*', end="")
        loop_print(spaces, '.')
        print()


def bottom_half(n):  # 2->2 5->8 7->12 (n*2-2)
    for row in range((n*2)-2):
        spaces = row+1
        fill = (4*n-5)-(spaces*2)
        loop_print(spaces, '.')
        print('*', end="")
        loop_print(fill,'+')
        if fill > 0:
            print('*', end="")
        loop_print(spaces, '.')
        print()


if __name__ == '__main__':
    print('*** Fun with Drawing ***')
    n = int(input('Enter input : '))
    top_half(n)
    bottom_half(n)


