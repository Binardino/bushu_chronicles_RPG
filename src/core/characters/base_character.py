class BaseCharacter:
    def __init__(self, name: str, level: int, stats, element_profile, category_profile = None, radical_profile = None):
        self.name               = name
        self.stats              = stats
        self.level              = level

        self.element_profile    = element_profile  #elemental affinities
        self.category_profile   = category_profile
        self.radical_profile    = radical_profile
        
        self.current_hp        = stats.max_hp 
        

    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name} - Name : {self.name}, Level : {self.level} - Stats : {self.stats}"
    def take_damage(self, damage_amount:int):

        self.stats.hp = max(0, self.stats.hp - damage_amount)
        print(f"💥 {self.name} took {damage_amount} damage! HP: {self.hp}/{self.max_hp}")
        if not self.is_alive:
            print(f"💀 {self.name} has been defeated!")

        return self.stats.hp
