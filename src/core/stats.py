class Stats:
    def __init__(self,  hp:int, attack:int, defense:int, magic:int, luck:int, speed:int, range:int):
        hp      = self.hp
        attack  = self.attack
        defense = self.defense
        magic   = self.magic
        luck    = self.luck
        speed   = self.speed
        range   = self.range

    def __repr__(self):
        class_name = type(self).__name__

        return f"{class_name}(hp={self.hp!r},attack={self.attack!r},defense={self.defense!r},magic={self.magic!r})"

    def __str__(self):
        return f""" Hp      : {self.hp}
                    Attack  : {self.attack}
                    Defense : {self.defense}
                    Magic   : {self.magic}
                    Luck    : {self.luck}
                    Speed   : {self.speed}
                    Range   : {self.range}        
                """

    def is_alive(self) -> bool:
        return self.hp > 0
    
    