class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, obj):
        return self.value + obj.value

    def __sub__(self, obj):
        return self.value - obj.value

    def __mul__(self, obj):
        return self.value * obj.value

    def __truediv__(self, obj):
        return self.value / obj.value


if __name__ == '__main__':
    x, y = input("Enter num1 num2 : ").split(",")
    x, y = Calculator(int(x)), Calculator(int(y))
    print(x + y, x - y, x * y, x / y, sep="\n")
