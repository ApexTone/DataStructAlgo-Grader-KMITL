# this code may not produce correct result format for grader
"""
2 3 4 5 6 7 8 9 10 11 12 -1 12 11 10 9 8 -1 8 10 12 3 5 7 9 11 -1
"""


def child_pat(lst):
    for i in lst:
        print(i, end=" ")
    print()


if __name__ == '__main__':
    print(' *** Recite the multiplication table ***')
    raw_input = input("Enter pattern for child 1 to 3 (-1 for sep) : ").split('-1')
    child1 = raw_input[0].split()
    child2 = raw_input[1].split()
    child3 = raw_input[2].split()
    print()
    print("Pattern for child 1 :", end=" ")
    child_pat(child1)
    print("Pattern for child 2 :", end=" ")
    child_pat(child2)
    print("Pattern for child 3 :", end=" ")
    child_pat(child3)

    day = 1
    lc1 = len(child1)
    lc2 = len(child2)
    lc3 = len(child3)
    while day <= 365:
        if child1[(day-1) % lc1] == child2[(day-1) % lc2] == child3[(day-1) % lc3]:
            break
        day += 1
    if day <= 365:
        print(day)
    else:
        print('No')
