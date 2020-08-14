def odd_even(arr, s):
    # odd-even is not array index
    if type(arr) is list:  # if list
        output = list()
        if s == 'Even':
            for i in range(1, len(arr), 2):
                output.append(arr[i])
        else:
            for i in range(0, len(arr), 2):
                output.append(arr[i])
        return output
    else:  # if string
        output = ''
        if s == 'Even':
            for i in range(1, len(arr), 2):
                output += arr[i]
        else:
            for i in range(0, len(arr), 2):
                output += arr[i]
        return output


if __name__ == '__main__':
    print('*** Odd Even ***')
    input_type, input_arr, oe = input('Enter Input : ').split(',')
    # print(input_type)
    if input_type == 'L':
        input_arr = input_arr.split()
    # print(input_arr)
    # print(oe)
    print(odd_even(input_arr, oe))
