def make_range(args):
    la = len(args)
    output = list()
    if la == 1:
        end = args[0]
        i = 0.0
        while i < end:
            output.append(round(i, 3))
            i += 1
    elif la == 2:
        start = args[0]
        end = args[1]
        i = float(start)
        while i < end:
            output.append(round(i, 3))
            i += 1
    elif la == 3:
        start = args[0]
        end = args[1]
        step = args[2]
        i = float(start)
        while i < end:
            output.append(round(i, 3))
            i += step
    else:
        return 'ERROR'
    return tuple(output)


if __name__ == '__main__':
    print('*** New Range ***')
    in_args = list(map(float, input("Enter Input : ").split()))
    print(make_range(in_args))
