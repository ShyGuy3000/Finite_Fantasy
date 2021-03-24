########################
#   IMPORTED MODULES   #
########################
import random
import time
import os


####################
#   DECLARATIONS   #
####################
def clear_screen():
    # Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Mac/Linux
    else:
        _ = os.system('clear')


def print_pause(story_message):
    print(story_message)
    time.sleep(2)


# This function creates two enemies at random from a list, but ensures that the
# two enemies are unique. It creates the initial inventory.
def game_setup():
    global enemy1
    global enemy2
    global inventory
    inventory = ["staff"]
    enemies = ["mystic dragon", "golem", "kraken", "lich fiend", "magic slime",
               "pentacorn", "gryphon"]
    enemy1 = random.choice(enemies)
    enemy2 = random.choice(enemies)
    while enemy2 == enemy1:
        enemy2 = random.choice(enemies)


# This function  provides the story introduction for our hero.
def story_introduction():
    print_pause("Your travels have brought you to this region in search of "
                "the legendary World Jewel.")
    print_pause("You approach a quiet looking meadow, with a soft breeze "
                "rustling the grass.")
    print_pause("A friendly barkeep in the previous town warned of monsters "
                "lurking nearby.")
    print_pause(f"You have a worn travelling {inventory[0]} to provide little "
                "safety.")
    print_pause("You see a forest due north, a beach to the west, and a cave "
                "far east.")


# This function deals with the three (3) primary choices for adventuring from
# the crossroads.
def adventure_time():
    print_pause("You're at the crossroads, which path will you take?")
    hero_path = input("1. North\n"
                      "2. West\n"
                      "3. East\n"
                      "(You may enter the number or direction.)\n").lower()
    if hero_path in ['1', 'north', 'n']:
        if "sword" in inventory:
            print_pause("You return for another view of the forest clearing.")
            print_pause("While calming, there is nothing more here.")
            adventure_time()
        else:
            print_pause("You cautiously enter the dark forest.")
            print_pause("Eventually, you come upon an open clearing, with a "
                        "brilliant sword lodged in an auspicious-looking "
                        "pedestal.")
            print_pause("This must be the fabled Sword of Mastery!!")
            print_pause("You firmly grasp the sword and begin to remove it...")
            print_pause("You triumphantly remove the sword from its resting "
                        "place, casting aside your nigh-broken staff.")
            inventory[0] = "sword"
            print_pause("With sword in hand, you press onward.")
            adventure_time()
    elif hero_path in ['2', 'west', 'w']:
        if "shield" in inventory:
            print_pause("The sparkling beach is a tranquil sight, but there "
                        "is nothing more for you here in your travels.")
            print_pause("You decide to head back.")
            adventure_time()
        else:
            print_pause("You follow the signs leading to the clear sands of "
                        "the beach.")
            print_pause("While traversing the beach, you step on a stone"
                        "plate!")
            print_pause("To your surprise, a stone structure rises from the "
                        "sand!")
            print_pause("There is an opening, but as you approach to enter, "
                        f"you are assailed by a {enemy1}!")
            not_so_random_battle(1, enemy1)
    elif hero_path in ['3', 'east', 'e']:
        print_pause("You slowly enter the cave, observing sconces lit along "
                    "the walls.")
        print_pause("Moving deeper into the cave, you enter an open room.")
        print_pause("You focus your gaze, and realize in the center of the "
                    f"room is a towering {enemy2}!")
        print_pause(f"Before you can think, the {enemy2} lunges in your "
                    "direction!")
        not_so_random_battle(2, enemy2)
    else:
        print_pause("Silly hero, do not tarry! Choose a correct response.")
        adventure_time()


# Primary battle layout used, which plays out the scenarios for each battle,
# which are function calls of their own.
def not_so_random_battle(scenario, current_enemy):
    print_pause("Do you wish to fight or flee?")
    battle_choice = input("1. Attack!\n"
                          "2. Run away...\n"
                          "(You may enter the number or command.)\n").lower()
    if battle_choice in ['1', 'attack']:
        if scenario == 1:
            first_battle()
        elif scenario == 2:
            second_battle()
    elif battle_choice in ['2', 'run', 'run away', 'flee']:
        print_pause("Fearing for your life, you beat a hasty retreat.")
        print_pause(f"The {current_enemy} loses interest and doesn't pursue.")
        adventure_time()
    else:
        print_pause("Choose quickly (and correctly)!")
        not_so_random_battle(scenario, current_enemy)


def first_battle():
    print_pause(f"As the {enemy1} approaches, you ready your {inventory[0]}.")
    if "sword" in inventory:
        print_pause("Your blade shines brightly, and as you swing mightily, "
                    f"the {enemy1} is cleaved in twain.")
        print_pause("Beyond your slain foe, you spot a welcome sight: an "
                    "ornate-looking treasure chest!")
        print_pause("You slowly open the chest...")
        print_pause("Finding a stalwart mythril shield!")
        inventory.append("shield")
        print_pause(f"You happily equip your {inventory[1]}, and continue on "
                    "your journey.")
        adventure_time()
    elif "staff" in inventory:
        print_pause(f"You hold up your {inventory[0]} to deflect your foe's "
                    "assault, but are simply rent asunder.")
        print_pause("You perish in battle, your journey incomplete...")


def second_battle():
    print_pause(f"As the {enemy2} approaches, you ready yourself for battle!")
    print_pause("Before you can attack, the monster launches a magical volley "
                "in your direction!")
    if "shield" in inventory:
        print_pause(f"You raise your {inventory[1]}, effortlessly deflecting "
                    "the attack.")
        print_pause(f"During this opening, you draw your {inventory[0]} and "
                    f"strike a lethal blow into the {enemy2}'s heart.")
        print_pause("As the monster fades away, left behind is a sparkling "
                    "crystal...")
        print_pause("You have found the legendary World Jewel!!")
        print_pause("You saved the kingdom and brought everlasting peace!")
        print_pause("")
        print_pause("FIN")
        print_pause("")
    else:
        print_pause("With no means to shield yourself, the attack finds its "
                    "mark, destroying your life essence in the process.")
        print_pause("You perish in battle, your journey incomplete...")


def play_again():
    quest_continue = True
    print_pause("Would you like to play again?")
    player_choice = input("1. Yes\n"
                          "2. No\n"
                          "(You may enter the number or command.)\n").lower()
    if player_choice in ['1', 'yes', 'y']:
        print_pause("The tale shall start anew.")
        print_pause("")
        quest = 'in_progress'
        clear_screen()
        return quest
    elif player_choice in ['2', 'no', 'n']:
        print_pause("Thank you for playing!")
        quest = 'the_end'
        return quest


def full_game():
    quest = 'in_progress'
    while quest == 'in_progress':
        game_setup()
        story_introduction()
        adventure_time()
        quest = play_again()


#####################
#   PROGRAM START   #
#####################
full_game()
