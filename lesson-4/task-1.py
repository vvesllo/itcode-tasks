class Rectange:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
rect = Rectange(5, 10)

print(f"Rect S={rect.get_square()}")
print(f"Rect P={rect.get_perimeter()}")