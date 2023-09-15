# trying to make random rectangle object guessing game
import random
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def in_rectangle(self, rectangle) -> bool:
        """
        function checking if point lies in rectangle.
        :param rectangle: random generated rectangle object.
        :return: Bool if guessed point is in rectangle or not.
        """

        if (rectangle.coordinate1.x < self.x < rectangle.coordinate2.x and
                rectangle.coordinate1.y < self.y < rectangle.coordinate2.y):
            return True
        else:
            return False

    def point_drawing(self):
        """
        function will draw a point in turtle graph
        :return: point
        """
        t = turtle.Turtle()
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.dot(5)
        t.hideturtle()


class Rectangle:

    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def turtle_drawing(self):
        """
        function will draw o rectangle based on random generated points
        :return: drawing of rectangle
        """
        a = self.coordinate1.x - self.coordinate2.x
        b = self.coordinate1.y - self.coordinate2.y
        t = turtle.Turtle()
        t.forward(a)  # a = length of first side
        t.left(90)   # Turn turtle by 90 degree
        t.forward(b)  # b length of second side
        t.left(90)
        t.forward(a)
        t.left(90)
        t.forward(b)
        return t


def main():
    # make random rectangle
    rectangle = Rectangle(Point(random.randint(0, 9), random.randint(0, 9)),
                          Point(random.randint(10, 19), random.randint(10, 19)))
    # for testing purposes I will print coordinates of rectangle
    print(f'X:{rectangle.coordinate1.x}, Y:{rectangle.coordinate1.y} - '
          f'X:{rectangle.coordinate2.x},Y{rectangle.coordinate2.y}')

    user_x = int(input('Guess x coordinate: '))
    user_y = int(input('Guess y coordinate: '))
    user_point = Point(user_x, user_y)
    print(user_point.in_rectangle(rectangle))
    print(rectangle.turtle_drawing(), user_point.point_drawing())
    turtle.exitonclick()


if __name__ == '__main__':
    main()
