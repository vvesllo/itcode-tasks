class A:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"A(value={self.value})"
    
a = A(10)
b = A("abc")

print(a)
print(str(b))