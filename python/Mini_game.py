import random

player_name = input("What is your name? ")
player_hp = 100
boss_name = "Evil Boss"
boss_hp = 200
turn = 1

print(f"{boss_name} has appeared! Prepare to fight, {player_name}!")

while player_hp > 0 and boss_hp > 0:
    print(f"\nTurn {turn}:")
    print(f"{player_name}'s HP: {player_hp}")
    print(f"{boss_name}'s HP: {boss_hp}")
    action = input("What will you do? [attack/defend/heal] ").lower()
    
    if action == "attack":
        damage = random.randint(10, 20)
        boss_hp -= damage
        print(f"You attack {boss_name} for {damage} damage!")
        boss_action = random.choice(["attack", "defend"])
        if boss_action == "attack":
            damage = random.randint(15, 25)
            player_hp -= damage
            print(f"{boss_name} attacks you for {damage} damage!")
        else:
            print(f"{boss_name} defends.")
    elif action == "defend":
        damage = random.randint(5, 10)
        player_hp -= damage
        print(f"{boss_name} attacks you for {damage} damage!")
        boss_action = random.choice(["attack", "defend"])
        if boss_action == "attack":
            damage = random.randint(15, 25)
            player_hp -= damage
            print(f"{boss_name} attacks you for {damage} damage!")
        else:
            print(f"{boss_name} defends.")
    elif action == "heal":
        heal = random.randint(10, 15)
        player_hp += heal
        print(f"You heal yourself for {heal} HP!")
        boss_action = random.choice(["attack", "defend"])
        if boss_action == "attack":
            damage = random.randint(15, 25)
            player_hp -= damage
            print(f"{boss_name} attacks you for {damage} damage!")
        else:
            print(f"{boss_name} defends.")
    else:
        print("Invalid action. Try again.")
        continue
    
    turn += 1
    
if player_hp <= 0:
    print("You have been defeated. Game over.")
elif boss_hp <= 0:
    print(f"{boss_name} has been defeated! Congratulations, {player_name}!")