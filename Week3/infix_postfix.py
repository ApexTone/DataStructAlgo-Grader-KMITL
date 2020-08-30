class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if self.is_empty():
            # print("Stack is empty")
            return -1
        return self.items[-1]

    def pop(self):
        if self.is_empty():
            # print("Stack is empty")
            return -1
        return self.items.pop()

    def push(self, value):
        self.items.append(value)


def infix_to_postfix(exp):  # code this -> bug
    s = Stack()
    postfix = ''
    priority = {
        '(': -99,
        '+': 0,
        '-': 0,
        '*': 2,
        '/': 2,
        '^': 3,
    }
    # how to optimize?
    for letter in exp:
        if letter in '+-*/^':  # interesting part
            if s.is_empty():
                s.push(letter)
            else:
                while not s.is_empty():
                    if s.peek() == '(':
                        break
                    else:  # don't change this
                        if priority.get(s.peek(), -2) < priority.get(letter, -2):
                            break
                        else:
                            postfix += s.pop()
                s.push(letter)
        elif letter == '(':
            s.push(letter)
        elif letter == ')':
            while s.peek() != '(':
                postfix += s.pop()
            s.pop()
        else:
            postfix += letter
    while not s.is_empty():
        postfix += s.pop()
    return postfix


if __name__ == '__main__':
    out = infix_to_postfix(input('Enter input : '))
    print(out)
