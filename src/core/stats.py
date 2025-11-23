class Stats:
    def __init__(self, name, hp:int, attack:int, defense:int, magic:int, luck:int, speed:int):
        name    = self.name
        hp      = self.hp
        attack  = self.attack
        defense = self.defense
        magic   = self.magic
        luck    = self.luck
        speed   = self.speed

    def __str__(self):
        return f""" Hp      : {self.hp}
                    Attack  : {self.attack}
                    Defense : {self.defense}
                    Magic   : {self.magic}
                    Luck   : {self.luck}    
                """

    def is_alive(self) -> bool:
        return self.hp > 0
    
    