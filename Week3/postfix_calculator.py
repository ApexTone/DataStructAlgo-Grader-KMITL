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
            return 0
        return self.items[-1]

    def pop(self):
        if self.is_empty():
            # print("Stack is empty")
            return 0
        return self.items.pop()

    def push(self, value):
        self.items.append(value)


class StackCalc:
    def __init__(self, postfix=""):
        self.postfix = postfix
        self.value = 0

    def run(self, postfix):
        s = Stack()
        for value in postfix:
            if value == "DUP":
                s.push(s.peek())
            elif value == "POP":
                s.pop()
            elif value == "PSH":
                pass
            elif value in "+-*/^":
                a = s.pop()
                b = s.pop()
                if value == '+':
                    s.push(a+b)
                elif value == '-':
                    s.push(a-b)
                elif value == '*':
                    s.push(a*b)
                elif value == '/':
                    s.push(a/b)
                elif value == '^':
                    s.push(a**b)
            else:
                try:
                    s.push(int(value))
                except:
                    print(f'Invalid instruction: {value}')
                    quit()
        self.value = s.pop()

    def get_value(self):
        return self.value


if __name__ == '__main__':
    print("* Stack Calculator *")
    arg = input("Enter arguments : ").split()
    machine = StackCalc()
    machine.run(arg)
    print(f"{machine.get_value():.0f}")
