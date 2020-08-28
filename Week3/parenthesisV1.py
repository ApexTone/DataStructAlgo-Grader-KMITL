class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0


def is_match(p_open, p_close):
    paren = {
        '{': '}',
        '(': ')',
        '[': ']',
        ']': '[',
        ')': '(',
        '}': '{'
    }
    return paren[p_open] == p_close


def parenthesis_check(exp):
    s = Stack()
    count = 0
    for letter in exp:
        if letter in "({[":
            s.push(letter)
        elif letter in ")}]":
            if not s.is_empty():
                if not is_match(letter, s.pop()):
                    count += 2
            else:
                count += 1
    else:  # do when loop end without break
        if s.is_empty() and count == 0:
            print("0\nPerfect ! ! !")
        else:  # excessive open parenthesis left in stack
            while not s.is_empty():
                s.pop()
                count += 1
            print(count)


if __name__ == '__main__':
    exp = input("Enter Input : ")
    parenthesis_check(exp)
