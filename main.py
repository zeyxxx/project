class Wero:

    #Конструктор класса
    def __init__(self, name, lvl=1, hp=100):
        # артрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} base action!")
        
#экземпояр/ обьектом на основе класса
kirito = Wero(name="Kirito")
asuna = Wero(name="asuna")
# kirito = Wero(name="Kirito", lvl=100, hp=1000) полное
# asuna = Wero(name="asuna", lvl=101, hp=1001) полное

print(kirito.name)
#print(kirito.name,kirito.lvl, kirito.hp) несколько
print(asuna.name)
#print(asuna.name,asuna.lvl, asuna.hp) несколько








