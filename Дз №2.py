import random

# Родительский класс
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет! Я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} атакует!")

    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает и восстанавливает здоровье. Здоровье: {self.health}")


# Класс Warrior
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print("Воин атакует мечом!")


# Класс Mage
class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print("Маг кастует заклинание!")


# Класс Assassin
class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print("Ассасин атакует из-под тишка!")


# Создание объектов
warrior = Warrior("Артур", 5, 100, 20, 50)
mage = Mage("Мерлин", 5, 80, 25, 100)
assassin = Assassin("Шэдоу", 5, 90, 22, 70)

heroes = {
    "warrior": warrior,
    "mage": mage,
    "assassin": assassin
}

# Игра
print("Выберите героя: Warrior / Mage / Assassin")
choice = input().lower()

if choice not in heroes:
    print("Неверный выбор!")
else:
    player = heroes[choice]

    enemies = list(heroes.values())
    enemies.remove(player)
    enemy = random.choice(enemies)

    print(f"\nВы выбрали: {player.__class__.__name__}")
    print(f"Противник: {enemy.__class__.__name__}\n")

    player.attack()
    enemy.attack()

    # Логика победителя
    if (
        (isinstance(player, Warrior) and isinstance(enemy, Assassin)) or
        (isinstance(player, Assassin) and isinstance(enemy, Mage)) or
        (isinstance(player, Mage) and isinstance(enemy, Warrior))
    ):
        print(f"{player.__class__.__name__} победил!")
    else:
        print(f"{enemy.__class__.__name__} победил!")
