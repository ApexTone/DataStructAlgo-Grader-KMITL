if __name__ == '__main__':
    print(' *** Wind classification ***')
    speed = float(input('Enter wind speed (km/h) : '))
    res = ''
    if speed < 0:
        print("!!!Wrong value can't classify.")
        quit()
    if 0 <= speed < 52:
        res = 'Breeze'
    elif speed < 56:
        res = 'Depression'
    elif speed < 102:
        res = 'Tropical Storm'
    elif speed < 209:
        res = 'Typhoon'
    elif speed >= 209:
        res = 'Super Typhoon'
    print(f'Wind classification is {res}.')
