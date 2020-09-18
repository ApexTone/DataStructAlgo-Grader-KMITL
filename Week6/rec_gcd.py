def rec_gcd(x, y):
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    if x != 0 and y == 0:
        return x
    elif x == 0 and y != 0:
        return y
    elif x == 1 or y == 1:
        return 1
    else:
        if x >= y:
            return rec_gcd(y, x % y)
        else:
            return rec_gcd(x, y % x)


if __name__ == '__main__':
    a, b = list(map(int, input('Enter Input : ').split()))
    if a == 0 and b == 0:
        print('Error! must be not all zero.')
    else:
        if a >= b >= 0 or a >= 0 >= b:
            print(f'The gcd of {a} and {b} is : {rec_gcd(a, b)}')
        elif b >= a >= 0 or b >= 0 >= a:
            print(f'The gcd of {b} and {a} is : {rec_gcd(a, b)}')
        elif a < 0 and b < 0:
            if abs(a) > abs(b):
                print(f'The gcd of {a} and {b} is : {rec_gcd(a, b)}')
            else:
                print(f'The gcd of {b} and {a} is : {rec_gcd(a, b)}')