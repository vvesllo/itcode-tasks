class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b
    
    @staticmethod
    def mul(a, b):
        return a * b
    
    @staticmethod
    def div(a, b):
        return a / b
    

print(Calculator.add(2, 5))
print(Calculator.sub(12, 6))
print(Calculator.mul(3, 3))
print(Calculator.div(6, 2))