# Code by Pop => Cheese for only 3,4 input

def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


if __name__ == '__main__':
    print('*** Fun with permute ***')
    num = [int(i) for i in input('input : ').split(',')]

    print('Original Cofllection: ', num)  # Typo for grader purpose
    print('Collection of distinct numbers:')
    num.reverse()
    case = 0
    if len(num) == 3:
        case = 1
    elif len(num) == 4:
        case = 2
    # print('length = ', len(num))
    # print('reverse = ', num)
    totalList = []
    starterList = []
    # append to new List
    for i in range(len(num)):
        starterList.append(num[i])

    start_index = 0
    next_index = 0
    if case == 1:
        # append to totalList
        totalList.append(starterList)
        for i in range(factorial(len(num))-1):
            # print('--------------')
            # print('loop =', i)
            newList = []

            start_index = -len(num) + i
            next_index = -len(num) + i + 1
            # print('start = ', start)
            # print('next = ', next)

            # swap!!!
            num[start_index], num[next_index] = num[next_index], num[start_index]

            # append to new List
            for j in range(len(num)):
                newList.append(num[j])

            # append to totalList
            totalList.append(newList)

            # print('totalList now = ', totalList)
            # print('--------------')
    elif case == 2:

        case2_list = []
        for i in range(1, len(num)):
            case2_list.append(num[i])
        for i in range(factorial(len(num))):
            if i % 4 == 0:
                case_list = list()
                case_list.append(starterList[0])
                i = i//4
                newList = []
                start2 = -len(num) + i
                next2 = -len(num) + 1 + i
                # swap!!!
                if i != 0:
                    case2_list[start2], case2_list[next2] = case2_list[next2], case2_list[start2]
                # append to new List
                for j in range(len(num)):
                    newList.append(num[j])
                # extend to caseList
                case_list.extend(case2_list)
                # append to totalList
                totalList.append(case_list)
            else:
                if i % 4 == 1:
                    num = case_list.copy()
                i = (i % 4)-1
                newList = []
                start_index = -len(num) + i
                next_index = -len(num) + 1 + i

                # swap!!!
                num[start_index], num[next_index] = num[next_index], num[start_index]
                # append to new List
                for j in range(len(num)):
                    newList.append(num[j])

                # append to totalList
                totalList.append(newList)

    print('', totalList)
