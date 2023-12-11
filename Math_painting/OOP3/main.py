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

def main():
    color_user = input('Choose background color for canvas W for white / B for black: ')
    if color_user.lower() == 'black' or color_user == 'b':
        color_user = [0, 0, 0]
    else:
        color_user = [255, 255, 255]

    canvas = Canvas(width=int(input('Enter canvas width: ')),
                    height=int(input('Enter canvas height: ')),
                    color=color_user)

    next_drawing = True
    while next_drawing is True:
        ask_user = input('What do you want to draw? square/rectangle? Enter quit for quit: ')

        if ask_user.lower() == 'rectangle':
            rec_color = input('Choose color: red/green/blue: ')
            if rec_color == 'red':
                rec_color = [255, 0, 0]
            if rec_color == 'blue':
                rec_color = [0, 0, 255]
            if rec_color == 'green':
                rec_color = [0, 255, 0]
            # make an object with user input
            rec = Rectangle(
                x=int(input('Enter x point: ')),
                y=int(input('Enter y point: ')),
                width=int(input('Enter width: ')),
                height=int(input('Enter height: ')),
                color=rec_color
            )
            # draw rectangle on canvas
            rec.draw(canvas)

        if ask_user.lower() == 'square':
            square_color = input('Choose color: red/green/blue: ')
            if square_color == 'red':
                square_color = [255, 0, 0]
            if square_color == 'blue':
                square_color = [0, 0, 255]
            if square_color == 'green':
                square_color = [0, 255, 0]
            square = Square(
                x=int(input('Enter x point: ')),
                y=int(input('Enter y point: ')),
                side=int(input('Enter lenght of side: ')),
                color=square_color
            )
            square.draw(canvas)

        elif ask_user.lower() == 'quit':
            canvas.make(input('Type name of file: '))
            next_drawing = False
            break


if __name__ == '__main__':
    main()











