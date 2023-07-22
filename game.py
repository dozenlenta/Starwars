class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} attacked {other.name} for {self.attack_power} damage.")

class Jedi(Character):
    def __init__(self, name, health, attack_power, force_points):
        super().__init__(name, health, attack_power)
        self.force_points = force_points

    def use_force(self, other):
        other.health -= self.force_points
        print(f"{self.name} used the Force on {other.name} for {self.force_points} damage.")

class Sith(Character):
    def __init__(self, name, health, attack_power, lightning_power):
        super().__init__(name, health, attack_power)
        self.lightning_power = lightning_power

    def use_lightning(self, other):
        other.health -= self.lightning_power
        print(f"{self.name} used Force lightning on {other.name} for {self.lightning_power} damage.")

def battle(jedi, sith):
    while jedi.health > 0 and sith.health > 0:
        jedi.attack(sith)
        sith.use_lightning(jedi)
        if jedi.health > 0:
            jedi.use_force(sith)
        if sith.health > 0:
            sith.attack(jedi)
    if jedi.health > 0:
        print(f"{jedi.name} has won the battle!")
    else:
        print(f"{sith.name} has won the battle!")

# Example Usage Game
jedi = Jedi("Obi-Wan Kenobi", 100, 20, 40)
sith = Sith("Darth Vader", 150, 30, 60)

battle(jedi, sith)
