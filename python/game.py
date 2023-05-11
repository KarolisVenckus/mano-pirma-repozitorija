import random
import sys
import time


class Character:
    def __init__(self, name, max_health, attack_power, defense_power):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack_power = attack_power
        self.defense_power = defense_power

    def attack(self, other):
        damage = self.attack_power - other.defense_power
        if damage > 0:
            other.health -= damage
            print(f"{self.name} attacked {other.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack was blocked by {other.name}!")

    def defend(self):
        self.defense_power += 2
        print(f"{self.name} is defending!")

    def is_alive(self):
        return self.health > 0

    def reset(self):
        self.health = self.max_health
        self.defense_power = 0

    def heal(self):
        if self.health == self.max_health:
            print(f"{self.name}'s health is already full!")
        else:
            self.health += 10
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"{self.name} healed for 10 HP! Current health: {self.health}/{self.max_health}")


class Enemy(Character):
    def __init__(self, name, max_health, attack_power, defense_power, reward):
        super().__init__(name, max_health, attack_power, defense_power)
        self.reward = reward

    def choose_action(self):
        options = ["attack", "defend"]
        if self.health < self.max_health:
            options.append("heal")
        return random.choice(options)

    def do_action(self, other):
        action = self.choose_action()
        if action == "attack":
            self.attack(other)
        elif action == "defend":
            self.defend()
        elif action == "heal":
            self.heal()


class Game:
    def __init__(self, player_name):
        self.player = Character(player_name, 100, 10, 5)
        self.enemies = [
            Enemy("Goblin", 50, 5, 2, 10),
            Enemy("Orc", 100, 10, 5, 20),
            Enemy("Dragon", 200, 20, 10, 50)
        ]

    def run(self):
        print("Welcome to the game!\n")
        time.sleep(1)

        while True:
            enemy = random.choice(self.enemies)
            print(f"You encountered a {enemy.name}!\n")
            time.sleep(1)

            while enemy.is_alive() and self.player.is_alive():
                print(f"Your health: {self.player.health}/{self.player.max_health}\n")
                time.sleep(1)
                print(f"{enemy.name}'s health: {enemy.health}/{enemy.max_health}\n")
                time.sleep(1)

                action = input("Do you want to attack (a), defend (d), heal (h), or quit (q)? ")
                if action == "a":
                    self.player.attack(enemy)
                elif action == "d":
                    self.player.defend()
                elif action == "h":
                    self.player.heal()
                elif action == "q":
                    sys.exit()
                else:
                    print("Invalid action!")
                    continue

                if enemy.is_alive():
                    enemy.do_action(self.player)
                    time.sleep(1)

                if self.player.is_alive():
                    print(f"You defeated the {enemy.name} and gained {enemy.reward} gold!")
                    self.player.reset()
                else:
                    print("You died!")
                    break


                print("1. Play Game")
                print("2. Exit Game")

            while True:
                choice = input("Enter your choice: ")
                if choice == "1":
                    game = Game("Player")
                    game.run()
                elif choice == "2":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice!")
                    continue


if __name__ == '__main__':
    main()       