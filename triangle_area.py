class Triangle:

    def __init__(self, height="0", base="0"):
        self.height = height
        self.base = base

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value):

        if value.isdigit():
            self.__base = value

    def area(self):
        return (int(self.__height) * (int(self.__base))) / 2


def main():
    triangle = Triangle()

    print("Height MUST be a whole number else height will be zero\n")
    height = input("Enter the height value: ")

    print("\nbase MUST be a whole number else base will be zero\n")
    base = input("Enter the base value: ")

    triangle.height = height
    triangle.base = base

    print("\nheight: ", triangle.height)

    print("base: ", triangle.base)

    print("\nThe area of the Triangle: ", triangle.area())


main()
