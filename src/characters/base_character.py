from ..core import Stats

class BaseCharacter:
    def __init__(self, name, stats, level, elements):
        self.name     = name
        self.stats    = stats
        self.level    = level
        self.elements = elements #elemental affinities
        self._current_hp = stats.max_hp 
        self.is_alive = True
        

    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name} - Name : {self.name}, Level : {self.level} - Stats : {self.stats}"
    def take_damage(self, damage_amount:int):

        self.stats.hp = max(0, self.stats.hp - damage_amount)
        print(f"💥 {self.name} took {damage_amount} damage! HP: {self.hp}/{self.max_hp}")
        if not self.is_alive:
            print(f"💀 {self.name} has been defeated!")

        return self.stats.hp
