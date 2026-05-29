name = input("Player Name:  ")
attack = int(input("Attack :"))
defense = int(input("Defense :"))
hp = int(input("HP :"))
speed = int(input("Speed :"))
magic = int(input("Magic :"))
enemy_name = input("Enemy Name: ")
enemy_health = int(input("Enemy HP: "))
enemy_attack = int(input("Enemy Attack: "))
enemy_rank = input("Enemy Rank: ")

power = attack*2 + defense + hp + speed + magic*2

if attack > 80:
    print("CRITICAL HIT ACTIVATED")
    power += 20

if enemy_rank == "S":
    enemy_attack += 50

def attack_enemy(enemy_health, power):
    enemy_health = enemy_health - power
    return enemy_health

def enemy_turn(hp,enemy_attack,enemy_name):
    hp = hp - enemy_attack
    print(f"{enemy_name} attacked {name} for {enemy_attack} damage")
    return hp
hits = 0
while enemy_health > 0 and hp > 0:
    hits += 1
    enemy_health = attack_enemy(enemy_health, power)
    if enemy_health < 0:
        enemy_health = 0
    if enemy_health == 0:
        break
    hp = enemy_turn(hp,enemy_attack,enemy_name)
    if hp < 0:
        hp = 0

    print(f"Attack {hits}")
    print(f"Enemy HP : {enemy_health}")
    print(f"Player HP : {hp}")
    print("----------------")

if hp > 0 and enemy_health == 0:
    print("VICTORY")
    win = 1

else:
    print("DEFEAT")
    win=0

if power >= 200 and win==1:
    print(f"{name} is a S-RANK HUNTER")

elif power >= 150 and win==1:
    print(f"{name} is a A-RANK HUNTER")

elif power >= 100 and win==1:
    print(f"{name} is a B-RANK HUNTER")

else:
    print(f"{name} is a C-RANK HUNTER")