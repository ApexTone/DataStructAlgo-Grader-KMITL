class StackCalc:
    def __init__(self):
        self.items = []
        self.value = 0
    
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
        
    def run(self, exp):
        for letter in exp:
            if letter i
    
    def get_value(self):
        return self.value


if __name__ == '__main__':
    print("* Stack Calculator *")
    arg = input("Enter arguments : ").split()
    machine = StackCalc()
    machine.run(arg)
    print(machine.get_value())