
import random

#weapon_list = [dagger, sword, spear, bow, battle_axe, mace, lance]
#example = [damage, attack_speed, unit_range, "weapon name"]
dagger = [5, 1, 1, "dagger"]
sword = [8, 2, 2, "sword"]
spear = [11, 4, 6, "spear"]
bow = [14, 3, 20, "bow"]
battle_axe = [16, 6, 3, "battle axe"]
mace = [21, 8, 4, "mace"]
lance = [34, 6, 5, "lance"]
javelin = [13, 8, 15, "javelin"]

#armor_list = [leather, chain, iron]
leather = [10]
chain = [25]
iron = [35]

#horse_armor_list = [leather_horse, chain_horse, iron_horse]
leather_horse = [10]
chain_horse = [25]
iron_horse = [35]

horse_health = 200
health = 100
damage = 12
strength = 5
attack_speed = 5
unit_range = 2
alive = True


def die(sides, plus):
    result = random.randint(1, sides) + plus
    return result


def fight(name1, name2):
    p1 = name1
    p2 = name2
    p1_hp = health
    p2_hp = health
    while p1_hp >= 1 or p2_hp >= 1:
        roll = die(damage, strength)
        print(p1 + " dealt " + str(roll) + " damage to " + p2)
        p2_hp = p2_hp - roll
        roll = die(damage, strength)
        print(p2 + " dealt " + str(roll) + " damage to " + p1)
        p1_hp = p1_hp - roll
        if p1_hp < 1:
            print(p2 + " has won")
            break

        if p2_hp < 1:
            print(p1 + " has won")
            break


fight('superman', 'batman')

