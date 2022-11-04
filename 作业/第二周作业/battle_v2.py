import random


class Warrior:
    HP_Max = 100
    HP = 0
    damage = 30
    name = ''
    status = True
    block_p = 50
    berserker = False

    def __init__(self, name):
        self.name = name
        self.status = True
        self.HP = self.HP_Max

    def attack(self, enemy):
        self.berserk()
        enemy.defend(self.damage)

    def defend(self, damage):
        self.block(damage)
        if self.HP <= 0:
            self.status = False
            print(f"{self.name} is dead.")
        else:
            print(f"{self.name}'s HP is {self.HP}")

    def berserk(self):
        if self.HP < self.HP_Max * 0.3:
            if self.berserker:
                self.berserker = True
                print(f"Crazy! {self.name}'s Damage+ 50%")
                self.damage *= 1.5

    def block(self, damage):
        if random.randint(1, 100) <= self.block_p:
            self.HP -= round(damage / 2)
            print("Block! The enemy's damage -50%")
        else:
            self.HP -= damage


class Assassin:
    HP_Max = 100
    HP = 0
    damage = 30
    name = ''
    status = True
    dodge_p = 30
    critical_p = 30
    critical = False

    def __init__(self, name):
        self.name = name
        self.status = True
        self.HP = self.HP_Max

    def attack(self, enemy):
        self.critical_attack()
        enemy.defend(self.damage)
        if self.critical:
            self.critical = False
            self.damage = self.damage * 2 / 3

    def defend(self, damage):
        self.dodge(damage)
        if self.HP <= 0:
            self.status = False
            print(f"{self.name} is dead.")
        else:
            print(f"{self.name}'s HP is {self.HP}")

    def critical_attack(self):
        if random.randint(1, 100) <= self.critical_p:
            self.critical = True
            self.damage = self.damage * 1.5
            print("CT! Damage +50%")

    def dodge(self, damage):
        if random.randint(1, 100) <= self.dodge_p:
            self.HP -= damage
        else:
            print("Dodge!")


if __name__ == "__main__":
    W = Warrior("Tank")
    A = Assassin("Assassin")
    while W.status and A.status:
        if W.status and A.status:
            W.attack(A)
        else:
            break
        if W.status and A.status:
            A.attack(W)
        else:
            break
