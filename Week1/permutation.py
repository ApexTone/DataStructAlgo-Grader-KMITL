# code by exithere

if __name__ == '__main__':
    print("*** Fun with permute ***")
    lst = list(map(int, input("input : ").split(',')))
    print("Original Cofllection: ", lst)  # typo for grader
    lst = lst[::-1]  # reverse the input
    print("Collection of distinct numbers:")
    print(' ', end='')

    def add_permutation(position, l):
        return [l[0:i] + [lst[position]] + l[i:] for i in range(len(l) + 1)]

    def permutation(l):
        if len(l) == 0:
            return [[]]
        return [x for y in permutation(l[1:]) for x in add_permutation(l[0], y)]

    print(permutation([i for i in range(len(lst))]))