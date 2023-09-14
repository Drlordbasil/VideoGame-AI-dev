import random


class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.attack = 10
        self.defense = 5

    def print_status(self):
        print("Player Information")
        print("===================")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")

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

    def print_status(self):
        print("Enemy Information")
        print("==================")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")


def print_intro():
    print("Welcome to the Python RPG Game!")
    print("===============================")
    print("In this game, you will battle against various enemies.")
    print("Level up, gain powerful weapons, and defeat the final boss!")
    print("May the odds be in your favor!")
    print()


def create_player():
    name = input("Enter your player name: ")
    print()
    print("Player created successfully!")
    print()
    return Player(name)


def battle(player, enemy):
    print(f"A wild {enemy.name} has appeared!")
    print()
    player.print_status()
    print()
    enemy.print_status()
    print()
    while True:
        print(f"{player.name}'s Turn")
        print("----------------")
        print()
        player.attack_enemy(enemy)
        print(f"{player.name} attacked {enemy.name}!")
        enemy.print_status()
        print()
        if enemy.health <= 0:
            print(f"{player.name} defeated {enemy.name}!")
            print()
            player.level_up()
            player.print_status()
            print()
            break
        print(f"{enemy.name}'s Turn")
        print("----------------")
        print()
        enemy.attack_player(player)
        print(f"{enemy.name} attacked {player.name}!")
        player.print_status()
        print()
        if player.health <= 0:
            print(f"{player.name} was defeated by {enemy.name}!")
            print()
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
        input("Press enter to continue...")
        print()
        battle(player, enemy)


if __name__ == '__main__':
    play_game()