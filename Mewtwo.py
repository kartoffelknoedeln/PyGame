import time
import numpy as np
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Pokemon:
    def __init__(self, name, types, moves, EVs, health, status, battle):
        self.name = name
        self.types = types
        self.move_name = moves['MOVE NAME']
        self.move_type = moves['MOVE TYPE']
        self.move_power = moves['MOVE POWER']
        self.move_accuracy = moves['MOVE ACCURACY']
        self.move_physpc = moves['MOVE PHYSPC']
        self.move_stab = moves['MOVE STAB']
        self.hp = EVs['HP']
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.special = EVs['SPECIAL']
        self.speed = EVs['SPEED']
        self.health = health
        self.status = status
        self.battle = battle

    def fight(self, oppoPokemon):
        print('-----PARTY-----')
        print(f"\n{self.name}")
        print(":L100")
        print("TYPE/", self.types)
        print("STATUS/", self.status)
        print("HP/", self.hp)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("SPECIAL/", self.special)
        print("SPEED/", self.speed)
        print("\nVS\n")

        print('-----MEWTWO-----')
        print(f"\n{oppoPokemon.name}")
        print(":L100")
        print("TYPE/", oppoPokemon.types)
        print("STATUS/", self.status)
        print("HP/", oppoPokemon.hp)
        print("ATTACK/", oppoPokemon.attack)
        print("DEFENSE/", oppoPokemon.defense)
        print("SPECIAL/", oppoPokemon.special)
        print("SPEED/", oppoPokemon.speed)

        time.sleep(2)

        while (self.health > 0) and (oppoPokemon.health > 0):
            string_attack = ''
            type_adv = 1

##---
        
            print(f"\n{self.name}\t\tHP:\t{self.health}/{self.hp}\t\tSTATUS:\t{self.status}")
            print(f"{oppoPokemon.name}\t\tHP:\t{oppoPokemon.health}/{oppoPokemon.hp}\t\tSTATUS:\t{oppoPokemon.status}")

            print(f"\nGo, {self.name}!")
            for i, x in enumerate(self.move_name):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.move_name[index-1]}!")
            time.sleep(1)

            if self.move_name[index-1] == 'Seismic Toss':
                oppoPokemon.health -= 100
            else:
                if self.move_name[index-1] == 'Thunder Wave' or self.move_name[index-1] == 'Sleep Powder':
                    if self.move_name[index-1] == 'Thunder Wave':
                        oppoPokemon.status = 'PRZ'
                        delay_print(f"\n{oppoPokemon.name} has been paralysed!")
                    else:
                        if np.random.choice(4) != 3:
                            oppoPokemon.status = 'SLP'
                            delay_print(f"\n{oppoPokemon.name} has fell asleep!")
                        else:
                            delay_print("\nBut it missed!")
                else:
                    if np.random.choice(101) <= self.move_accuracy[index-1]:
                        modifier = np.random.randint(85, 101)/100
                        critical = 1
                        criticalhit = np.random.choice(4)
                        if self.move_name[index-1] == 'Razor Leaf' and criticalhit == 0:
                            critical = 2
                            delay_print("\nIt's a critical hit!")
                        if self.move_physpc[index-1] == 'Special':
                            dmg_calc_1 = round(((((42) * self.move_power[index-1] * self.special/oppoPokemon.special)/50)+2)*self.move_stab[index-1]*modifier*critical)
                            oppoPokemon.health -= dmg_calc_1
                        else:
                            dmg_calc_1 = round(((((42) * self.move_power[index-1] * self.attack/oppoPokemon.defense)/50)+2)*self.move_stab[index-1]*modifier)
                            oppoPokemon.health -= dmg_calc_1
                        if oppoPokemon.health < 0:
                            oppoPokemon.health = 0
                    else:
                        delay_print("\nBut it missed!")

            time.sleep(1)

##---

            print(f"\n{self.name}\t\tHP:\t{self.health}/{self.hp}\t\tSTATUS:\t{self.status}")
            print(f"{oppoPokemon.name}\t\tHP:\t{oppoPokemon.health}/{oppoPokemon.hp}\t\tSTATUS:\t{oppoPokemon.status}")

            time.sleep(.5)

            if oppoPokemon.health <= 0:
                delay_print("\n... " + oppoPokemon.name + ' has fainted!')
                break

            print(f"\nGo, {oppoPokemon.name}!")
            index = (np.random.choice(4)+1)
            delay_print(f"\n{oppoPokemon.name} used {oppoPokemon.move_name[index-1]}!")
            time.sleep(1)

            status_flip = np.random.choice(2)

            if (oppoPokemon.status == 'PRZ' and status_flip == 0) or (oppoPokemon.status == 'SLP' and status_flip == 0):
                if (oppoPokemon.status == 'PRZ'):
                    delay_print(f"\nBut {oppoPokemon.name} is paralysed!")
                else:
                    delay_print(f"\nBut {oppoPokemon.name} is still asleep!")

            else:
                if oppoPokemon.status == 'SLP':
                    delay_print(f"\nNow {oppoPokemon.name} is awake!")
                    oppoPokemon.status = None
                if np.random.choice(101) <= oppoPokemon.move_accuracy[index-1]:
                    if (index-1) != 3:
                        typing = ['Electric', 'Ice', 'Water', 'Grass/Poison', 'Fire/Flying', 'Psychic']
                        if oppoPokemon.move_type[index-1] == typing[0]:
                            if self.types == typing[0] or self.types == typing[3]:
                                type_adv *= 0.5
                                string_attack = " It's not very effective..."
                            if self.types == typing[2] or self.types == typing[4]:
                                type_adv *= 2
                                string_attack = " It's super effective!"
                        if oppoPokemon.move_type[index-1] == typing[1]:
                            if self.types == typing[2]:
                                type_adv *= 0.5
                                string_attack = " It's not very effective..."
                            if self.types == typing[3] or self.types == typing[4]:
                                type_adv *= 2
                                string_attack = " It's super effective!"
                        if oppoPokemon.move_type[index-1] == typing[5]:
                            if self.types == typing[3]:
                                type_adv *= 2
                                string_attack = " It's super effective!"
                            
                        delay_print(string_attack)

                        modifier = np.random.randint(85, 101)/100
                        dmg_calc_2 = round(((((42) * oppoPokemon.move_power[index-1] * oppoPokemon.special/self.special)/50)+2)*oppoPokemon.move_stab[index-1]*modifier*type_adv)
                        self.health -= dmg_calc_2
                        
                    else:
                        if oppoPokemon.health < 208:
                            oppoPokemon.health += 208
                        else:
                            oppoPokemon.health = 415
                    if self.health < 0:
                        self.health = 0
                else:
                    delay_print("\nBut it missed!")

            time.sleep(1)

            print(f"\n{self.name}\t\tHP:\t{self.health}/{self.hp}\t\tSTATUS:\t{self.status}")
            print(f"{oppoPokemon.name}\t\tHP:\t{oppoPokemon.health}/{oppoPokemon.hp}\t\tSTATUS:\t{oppoPokemon.status}")

            time.sleep(.5)

            if self.health <= 0:
                delay_print("\n... " + self.name + ' has fainted!')
                print()
                print()
                self.battle = False

        if not self.health <= 0:
            exp = np.random.choice(10000)
            delay_print(f"\n{self.name} gained {exp} EXP. points!")

