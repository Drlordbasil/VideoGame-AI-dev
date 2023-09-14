import random


class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.attack = 10
        self.defense = 5

    def get_status(self):
        return f"Player Information\n===================\nName: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}\n"

    def level_up(self):
        self.level += 1
        self.attack += random.randint(5, 10)
        self.defense += random.randint(3, 8)
        self.health = 100

    def attack_enemy(self, enemy):
        damage = max(0, self.attack - enemy.defense)
        enemy.health -= damage

    def attack_player(self, player):
        damage = max(0, self.attack - player.defense)
        player.health -= damage


class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = 100 + level * 10
        self.attack = 5 + level * 2
        self.defense = 3 + level

    def get_status(self):
        return f"Enemy Information\n==================\nName: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}\n"


def print_intro():
    print("Welcome to the Python RPG Game!")
    print("===============================")
    print("In this game, you will battle against various enemies.")
    print("Level up, gain powerful weapons, and defeat the final boss!")
    print("May the odds be in your favor!")
    print()


def create_player():
    name = input("Enter your player name: ")
    print("\nPlayer created successfully!\n")
    return Player(name)


def battle(player, enemy):
    print(f"A wild {enemy.name} has appeared!\n")
    print(player.get_status())
    print(enemy.get_status())

    while True:
        print(f"{player.name}'s Turn\n----------------\n")
        player.attack_enemy(enemy)
        print(f"{player.name} attacked {enemy.name}!")
        print(enemy.get_status())

        if enemy.health <= 0:
            print(f"{player.name} defeated {enemy.name}!\n")
            player.level_up()
            print(player.get_status())
            break

        print(f"{enemy.name}'s Turn\n----------------\n")
        enemy.attack_player(player)
        print(f"{enemy.name} attacked {player.name}!")
        print(player.get_status())

        if player.health <= 0:
            print(f"{player.name} was defeated by {enemy.name}!\n")
            break


def play_game():
    print_intro()
    player = create_player()
    enemies = [
        Enemy("Zombie", 1),
        Enemy("Skeleton", 2),
        Enemy("Dragon", 5),
        Enemy("Giant", 10),
        Enemy("Final Boss", 100)
    ]

    for enemy in enemies:
        input("Press enter to continue...\n")
        battle(player, enemy)


if __name__ == '__main__':
    play_game()