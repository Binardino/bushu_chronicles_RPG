from core.characters.base_character import BaseCharacter
from core.elements.elements import element_profile

class Hero(BaseCharacter):
    def __init__(self, name, level, stats, element_profile, kwargs**):
        super().__init__(
            name            = name,
            leve            = level,
            stats           = stats,
            element_profile = element_profile,
            **kwargs,
            )
        self.experience = 0
        self.inventory  = []
