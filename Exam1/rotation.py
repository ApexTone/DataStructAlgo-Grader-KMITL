if __name__ == '__main__':
    print('*** String Rotation ***')
    original = input('Enter 2 strings : ').split()
    copy1 = original[0]
    copy2 = original[1]
    counter = 1
    while True:
        temp = ''
        temp += copy1[len(copy1)-2:]+copy1[:len(copy1) -
                                           2]  # rotate 2 to the right
        copy1 = temp

        temp = ''
        temp += copy2[3:]+copy2[:3]  # rotate 3 to the left
        copy2 = temp

        if counter <= 5:
            print(counter, copy1, copy2)
        if copy1 == original[0] and copy2 == original[1]:
            if counter > 5:
                print(' . . . . .')
                print(counter, copy1, copy2)
            break
        counter += 1
    print(f'Total of  {counter} rounds.')
