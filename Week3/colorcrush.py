if __name__ == "__main__":
    row = input('Enter Input : ').split()
    combo = 0

    while True:
        blasted = False
        blast_counter = 0
        # print("new round", row)
        current_color = None
        start_index = -1
        for i in range(len(row)-1):
            # print(f'Blast counter: {blast_counter}')
            if start_index < 0:
                current_color = row[i]
                start_index = i
                blast_counter = 1
                # print(f'Color to blast: {current_color}')

            # not able to blast
            if current_color != row[i]:
                # print(f'Change color: {row[i]}')
                current_color = row[i]
                start_index = i
                blast_counter = 1
            else:  # continue the blast_counter
                blast_counter += 1
                # print(f'Continue {blast_counter}')

            # blast
            if blast_counter >= 3:
                blasted = True
                combo += 1
                # print('-----------------------------------')
                # print(f'Blasting {current_color}')
                # print(row)
                # print(f"start at: {start_index}, end at: {start_index+2}")
                for _ in range(3):
                    row.pop(start_index)
                # print('-----------------------------------')
                break
        if not blasted:
            break

    # print('--------End-----------')
    print(len(row))
    if len(row) == 0:
        print('Empty')
    else:
        for letter in row[::-1]:
            print(letter, end="")
        print()
    if combo >= 2:
        print(f'Combo : {combo} ! ! !')
