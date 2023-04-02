from colorama import init, Fore, Style
import time
init()


def area_triangle(height, base):
    """
    :param height: Triangle height = float(input())
    :param base: Triangle base = float(input())
    :return: (base * height)\2
    """
    return (height * base) * 0.5


while True:
    try:
        print(Fore.LIGHTBLUE_EX + "Enter height value\n" + Style.RESET_ALL)
        height_value = float(input().strip())
        if not isinstance(height_value, (int, float)):
            raise ValueError
        break
    except ValueError:
        print(Fore.RED + "Invalid input\n")

while True:
    try:
        print(Fore.LIGHTBLUE_EX + "Enter base value\n" + Style.RESET_ALL)
        base_value = float(input())
        if not isinstance(base_value, (int,float)):
            raise ValueError
        break
    except ValueError:
        print(Fore.RED + "Invalid input\n")

print(Fore.YELLOW + "calculating...")
time.sleep(1.5)
print(Fore.LIGHTGREEN_EX + f"The area of the triangle is {area_triangle(height_value, base_value):.2f}")
