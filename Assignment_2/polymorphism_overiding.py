class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Square(Shape):
    def draw(self):
        print("Drawing a Square")


# Main code
s1 = Circle()   
s2 = Square()  

shapes = [s1, s2]

for shape in shapes:
    shape.draw()
