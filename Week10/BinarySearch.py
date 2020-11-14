def bi_search(left, right, lst, key):
    if left <= right:
        mid = (left + right) // 2
        if lst[mid] < key:
            return bi_search(mid + 1, right, lst, key)
        elif lst[mid] > key:
            return bi_search(left, mid - 1, lst, key)
        else:
            return True
    return False


if __name__ == '__main__':
    inp = input('Enter Input : ').split('/')
    arr, k = list(map(int, inp[0].split())), int(inp[1])
    print(bi_search(0, len(arr) - 1, sorted(arr), k))