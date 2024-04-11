import math

class Calculator:
    
    def tokeniser(self, expression): # "2+3-5"
        minusflag = 1
        expression.replace(" ", "")
        expression += ' '
        tokenlist = []
        token = ''
        chr = 0
        while chr < len(expression):
            if expression[chr] in ' ,':
                 chr += 1
            elif expression[chr] == '-' and minusflag == 1:
                token += expression[chr]
                while expression[chr + 1] in "0123456789.":
                    token += expression[chr + 1]
                    chr += 1
                tokenlist.append(token)
                token = ''
                chr += 1
                minusflag = 0
            elif expression[chr] == '(':
                token = '('
                tokenlist.append(token)
                chr += 1
                minusflag = 1
                token = ''
            elif expression[chr] == ')':
                token = ')'
                tokenlist.append(token)
                chr += 1
                minusflag = 0
                token = ''
            elif expression[chr] in "0123456789.":
                token += expression[chr]
                while expression[chr + 1] in "0123456789.":
                    token += expression[chr + 1]
                    chr += 1
                tokenlist.append(token)
                token = ''
                chr += 1
                minusflag = 0
            elif expression[chr] in "sctelm":
                token = expression[chr] + expression[chr + 1] + expression[chr + 2] + ('t' if expression[chr + 3] == 't' else '')
                tokenlist.append(token)
                token = ''
                chr += 3 + (1 if expression[chr + 3] == 't' else 0)
                minusflag = 0
            else:
                token = expression[chr]
                tokenlist.append(token)
                token = ''
                chr += 1
                minusflag = 0
        return tokenlist
    
    def calculate(self, expression):
        operationRang = {
            '(' : 0,
            '+' : 1,
            '-' : 1,
            '*' : 2,
            '/' : 2,
            '^' : 3,
            'sqrt' : 3,
            'sin' : 4,
            'cos' : 4,
            'tan' : 4,
            'ctg' : 4,
            'exp' : 5,
            '!' : 6,
            'log' : 7, #log(base, x)
            'mod' : 8,
        }

        tokenlist = self.tokeniser(expression)
        stack_d = []
        stack_c = []
        for token in tokenlist:
            try:
                stack_d.append(float(token))
            except ValueError:
                if token == '(':
                    stack_c.append(token)
                elif token == ')':
                    while stack_c[-1] != '(':
                        if stack_c[-1] in ['+','-','*','/','^',"log", "mod"]:
                            temp = self.operation(stack_c[-1], stack_d[-2], stack_d[-1])
                            stack_d.pop()
                            stack_d.pop()
                            stack_d.append(temp)
                            stack_c.pop()
                        else:
                            temp = self.operation(stack_c[-1], stack_d[-1])
                            stack_d.pop()
                            stack_d.append(temp)
                            stack_c.pop()
                    stack_c.pop()
                            
                elif len(stack_c) == 0:
                    stack_c.append(token)
                elif operationRang[token] <= operationRang[stack_c[-1]]:
                    while len(stack_c) != 0 and operationRang[token] < operationRang[stack_c[-1]]:
                        if stack_c[-1] in ['+','-','*','/','^',"log", "mod"]:
                            temp = self.operation(stack_c[-1], stack_d[-2], stack_d[-1])
                            stack_d.pop()
                            stack_d.pop()
                            stack_d.append(temp)
                            stack_c.pop()
                        elif stack_c[-1] in ["cos", "sin", "tan", "ctg", '!', 'sqrt', 'exp']:
                            temp = self.operation(stack_c[-1], stack_d[-1])
                            stack_d.pop()
                            stack_d.append(temp)
                            stack_c.pop()
                    stack_c.append(token)
                else:
                    stack_c.append(token)
            
        while len(stack_c) > 0:
            if stack_c[-1] in ['+','-','*','/','^',"log", "mod"]:
                temp = self.operation(stack_c[-1], stack_d[-2], stack_d[-1])
                stack_d.pop()
                stack_d.pop()
                stack_d.append(temp)
                stack_c.pop()
            elif stack_c[-1] in ["cos", "sin", "tan", "ctg", '!', 'sqrt', 'exp']:
                temp = self.operation(stack_c[-1], stack_d[-1])
                stack_d.pop()
                stack_d.append(temp)
                stack_c.pop()

        if len(stack_d) == 1:
            print(round(stack_d[0]*10000)/10000)
        

        
    
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return "Ошибка деления на ноль"

    def power(self, x, y):
        return x ** y

    def sqrt(self, x):
        return x ** .5

    def factorial(self, x):
        if int(x) == x and x > 0:
            return math.factorial(int(x))
        else:
            raise ValueError("Факториал определен только для целых положительных чисел")

    def Sin(self, x):
        return round(math.sin(x * math.pi / 180)*100000) / 100000

    def Cos(self, x):
        return round(math.cos(x * math.pi / 180)*100000) / 100000

    def Tan(self, x):
        return self.Sin(x) / self.Cos(x)

    def Ctg(self, x):
        return self.Cos(x) / self.Sin(x)
    
    def Exp(self, x):
        return math.exp(x)

    def Log(self, x, y):
        return math.log(x, y)
    
    def Mod(self, x, y):
        return x % y

    def operation(self, operation, x=0, y=0):
        match operation:
            case "+":
                return self.add(x, y)
            case "-":
                return self.subtract(x, y)
            case "*":
                return self.multiply(x, y)
            case "/":
                return self.divide(x, y)
            case "^":
                return self.power(x, y)
            case "sqrt":
                return self.sqrt(x)
            case "!":
                return self.factorial(x)
            case "sin":
                return self.Sin(x)
            case "cos":
                return self.Cos(x)
            case "tan":
                return self.Tan(x)
            case "ctg":
                return self.Ctg(x)
            case "exp":
                return self.Exp(x)
            case "log":
                return self.Log(y, x)
            case "mod":
                return self.Mod(x, y)

calc1 = Calculator()
while 1:
    expression = input("Введите выражение:\n")
    calc1.calculate(expression)