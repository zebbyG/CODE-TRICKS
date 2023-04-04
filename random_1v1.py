from colorama import init, Fore, Style
import random
import time

init()


print(Fore.LIGHTBLUE_EX + "\nWelcome to 1v1 with random enemies\n" + Style.RESET_ALL)

print(Fore.LIGHTGREEN_EX + "Getting ready...\n" + Style.RESET_ALL)
time.sleep(3.5)
enemies = ["Lion", "Thanos", "Assassin", "Zombie", "Spider", "Snake", "Thief"]

global name
for e in enemies:
    try:
        name = input(Fore.LIGHTMAGENTA_EX + "Enter game user-name?\n\n>>> " + Style.RESET_ALL)
        if name in enemies:
            raise ValueError
        break
    except ValueError:
        print(Fore.RED + "user-name is taken try another user-name" + Style.RESET_ALL)

choose_enemy = random.choice(enemies)
time.sleep(1)
print(Fore.YELLOW + f"Welcome {name} a random attacker is coming...\n")
time.sleep(2.5)
print(Fore.RED + f"{choose_enemy} appeared!\n\n" + Style.RESET_ALL)

player = 100
opponent = 100

# Your attack

while player > 1:
    time.sleep(1)
    print("==================")
    print(" ")
    print(Fore.BLUE + f"{name}'s life: {player}%\n" +
          Fore.YELLOW + f"{choose_enemy}'s life: {opponent}%" + Style.RESET_ALL)
    print(" ")
    time.sleep(1)
    print(Fore.LIGHTGREEN_EX + "What will you do?" + Style.RESET_ALL)
    attack = int(input("1: Normal attack\n2: Risk special attack\n3: Recover life\n\n>>> "))
    print(" ")

    if attack == 1:
        attack1 = random.randint(16, 19)
        print(Fore.LIGHTGREEN_EX + f"{attack1}% of {choose_enemy}'s life damaged")
        opponent = opponent - attack1
        time.sleep(1.5)
        print(Fore.YELLOW + f"{choose_enemy} have {opponent}% life now!\n" + Style.RESET_ALL)

    elif attack == 2:
        attack2 = random.randint(1, 2)

        if attack2 == 1:
            time.sleep(1)
            chance1 = random.randint(21, 29)
            print(Fore.LIGHTGREEN_EX + f"{chance1}% of {choose_enemy}'s life damaged")
            opponent = opponent - chance1
            time.sleep(1.5)
            print(Fore.YELLOW + f"{choose_enemy} have {opponent}% life now!" + Style.RESET_ALL)
            print(" ")

        else:
            print(Fore.RED + f"{choose_enemy} countered...no damage taken" + Style.RESET_ALL)

    elif attack == 3:
        attack3 = random.randint(17, 23)
        print(Fore.GREEN + f"You recovered {attack3}% of life!" + Style.RESET_ALL)
        time.sleep(1.5)
        player = player + attack3
        print(f"You have {player}% life now!")

        # Win or lose

    if player < 1:
        time.sleep(1)
        print(Fore.YELLOW + f"{choose_enemy} wins with {opponent}% life!!! {name} life is {player}%")
        time.sleep(2)
        break

    elif opponent < 1:
        time.sleep(1)
        print(Fore.BLUE + f"{name} wins with {player}% life!! {choose_enemy} life  is {opponent}%")
        time.sleep(2)
        break

        # enemy attack

    print("==================")
    print(Fore.LIGHTMAGENTA_EX + f"{choose_enemy} time!" + Style.RESET_ALL)
    print("==================")
    time.sleep(3)
    print(" ")

    opp_chance = random.randint(1, 3)

    if opp_chance == 1:
        time.sleep(2.5)
        opp_chance1 = random.randint(11, 15)
        print(Fore.LIGHTRED_EX + f"{opp_chance1}% of {name}'s life is damaged!!")
        player = player - opp_chance1
        time.sleep(1.5)
        print(Fore.YELLOW + f"You have {player}% life now!" + Style.RESET_ALL)
        print(" ")

    elif opp_chance == 2:
        time.sleep(1.5)
        opp_chance2 = random.randint(1, 2)

        if opp_chance2 == 1:
            time.sleep(2.5)
            damage2 = random.randint(19, 25)
            print(Fore.LIGHTRED_EX + f"{damage2}% of {name}'s life is damaged!!")
            player = player - damage2
            time.sleep(1.5)
            print(Fore.YELLOW + f"You have {player}% life now!")
            print(" ")
        else:
            print(Fore.GREEN + "You countered no damage taken" + Style.RESET_ALL)

    elif opp_chance == 3:
        time.sleep(2.5)
        opp_chance3 = random.randint(15, 20)
        print(Fore.YELLOW + f"{choose_enemy} recovered {opp_chance3}% life!")
        time.sleep(1.5)
        opponent = opponent + opp_chance3
        print(Fore.LIGHTRED_EX + f"{choose_enemy} has {opponent}% life now!" + Style.RESET_ALL)

    print(" ")
