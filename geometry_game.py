# trying to make random rectangle object guessing game
import random
import turtle


class Point:
    """
    class made to take point x,y
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def in_rectangle(self, rectangle) -> bool:
        """
        function checking if point lies in rectangle.
        :param rectangle: random generated rectangle object.
        :return: Bool if guessed point is in rectangle or not.
        """
        # checking if user input is between the rectangle points
        if (rectangle.coordinate1.x < self.x < rectangle.coordinate2.x and
                rectangle.coordinate1.y < self.y < rectangle.coordinate2.y):
            return True
        else:
            return False

    def point_drawing(self):
        """
        function will draw a point in turtle graph.
        :return: point based on user input
        """
        t = turtle.Turtle()
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.dot(5, 'green')
        t.hideturtle()


class Rectangle:
    """
    class creating rectangle, need 2 arguments
    """

    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def turtle_drawing(self):
        """
        function will draw o rectangle based on random generated points
        :return: drawing of rectangle
        """
        a = self.coordinate2.x - self.coordinate1.x
        b = self.coordinate2.y - self.coordinate1.y
        t = turtle.Turtle()
        t.forward(a)  # a = length of first side
        t.left(90)   # Turn turtle by 90 degree
        t.forward(b)  # b length of second side
        t.left(90)
        t.forward(a)
        t.left(90)
        t.forward(b)
        return t


def check_input(prompt):
    """
    function checking users input
    :param prompt: prompt sentece
    :return: valid input (integer)
    """
    while True:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print('Wrong value, you must type an integer. Try again.')


def random_cord() -> int:
    """
    generating random numbers
    :return: random integer
    """
    return random.randint(0, 9)


def main():
    # make random rectangle
    rectangle = Rectangle(Point(random_cord(), random_cord()),
                          Point((random_cord() + 10), (random_cord()+10)))
    # for testing purposes I will print coordinates of rectangle
    print(f'X:{rectangle.coordinate1.x}, Y:{rectangle.coordinate1.y} - '
          f'X:{rectangle.coordinate2.x},Y{rectangle.coordinate2.y}')

    user_x = check_input('What is X coord: ')
    user_y = check_input('What is Y coord: ')

    user_point = Point(user_x, user_y)
    # print out if user was lucky and hit the spot
    print(user_point.in_rectangle(rectangle))
    # printing GUI
    print(rectangle.turtle_drawing(), user_point.point_drawing())
    turtle.exitonclick()


if __name__ == '__main__':
    main()
