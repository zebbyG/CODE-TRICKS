import pyautogui as pg
from colorama import init, Fore, Style
import time

init()


def type_inputs(statement, number_of_statements: int, delay):
    """
    :param statement: What to be printed
    :param number_of_statements: Number of times your statement will be printed
    :param delay: the time taken to be print the statement * number_of_statements
    """
    for num in range(number_of_statements):
        pg.write(statement)
        time.sleep(delay)
        pg.press('Enter')


print(Fore.LIGHTMAGENTA_EX + "Enter how many times you want your statement to be printed[enter a number]\n"
      + Style.RESET_ALL)
times_statement_printed = int(input())

print(Fore.LIGHTGREEN_EX + "Enter the intervals your statement will be printed in(in seconds)")
intervals = float(input())

print(Fore.LIGHTBLUE_EX + "\nType in your statement\n" + Style.RESET_ALL)
message = input()

print(Fore.YELLOW + "The program will run in 5 secs" + Style.RESET_ALL)
time.sleep(5)

type_inputs(message, times_statement_printed, intervals)
