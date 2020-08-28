class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return -1

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return -1

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0


if __name__ == "__main__":
    print('******** Parking Lot ********')
    inp = input('Enter max of car,car in soi,operation : ').split()
    max_car = int(inp[0])
    cars = list(map(int, inp[1].split(',')))
    order = inp[2]
    car_id = int(inp[3])

    if len(cars) == 1 and cars[0] == 0:
        cars = []

    def debugmode():
        print('start'.center(20, '-'))
        print(max_car)
        print(cars)
        print(order)
        print(car_id)
        print('end'.center(20, '-'))
    # debugmode()

    if order == 'arrive':
        if car_id in cars:
            print(f'car {car_id} already in soi')
        elif len(cars) >= max_car:
            print(f'car {car_id} cannot arrive : Soi Full')
        else:
            print(f'car {car_id} arrive! : Add Car {car_id}')
            cars.append(car_id)
    elif order == 'depart':
        if len(cars) == 0:
            print(f'car {car_id} cannot depart : Soi Empty')
        elif car_id in cars:
            print(f'car {car_id} depart ! : Car {car_id} was remove')
            cars.remove(car_id)
        else:
            print(f'car {car_id} cannot depart : Dont Have Car {car_id}')

    print(cars)
