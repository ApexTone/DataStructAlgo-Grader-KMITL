# original code by ExitGuy
# documented and formatted by ApexTone

"""
1
..#+++
.##+#+
###+++
###+++
#+#++.
###+..

2
...#++++
..##+##+
.###+##+
####++++
####++++
#++#+++.
#++#++..
####+...

5
......#+++++++
.....##+#####+
....###+#####+
...####+#####+
..#####+#####+
.######+#####+
#######+++++++  # top half
#######+++++++  # bottom half
#+++++#++++++.
#+++++#+++++..
#+++++#++++...
#+++++#+++....
#+++++#++.....
#######+......
"""


def print_item(character, times):
    for i in range(times):
        print(character, end="")


if __name__ == '__main__':
    n = int(input("Enter Input : "))

    for i in range(2+n):  # top half
        print_item('.', 1+n-i)  # front reverse triangle
        print_item('#', i+1)  # front triangle
        print('+', end="")  # middle + line
        if 0 < i < n+1:  # python can do chain comparison, print # if it isn't first or last iteration
            print_item('#', n)  # fill
        else:
            print_item('+', n)  # border
        print('+')  # end + line and new line

    for i in range(2+n):  # bottom half
        print('#', end="")  # start # line
        if 0 < i < n+1:  # print + if it isn't first or last iteration
            print_item('+', n)  # fill
        else:
            print_item('#', n)  # border
        print('#', end="")  # middle # line
        print_item('+', 2+n-i)  # reverse triangle
        print_item('.', i)  # triangle
        print()  # new line
