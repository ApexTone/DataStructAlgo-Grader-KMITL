"""
Input = 3
*    *
**  **
******
**  **
*    *

Input = 4
*      *
**    **
***  ***
********
***  ***
**    **
*      *
"""


if __name__ == '__main__':
    number = int(input("Input = "))
    stars = 1
    spaces = 2 * number - 2
    for _ in range(number):  # top half
        for _ in range(stars):
            print('*', end="")
        for _ in range(spaces):
            print(' ', end="")
        for _ in range(stars):
            print('*', end="")
        stars += 1
        spaces -= 2
        print()

    stars -= 1
    spaces += 2
    for _ in range(number-1):  # bottom half
        stars -= 1
        spaces += 2
        for _ in range(stars):
            print('*', end="")
        for _ in range(spaces):
            print(' ', end="")
        for _ in range(stars):
            print('*', end="")

        print()
