def find_alphabet(text):
    for character in text:
        if ord('a') <= ord(character) <= ord("z"):
            return character
    return None

def alphabet_sort(lst):
    prep = []
    for item in lst:
        prep.append((find_alphabet(item), item))
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-1-i):
            if prep[j][0] > prep[j+1][0]:
                prep[j], prep[j+1] = prep[j+1], prep[j]
                swapped = True
        if not swapped:
            break
    out_lst = []
    for item in prep:
        out_lst.append(item[1])
    return out_lst


if __name__ == '__main__':
    in_lst = input("Enter Input : ").split(' ')
    out = alphabet_sort(in_lst)
    for item in out:
        print(item, end=" ")