if __name__ == '__main__':
    Pikachu = Pokemon('Pikachu', 'Electric', {'MOVE NAME': ['Thunder', 'Body Slam', 'Surf', 'Thunder Wave'],
                                              'MOVE TYPE': ['Electric', 'Normal', 'Water', 'Electric'],
                                              'MOVE POWER': [120, 85, 95, 0],
                                              'MOVE ACCURACY': [70, 100, 100, 100],
                                              'MOVE PHYSPC': ['Special', 'Physical', 'Special', 'Special'],
                                              'MOVE STAB': [1.5, 1, 1, 1]},
                                             {'HP': 278, 'ATTACK': 208, 'DEFENSE': 158, 'SPECIAL': 198, 'SPEED': 278},
                                             278, None, True)
    Charizard = Pokemon('Charizard', 'Fire/Flying', {'MOVE NAME': ['Fire Blast', 'Body Slam', 'Earthquake', 'Seismic Toss'],
                                                     'MOVE TYPE': ['Fire', 'Normal', 'Ground', 'Fighting'],
                                                     'MOVE POWER': [120, 85, 100, 150],
                                                     'MOVE ACCURACY': [85, 100, 100, 100],
                                                     'MOVE PHYSPC': ['Special', 'Physical', 'Physical', 'Physical'],
                                                     'MOVE STAB': [1.5, 1, 1, 1]},
                                                    {'HP': 359, 'ATTACK': 266, 'DEFENSE': 254, 'SPECIAL': 268, 'SPEED': 298},
                                                    359, None, True)
    Blastoise = Pokemon('Blastoise', 'Water', {'MOVE NAME': ['Hydro Pump', 'Blizzard', 'Earthquake', 'Body Slam'],
                                               'MOVE TYPE': ['Fire', 'Normal', 'Ground', 'Normal'],
                                               'MOVE POWER': [120, 120, 100, 85],
                                               'MOVE ACCURACY': [80, 70, 100, 100],
                                               'MOVE PHYSPC': ['Special', 'Special', 'Physical', 'Physical'],
                                               'MOVE STAB': [1.5, 1, 1, 1]},
                                              {'HP': 361, 'ATTACK': 264, 'DEFENSE': 298, 'SPECIAL': 268, 'SPEED': 254},
                                              361, None, True)
    Venusaur = Pokemon('Venusaur', 'Grass/Poison', {'MOVE NAME': ['Razor Leaf', 'Sleep Powder', 'Vine Whip', 'Body Slam'],
                                                    'MOVE TYPE': ['Grass', 'Normal', 'Grass', 'Normal'],
                                                    'MOVE POWER': [55, 0, 40, 85],
                                                    'MOVE ACCURACY': [95, 75, 100, 100],
                                                    'MOVE PHYSPC': ['Special', 'Special', 'Special', 'Physical'],
                                                    'MOVE STAB': [1.5, 1, 1.5, 1]},
                                                   {'HP': 363, 'ATTACK': 262, 'DEFENSE': 264, 'SPECIAL': 298, 'SPEED': 258},
                                                   363, None, True)
    Mewtwo = Pokemon('Mewtwo', 'Psychic', {'MOVE NAME': ['Psychic', 'Thunder', 'Blizzard', 'Recover'],
                                           'MOVE TYPE': ['Psychic', 'Electric', 'Ice', 'Normal'],
                                           'MOVE POWER': [90, 120, 120, 0],
                                           'MOVE ACCURACY': [100, 70, 70, 100],
                                           'MOVE PHYSPC': ['Special', 'Special', 'Special', 'Attack'],
                                           'MOVE STAB': [1.5, 1, 1, 1]},
                                           {'HP': 415, 'ATTACK': 318, 'DEFENSE': 278, 'SPECIAL': 406, 'SPEED': 358},
                                           415, None, True)

    Pikachu.fight(Mewtwo)
    if Pikachu.battle == False:
        Blastoise.fight(Mewtwo)
        if Blastoise.battle == False:
            Charizard.fight(Mewtwo)
            if Charizard.battle == False:
                Venusaur.fight(Mewtwo)
