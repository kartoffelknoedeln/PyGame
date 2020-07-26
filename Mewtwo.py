import time
import numpy as np
import sys

def gameboy_printing(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Pokemon:
    def __init__(self, names, types, moves, EVs, health, status, battle):
        self.names = names
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

    def introduction(self, oppoPokemon):
        print(f"\n{self.names}", ":L100")
        print("TYPE --", self.types)
        print("=====")
        print("STATUS/", self.status)
        print("=====")
        print("HP/", self.hp)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("SPECIAL/", self.special)
        print("SPEED/", self.speed)
        print("=====")
        print("\n*** VS ***")

        print(f"\n{oppoPokemon.names}", ":L100")
        print("TYPE/", oppoPokemon.types)
        print("=====")
        print("STATUS/", self.status)
        print("=====")
        print("HP/", oppoPokemon.hp)
        print("ATTACK/", oppoPokemon.attack)
        print("DEFENSE/", oppoPokemon.defense)
        print("SPECIAL/", oppoPokemon.special)
        print("SPEED/", oppoPokemon.speed)
        print("=====")

        time.sleep(1)

    def pokeStatuses(self, oppoPokemon):
        print(f"\n{self.names}\t\tHP:\t{self.health}/{self.hp}\t\tSTATUS:\t{self.status}")
        print(f"{oppoPokemon.names}\t\tHP:\t{oppoPokemon.health}/{oppoPokemon.hp}\t\tSTATUS:\t{oppoPokemon.status}")

        time.sleep(1)

    def partyAttack(self, oppoPokemon):
        print(f"\nGo, {self.names}!")
        for i, x in enumerate(self.move_name):
            print(f"{i+1}.", x)
        index = int(input('Pick a move: '))
        gameboy_printing(f"\n{self.names} used {self.move_name[index-1]}!")

        return index

    def partyDamageCalculation(self, oppoPokemon, index):
        if self.move_name[index-1] == 'SEISMIC TOSS':
                oppoPokemon.health -= 100
        else:
            if self.move_name[index-1] == 'THUNDER WAVE' or self.move_name[index-1] == 'SLEEP POWDER':
                if oppoPokemon.status == None:
                    if self.move_name[index-1] == 'THUNDER WAVE':
                        oppoPokemon.status = 'PRZ'
                        gameboy_printing(f"\n{oppoPokemon.names} has been PARALYSED!\n")
                    else:
                        if np.random.choice(4) != 3:
                            oppoPokemon.status = 'SLP'
                            gameboy_printing(f"\n{oppoPokemon.names} has fell ASLEEP!\n")
                        else:
                            gameboy_printing("\nBut it missed!\n")
                else:
                    gameboy_printing("\nBut it failed!\n")
            else:
                if np.random.choice(101) <= self.move_accuracy[index-1]:
                    modifier = np.random.randint(85, 101)/100
                    critical = 1
                    criticalhit = np.random.choice(4)
                    if self.move_name[index-1] == 'RAZOR LEAF' and criticalhit == 0:
                        critical = 2
                        gameboy_printing("\nCritical hit!")
                    if self.move_physpc[index-1] == 'Special':
                        dmg_calc_1 = round(((((42) * self.move_power[index-1] * self.special/oppoPokemon.special)/50)+2)*self.move_stab[index-1]*modifier*critical)
                        oppoPokemon.health -= dmg_calc_1
                    else:
                        dmg_calc_1 = round(((((42) * self.move_power[index-1] * self.attack/oppoPokemon.defense)/50)+2)*self.move_stab[index-1]*modifier)
                        oppoPokemon.health -= dmg_calc_1
                    if oppoPokemon.health < 0:
                        oppoPokemon.health = 0
                else:
                    gameboy_printing("\nBut it missed!\n")

    def MewtwoMakesMove(self, oppoPokemon, string_attack, type_adv):
        print(f"\nGo, {oppoPokemon.names}!")
        index = (np.random.choice(4)+1)
        gameboy_printing(f"\n{oppoPokemon.names} used {oppoPokemon.move_name[index-1]}!")
        time.sleep(1)

        status_flip = np.random.choice(2)

        if (oppoPokemon.status == 'PRZ' and status_flip == 0) or (oppoPokemon.status == 'SLP' and status_flip == 0):
            if (oppoPokemon.status == 'PRZ'):
                gameboy_printing(f"\nBut {oppoPokemon.names} is paralysed!\n")
            else:
                gameboy_printing(f"\nBut {oppoPokemon.names} is still asleep!\n")

        else:
            if oppoPokemon.status == 'SLP':
                gameboy_printing(f"\nNow {oppoPokemon.names} is awake!")
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
                gameboy_printing("\nBut it missed!\n")

    def fight(self, oppoPokemon):
        self.introduction(oppoPokemon)
        self.pokeStatuses(oppoPokemon)

        while (self.health > 0) and (oppoPokemon.health > 0):
            string_attack = ''
            type_adv = 1

##---

            index = self.partyAttack(oppoPokemon)        
            time.sleep(1)
            self.partyDamageCalculation(oppoPokemon, index)
            time.sleep(1)
            self.pokeStatuses(oppoPokemon)

            if oppoPokemon.health <= 0:
                gameboy_printing("\n... " + oppoPokemon.names + ' fainted!')
                break

##---
            
            self.MewtwoMakesMove(oppoPokemon, string_attack, type_adv)
            time.sleep(1)
            self.pokeStatuses(oppoPokemon)

            if self.health <= 0:
                gameboy_printing("\n... " + self.names + ' fainted!\n')
                self.battle = False

##---
                
        if not self.health <= 0:
            exp = np.random.choice(10000)
            gameboy_printing(f"\n{self.names} gained {exp} EXP. points!")

if __name__ == '__main__':
    Pikachu = Pokemon('PIKACHU', 'Electric', {'MOVE NAME': ['THUNDER', 'BODY SLAM', 'SURF', 'THUNDER WAVE'],
                                              'MOVE TYPE': ['Electric', 'Normal', 'Water', 'Electric'],
                                              'MOVE POWER': [120, 85, 95, 0],
                                              'MOVE ACCURACY': [70, 100, 100, 100],
                                              'MOVE PHYSPC': ['Special', 'Physical', 'Special', 'Special'],
                                              'MOVE STAB': [1.5, 1, 1, 1]},
                                             {'HP': 278, 'ATTACK': 208, 'DEFENSE': 158, 'SPECIAL': 198, 'SPEED': 278},
                                             278, None, True)
    Charizard = Pokemon('CHARIZARD', 'Fire/Flying', {'MOVE NAME': ['FIRE BLAST', 'BODY SLAM', 'EARTHQUAKE', 'SEISMIC TOSS'],
                                                     'MOVE TYPE': ['Fire', 'Normal', 'Ground', 'Fighting'],
                                                     'MOVE POWER': [120, 85, 100, 150],
                                                     'MOVE ACCURACY': [85, 100, 100, 100],
                                                     'MOVE PHYSPC': ['Special', 'Physical', 'Physical', 'Physical'],
                                                     'MOVE STAB': [1.5, 1, 1, 1]},
                                                    {'HP': 359, 'ATTACK': 266, 'DEFENSE': 254, 'SPECIAL': 268, 'SPEED': 298},
                                                    359, None, True)
    Blastoise = Pokemon('BLASTOISE', 'Water', {'MOVE NAME': ['HYDRO PUMP', 'BLIZZARD', 'EARTHQUAKE', 'BODY SLAM'],
                                               'MOVE TYPE': ['Fire', 'Normal', 'Ground', 'Normal'],
                                               'MOVE POWER': [120, 120, 100, 85],
                                               'MOVE ACCURACY': [80, 70, 100, 100],
                                               'MOVE PHYSPC': ['Special', 'Special', 'Physical', 'Physical'],
                                               'MOVE STAB': [1.5, 1, 1, 1]},
                                              {'HP': 361, 'ATTACK': 264, 'DEFENSE': 298, 'SPECIAL': 268, 'SPEED': 254},
                                              361, None, True)
    Venusaur = Pokemon('VENUSAUR', 'Grass/Poison', {'MOVE NAME': ['RAZOR LEAF', 'SLEEP POWDER', 'VINE WHIP', 'BODY SLAM'],
                                                    'MOVE TYPE': ['Grass', 'Normal', 'Grass', 'Normal'],
                                                    'MOVE POWER': [55, 0, 40, 85],
                                                    'MOVE ACCURACY': [95, 75, 100, 100],
                                                    'MOVE PHYSPC': ['Special', 'Special', 'Special', 'Physical'],
                                                    'MOVE STAB': [1.5, 1, 1.5, 1]},
                                                   {'HP': 363, 'ATTACK': 262, 'DEFENSE': 264, 'SPECIAL': 298, 'SPEED': 258},
                                                   363, None, True)
    Mewtwo = Pokemon('MEWTWO', 'Psychic', {'MOVE NAME': ['PSYCHIC', 'THUNDER', 'BLIZZARD', 'RECOVER'],
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
