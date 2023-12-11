import numpy as np
from PIL import Image

class Canvas:
    """
    class that will make a canvas after getting user input
    """
    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width

        # create empty 3D grid
        self.matrix = np.zeros((self.width, self.height, 3), dtype=np.uint8)

        # change 0,0,0 to users options
        self.matrix[:] = self.color

    def make(self):
        """
        method that will save final img
        """
        img = Image.fromarray(self.matrix, 'RGB')
        img.save('name.png')

class Rectangle:
    """
    class that will draw a rectangle based on user input.
    """

    def __init__(self, x, y, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        self.y = y
        self.x = x

    def draw(self, canvas):
        self.canvas = canvas
        """
        method that will draw rectangle on canvas
        """
        canvas.matrix[self.x:self.x + self.width, self.y:self.y + self.height] = self.color




canvas = Canvas(20,20,[255, 255, 255])
rec = Rectangle(x=10, y=10, width=5, height=8, color=[255, 0, 0])
rec.draw(canvas)
canvas.make()

