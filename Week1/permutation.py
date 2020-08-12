# @todo #2:1days Fix permutation order
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

        # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

        # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


if __name__ == '__main__':
    print('*** Fun with permute ***')
    num = [int(i) for i in input('input : ').split(',')]
    # ans = []
    print('Original Cofllection: ', num)  # Typo for grader purpose
    """
    # ans.append(num)
    num.reverse()
    for i in range(len(num)):
        temp = num.copy()
        print("Big loop", i)
        for j in range(i, len(num)):
            # print(temp[j], temp[j+1], end=" ")
            if i < len(num)-1:
                print('Normal', end=" ")
                temp[j], temp[j+1] = temp[j+1], temp[j]
            else:
                print('Special', end=" ")
                temp[0], temp[len(num)-1] = temp[len(num)-1], temp[0]
            print(temp)
            clone = temp.copy()
            if clone in ans:
                continue
            ans.append(clone)
    rev = num.copy()
    rev.reverse()
    # ans.append(rev)
    """
    ans = permutation(num)
    ans.reverse()
    print('Collection of distinct numbers:\n', ans)

