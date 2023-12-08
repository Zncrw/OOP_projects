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
        pass


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
        """
        method that will draw rectangle on canvas
        """
        pass

        
class Canvas:
    """
    class that will make a canvas after getting user input
    """
    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width

        # create empty 3D grid
        self.matrix = np.zeros((5, 4, 3), dtype=np.uint8)

        # change 0,0,0 to users options
        self.matrix[:] = self.color

    def make(self, imagepath):
        """
        method that will save final img
        """
        img = Image.fromarray(self.matrix, 'RGB')
        img.save(f'{imagepath}.png')
