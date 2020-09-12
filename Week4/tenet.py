class Queue:
    def __init__(self):
        self.items = list()

    def enqueue(self, value):
        self.items.append(value)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() <= 0

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return -1

    def pop_back(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return -1

    def __len__(self):
        return self.size()

    def __str__(self):
        output = ""
        if not self.is_empty():
            for item in self.items:
                output += str(item)
        else:
            output = 'Empty'
        return output


def will_explode(a, b, c):
    return a == b == c


if __name__ == '__main__':
    red, blue = input('Enter Input (Red, Blue) : ').split()
    red, blue = list(red), list(blue)
    # print(red, blue)
    defuser = []
    red_explosion = 0

    while True:
        exploded = False
        for i in range(len(blue) - 2):
            if will_explode(blue[i], blue[i+1], blue[i+2]):
                exploded = True
                defuser.append(blue[i])
                for _ in range(3):
                    blue.pop(i)
                break
        if not exploded:
            break
    blue_explosion = len(defuser)

    mistakes = 0
    while True:
        defuser_group = -1
        exploded = False
        for i in range(len(red) - 2):  # problem?
            if len(defuser) > 0:
                if will_explode(red[i], red[i+1], red[i+2]):
                    red.insert(i+2, defuser.pop())
                    defuser_group = i
            print(red)
            for j in range(i):
                print('     ', end="")
            # loop doesn't reached the end (consider special case)
            print(red[i:i+3])
            if will_explode(red[i], red[i + 1], red[i + 2]):  # don't check last element

                if defuser_group == i:  # bad defuser placement
                    mistakes += 1
                else:
                    red_explosion += 1
                exploded = True
                for _ in range(3):
                    red.pop(i)
                break
        if not exploded:
            break
    print('Red Team :')
    print(len(red))
    if len(red) == 0:
        print('Empty')
    else:
        for i in range(len(red)-1, -1, -1):
            print(red[i], end="")
        print()
    print(f'{red_explosion} Explosive(s) ! ! ! (HEAT)')
    if mistakes > 0:
        print(f'Blue Team Made (a) Mistake(s) {mistakes} Bomb(s)')
    print('----------TENETTENET----------')
    print(': maeT eulB')
    print(len(blue))
    if len(blue) == 0:
        print('ytpmE')
    else:
        for i in blue:
            print(i, end="")
        print()
    print(f'(EZEERF) ! ! ! (s)evisolpxE {blue_explosion}')


'''
Enter Input (Red, Blue) : AAABBBCDEE HHH
Red Team :
8
EEDCAHAA
1 Explosive(s) ! ! ! (HEAT)
----------TENETTENET----------
: maeT eulB
0
ytpmE
(EZEERF) ! ! ! (s)evisolpxE 1


Enter Input (Red, Blue) : AAABBBCDEE FGHHHIOPPP
Red Team :
12
EEDCBHBBAPAA
0 Explosive(s) ! ! ! (HEAT)
----------TENETTENET----------
: maeT eulB
4
FGIO
(EZEERF) ! ! ! (s)evisolpxE 2


Enter Input (Red, Blue) : AAABBBCDDDEE BBBTENETAAA  # handle this case
Red Team :
5
EECBA
1 Explosive(s) ! ! ! (HEAT)
Blue Team Made (a) Mistake(s) 2 Bomb(s)  # this
----------TENETTENET----------
: maeT eulB
5
TENET
(EZEERF) ! ! ! (s)evisolpxE 2


Enter Input (Red, Blue) : AAABBBDDD TENET
Red Team :
0
Empty
3 Explosive(s) ! ! ! (HEAT)
----------TENETTENET----------
: maeT eulB
5
TENET
(EZEERF) ! ! ! (s)evisolpxE 0


Enter Input (Red, Blue) : AAABBBCDDDEE OOOZZZTENETXXXYYY
Red Team :
15
EEDZDDCBXBBAYAA
0 Explosive(s) ! ! ! (HEAT)
----------TENETTENET----------
: maeT eulB
5
TENET
(EZEERF) ! ! ! (s)evisolpxE 4

Enter Input (Red, Blue) : pppaaaabbbb pppaaaa  -> consider this case
Red Team :
10
baapaapapp //bbbbaapaapapp bad output
1 Explosive(s) ! ! ! (HEAT)
----------TENETTENET----------
: maeT eulB
1
a
(EZEERF) ! ! ! (s)evisolpxE 2
'''
