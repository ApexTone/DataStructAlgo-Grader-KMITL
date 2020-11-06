def insertion_index(lst, curr_index, value):  # shift list value and return insertion index
    if curr_index > 0 and lst[curr_index - 1] > value:  # if this is not where to insert
        lst[curr_index] = lst[curr_index - 1]  # shift list element
        return insertion_index(lst, curr_index - 1, value)  # compare with another element
    else:
        return curr_index  # return insertion index


def insertion_sort(lst, start=0, length=None, progress=0):
    if length is None:  # for less parameters passing
        length = len(lst)

    value = lst[start]  # store value to be inserted

    index = insertion_index(lst, start, value)  # get insertion index and shift the list
    lst[index] = value  # insert value to the index
    progress += 1  # increase sorted part length

    if progress > 1:  # print insertion process (skip the first time)
        if len(lst[progress:]) != 0:  # prevent empty list printing '[]'
            print(f"insert {value} at index {index} : {lst[:progress]} {lst[progress:]}")
        else:
            print(f"insert {value} at index {index} : {lst[:progress]}")

    if start+1 < length:  # do until the last element
        insertion_sort(lst, start+1, length, progress)  # move to insert next element


if __name__ == '__main__':
    in_lst = list(map(int, input("Enter Input : ").split()))
    # Python function parameter is passed by reference, No return needed! Change will be applied directly.
    insertion_sort(in_lst)
    print("sorted")
    print(in_lst)
