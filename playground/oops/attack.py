#!/usr/bin/python3

import random
import math

'''
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has died and Sam is Victorious
Game Over
'''

# Warrior & Battle Class

class Warrior:
    def __init__(self, name="Warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() + .5)

        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)

        return blockAmt


# Warriors will have names, health and attack and block maximus

# They will have the capabilities or methods to block random amounts

# Attack random() 0.0 to 1.0 * maxAttack + .5

# BLock will use random()

# Battle class capability of looping until 1 warrior dies
# Warriors will each get a turn to attack each other

# Function gets 2 warriors
# 1 warrior attacks the other
# Attacks and blocks be integers


class Battle:

    def startFight(self, warrior1, warrior2):

        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break


    @staticmethod
    def getAttackResult(warriorA, warriorB):

        warriorAAttkAmt = warriorA.attack()

        warriorBBlockAmt = warriorB.block()

        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)

        warriorB.health = warriorB.health - damage2WarriorB

        print("{} attacks {} and deals {} damage".format(warriorA.name,
                                                         warriorB.name, damage2WrriorB))

        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name, warriorA.name))
            return "Game over"
        else:
            return "Fight Again"



def main():

    maximus = Warrior("Maximus", 50, 20, 10)

    galaxon = Warrior("Galaxon", 50, 20, 10)

    battle = Battle()

    battle.startFight(maximus, galaxon)

main()
