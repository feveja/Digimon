class Digimon:
    def __init__(self, id, nombre, stage, tipo, atributo, memoria, hp, sp, atk, df, int, spd):
        self.id = id
        self.nombre = nombre
        self.stage = stage
        self.tipo = tipo
        self.atributo = atributo
        self.memoria = memoria
        self.hp = hp
        self.sp = sp
        self.atk = atk
        self.df = df
        self.int = int
        self.spd = spd
    def __repr__(self):
        return f"Digimon({self.id}, {self.nombre}, {self.stage}, {self.tipo}, {self.atributo}, {self.memoria}, {self.hp}, {self.sp}, {self.atk}, {self.df}, {self.int}, {self.spd})"
    
    def obtener_nombre(self):
        return self.nombre