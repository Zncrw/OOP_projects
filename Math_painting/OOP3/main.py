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


def get_color(color: str) -> list:
    """
    function to get color for RGB values
    :param color: string of user
    :return: list with RGB values
    """
    if color in ['red', 'r']:
        return [255, 0, 0]
    if color in ['blue', 'b']:
        return [0, 0, 255]
    if color in ['green', 'g']:
        return [0, 255, 0]


def main():

    color_user = input('Choose background color for canvas W for white / B for black: ')
    if color_user.lower() in ['black', 'b', 'balck']:
        color_user = [0, 0, 0]
    elif color_user.lower() in ['white', 'w']:
        color_user = [255, 255, 255]
    else:
        print('Invalid color entered. Please choose W for white or B for black.')
        color_user = input('Choose background color for canvas W for white / B for black: ')
    while True:
        try:
            canvas = Canvas(width=int(input('Enter canvas width: ').strip()),
                            height=int(input('Enter canvas height: ').strip()),
                            color=color_user)
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

    next_drawing = True
    while next_drawing is True:
        ask_user = input('What do you want to draw? square/rectangle? Enter quit for quit: ')

        if ask_user.lower() in ['rectangle', 'r']:
            # make an object with user input
            rec = Rectangle(
                x=int(input('Enter x point: ')),
                y=int(input('Enter y point: ')),
                width=int(input('Enter width: ')),
                height=int(input('Enter height: ')),
                color=get_color(input('Choose color: red/green/blue: '))
            )
            # draw rectangle on canvas
            rec.draw(canvas)

        if ask_user.lower() in ['square', 's']:
            square = Square(
                x=int(input('Enter x point: ')),
                y=int(input('Enter y point: ')),
                side=int(input('Enter length of side: ')),
                color=get_color(input('Choose color: red/green/blue: '))
            )
            # draw square on canvas
            square.draw(canvas)

        elif ask_user.lower() in ['quit', 'q', 'exit']:
            canvas.make(input('Type name of file: '))
            break


if __name__ == '__main__':
    main()
