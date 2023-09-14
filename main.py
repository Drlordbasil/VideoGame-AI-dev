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
        enemy.health = max(0, enemy.health)

    def attack_player(self, player):
        damage = max(0, self.attack - player.defense)
        player.health -= damage
        player.health = max(0, player.health)


class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = random.randint(50, 100)
        self.attack = random.randint(5, 10) * level
        self.defense = random.randint(1, 5) * level

    def print_status(self):
        print("Enemy Information")
        print("==================")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")


class Game:
    def __init__(self):
        self.player = None
        self.enemies = [
            Enemy("Zombie", 1),
            Enemy("Skeleton", 2),
            Enemy("Dragon", 5),
            Enemy("Giant", 10),
            Enemy("Final Boss", 100)
        ]

    def print_intro(self):
        print("Welcome to the Python RPG Game!")
        print("================================")
        print("In this game, you will battle against various enemies.")
        print("Level up, gain powerful weapons, and defeat the final boss!")
        print("May the odds be in your favor!")
        print()

    def create_player(self):
        name = input("Enter your player name: ")
        self.player = Player(name)
        print()
        print("Player created successfully!")
        print()
        self.player.print_status()
        print()

    def battle(self, enemy):
        print(f"A wild {enemy.name} has appeared!")
        print()
        while True:
            print(f"{self.player.name}'s Turn")
            print("----------------")
            print()
            self.player.attack_enemy(enemy)
            print(f"{self.player.name} attacked {enemy.name}!")
            enemy.print_status()
            print()
            if enemy.health <= 0:
                print(f"{self.player.name} defeated {enemy.name}!")
                print()
                self.player.level_up()
                self.player.print_status()
                print()
                break
            print(f"{enemy.name}'s Turn")
            print("----------------")
            print()
            enemy.attack_player(self.player)
            print(f"{enemy.name} attacked {self.player.name}!")
            self.player.print_status()
            print()
            if self.player.health <= 0:
                print(f"{self.player.name} was defeated by {enemy.name}!")
                print()
                break

    def play_game(self):
        self.print_intro()
        self.create_player()
        for enemy in self.enemies:
            input("Press enter to continue...")
            print()
            self.battle(enemy)


if __name__ == "__main__":
    game = Game()
    game.play_game()