import math

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y

    def subtract(self, x, y):
        self.result = x - y

    def multiply(self, x, y):
        self.result = x * y

    def divide(self, x, y):
        try:
            self.result = x / y
        except ZeroDivisionError:
            raise ZeroDivisionError("Ошибка деления на ноль")

    def power(self, x, y):
        self.result = x ** y

    def sqrt(self, x):
        self.result = x ** .5

    def factorial(self, x):
        try:
            self.result = math.factorial(x)
        except ValueError:
            raise ValueError("Факториал определен только для целых положительных чисел")

    def sin(self, x):
        self.result = math.sin(x * math.pi / 180)

    def cos(self, x):
        self.result = math.cos(x * math.pi / 180)

    def tg(self, x):
        self.result = math.tan(x * math.pi / 180)

    def ctg(self, x):
        self.result = math.cos(x * math.pi / 180) / math.sin(x * math.pi / 180)

    def log(self, x, y):
        self.result = math.log(x, y)

    def operation(self, operation, x=0, y=0):
        match operation:
            case "+":
                self.add(x, y)
            case "-":
                self.subtract(x, y)
            case "*":
                self.multiply(x, y)
            case "/":
                self.divide(x, y)
            case "^":
                self.power(x, y)
            case "sqrt":
                self.sqrt(x)
            case "!":
                self.factorial(x)
            case "sin":
                self.sin(x)
            case "cos":
                self.cos(x)
            case "tg":
                self.tg(x)
            case "ctg":
                self.ctg(x)


calc1 = Calculator()
OperationsOrder = ["sin", "cos", "tg", "ctg", "!", "sqrt", "^", "*", "/", "+", "-"]

print("доступные операции:\nsin\tcos\ttg\tctg\t!\tsqrt\t^\t*\t/\t+\t-")
while True:
    expression = input("Введите выражение (операции и операнды отделять пробелом)\n")
    NumsAndOperations = expression.split()
    for operation in OperationsOrder:
        i = 0
        while i < len(NumsAndOperations):
            if NumsAndOperations[i] == operation:
                if operation in ["sqrt", "tg", "ctg", "sin", "cos"]:
                    calc1.operation(operation, float(NumsAndOperations[i + 1]))
                    NumsAndOperations[i] = calc1.result
                    del NumsAndOperations[i + 1]
                elif operation == "!":
                    try:
                        calc1.factorial(int(NumsAndOperations[i - 1]))
                        NumsAndOperations[i] = calc1.result
                        del NumsAndOperations[i - 1]
                    except ValueError:
                        raise ValueError("Факториал определен только для целых положительных чисел")
                else:
                    calc1.operation(operation, float(NumsAndOperations[i - 1]), float(NumsAndOperations[i + 1]))
                    NumsAndOperations[i] = calc1.result
                    del NumsAndOperations[i + 1]
                    del NumsAndOperations[i - 1]
                i = 0
            else:
                i += 1

    print(calc1.result)
    calc1.result = 0
