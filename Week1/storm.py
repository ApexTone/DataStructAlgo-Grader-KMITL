if __name__ == '__main__':
    print(' *** Wind classification ***')
    speed = float(input('Enter wind speed (km/h) : '))
    level = ''
    if speed <= 51.99:
        level = 'Breeze'
    elif speed <= 55.99:
        level = 'Depression'
    elif speed <= 101.99:
        level = 'Tropical Storm'
    elif speed <= 208.99:
        level = 'Typhoon'
    elif speed >= 209:
        level = 'Super Typhoon'
    print(f'Wind classification is {level}.')
