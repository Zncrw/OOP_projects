# trying to make random rectangle object guessing game
import random


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


class Rectangle:

    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2


def main():
    # make random rectangle
    rectangle = Rectangle(Point(random.randint(0, 9), random.randint(0, 9)),
                          Point(random.randint(10, 19), random.randint(10, 19)))
    # for testing purposes I will print coordinates of rectangle
    print(f'X:{rectangle.coordinate1.x}, Y:{rectangle.coordinate1.y} - '
          f'X:{rectangle.coordinate2.x},Y{rectangle.coordinate2.y}')
    print(rectangle)

    user_x = int(input('Guess x coordinate: '))
    user_y = int(input('Guess y coordinate: '))
    user_point = Point(user_x, user_y)
    print(user_point.in_rectangle(rectangle))


if __name__ == '__main__':
    main()
