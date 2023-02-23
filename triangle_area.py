class Triangle:

    def __init__(self, height="0", base="0"):
        self.height = height
        self.base = base

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            self.__height = value

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value):

        if isinstance(value, int):
            self.__base = value

    def area(self):
        return (int(self.__height) * (int(self.__base))) / 2


def main():
    triangle = Triangle()

    while True:
        try:
            height = float(input("Enter the height value: "))
            break
        except ValueError:
            print("\033[1;31mHeight MUST be a whole number\033[0m\n")

    while True:
        try:
            base = float(input("Enter the base value: "))
            break
        except ValueError:
            print("\033[1;31mbase MUST be a whole number\033[0m\n")

    triangle.height = height
    triangle.base = base

    print("height: ", triangle.height)

    print("base: ", triangle.base)

    print("\nThe area of the Triangle: ", triangle.area())


main()