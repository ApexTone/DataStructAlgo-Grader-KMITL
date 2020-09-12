if __name__ == "__main__":
    row = input('Enter Input : ').split()
    combo = 0

    while True:
        blasted = False
        blast_counter = 0
        current_color = None
        start_index = -1
        for i in range(len(row)-1):
            if start_index < 0:
                current_color = row[i]
                start_index = i
                blast_counter = 1

            # not able to blast
            if current_color != row[i]:
                current_color = row[i]
                start_index = i
                blast_counter = 1
            else:  # continue the blast_counter
                blast_counter += 1

            # blast
            if blast_counter >= 3:
                blasted = True
                combo += 1
                for _ in range(3):
                    row.pop(start_index)
                break
        if not blasted:
            break

    print(len(row))
    if len(row) == 0:
        print('Empty')
    else:
        for letter in row[::-1]:
            print(letter, end="")
        print()
    if combo >= 2:
        print(f'Combo : {combo} ! ! !')
