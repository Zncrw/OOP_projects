import numpy as np
from PIL import Image


class Square:
    """
    class that will draw a square based on users input
    """

    def __init__(self, x, y, side, color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x



    def draw(self, canvas):
        """
        method, that will draw a square on base canvas
        :param canvas: user defined canvas
        :return: square drawing
        """
        canvas.matrix[self.x:self.x + self.side, self.y:self.y + self.side] = self.color


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

    def make(self, image_path):
        """
        method that will save final img
        """
        img = Image.fromarray(self.matrix, 'RGB')
        img.save(f'{image_path}.png')

canvas = Canvas(20,20,[255, 255, 255])
rec = Rectangle(x=10, y=10, width=5, height=8, color=[255, 0, 0])
square = Square(x=1, y=1, side=5,color=[255, 0, 0])
rec.draw(canvas)
square.draw(canvas)
canvas.make('Test')