class Stats:
    def __init__(self,  max_hp:int, attack:int, defense:int, magic:int, luck:int, speed:int, range:int):
        max_hp  = self.max_hp
        attack  = self.attack
        defense = self.defense
        magic   = self.magic
        luck    = self.luck
        speed   = self.speed
        range   = self.range

    def __repr__(self):
        class_name = type(self).__name__

        #return f"{class_name}(hp={self.hp!r},attack={self.attack!r},defense={self.defense!r},magic={self.magic!r})"
        return f"""{class_name}(max_hp={self.max_hp}, attack={self.attack}, defense={self.defense}, 
                magic={self.magic}, luck={self.luck}, speed={self.speed}, attack_range={self.attack_range})"""

    def __str__(self):
        # This method defines how the object looks when you print() it
        return f"""
        📊 STATS SHEET
        --------------
        ❤️  Max HP  : {self.max_hp}
        ⚔️  Attack  : {self.attack}
        🛡️  Defense : {self.defense}
        ✨  Magic   : {self.magic}
        🍀  Luck    : {self.luck}
        💨  Speed   : {self.speed}
        🎯  Range   : {self.attack_range}
        """