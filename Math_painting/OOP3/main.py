import numpy as np
from PIL import Image
#
#
# matrix = np.zeros((5, 4, 3), dtype=np.uint8)
# matrix[:] = [255, 255, 0]
#
# img = Image.fromarray(matrix, 'RGB')
# img.save('test.png')
class Square:

    def __init__(self, x, y, side, color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x

    def draw(self, canvas):

        pass

class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        self.y = y
        self.x = x

    def draw(self, canvas):
        pass


        
class Canvas:

    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        # create empty 3D grid

        # change 0,0,0 to users options
        



    def make(self, imagepath):
        pass




