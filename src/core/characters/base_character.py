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
        
    # ----------- Life Method  ------------------        
    def is_alive(self) -> bool:
        """Return True if HP > 0"""

        return self.current_hp > 0
    
    # ----------- Combat Methods ----------------
    def take_damage(self, damage_amount:int):

        self.current_hp = max(0, self.current_hp - damage_amount)
        
        print(f"💥 {self.name} took {damage_amount} damage! 
              HP: {self.current_hp}/{self.stats.max_hp}")
        
        if not self.is_alive:
            print(f"💀 {self.name} has been defeated!")

        return self.current_hp

    def heal(self, heal_amount : int):
        self.current_hp = min(self.max_hp, self.current_hp + heal_amount)

        print(f"✨ {self.name} healed {heal_amount} HP "
              f"(HP {self.current_hp}/{self.stats.max_hp})")    
    