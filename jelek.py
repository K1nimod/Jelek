class Jel:
    def __init__(self, ora, perc, mp, x, y):
        self.ora = ora
        self.perc = perc
        self.mp = mp
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.ora} {self.perc}{self.mp}{self.x}{self.y}"
        
f = open("jel.txt", "rt", encoding="utf-8")

