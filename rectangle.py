#retangle: data member: width, height;  class methods:  area(), perimeter() return area and perimeter computer
import turtle

class Rectangle:
    def __init__(self, width, height):
        self.Width = width
        self.Height = height
    
    def area(self):
        return self.Width* self.Height
    
    def perimeter(self):
        return 2 * (self.Width + self.Height)
    
    def plot(self):
        t = turtle.Turtle()
        #print(t.pos())
        t.clear()
        t.goto(-100,-100)
        t.forward(self.Width)
        t.left(90)
        t.forward(self.Height)
        t.left(90)
        t.forward(self.Width)
        t.left(90)
        t.forward(self.Height)
        turtle.done()
    
rect1 = Rectangle(40, 30)
rect2 = Rectangle(60, 30)    
print(rect1.area())
print(rect1.perimeter())
bigRect = Rectangle(300, 200)
bigRect.plot()
