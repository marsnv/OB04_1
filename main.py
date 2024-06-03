from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Нанесен удар мечом..."

class Bow(Weapon):
    def attack(self):
        return "Нанесен удар из лука..."

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "Боец безоружен."

class Monster:
    def __init__(self, name):
        self.name = name

    def take_damage(self):
        return f"Монстр {self.name} побежден!"

# Пример демонстрации
def battle(fighter, monster):
    print(f"Боец {fighter.name} идет в бой...")
    print(fighter.attack())
    print(monster.take_damage())

# Пример использования
fighter = Fighter(input("Введите имя бойца (по умолчанию 'Илья муромец'): ") or "Илья муромец")
monster = Monster(input("Введите имя монстра (по умолчанию 'Годзилла'): ") or "Годзилла")

# Боец выбирает меч
fighter.changeWeapon(Sword())
battle(fighter, monster)

# Боец выбирает лук
fighter.changeWeapon(Bow())
battle(fighter, monster)
