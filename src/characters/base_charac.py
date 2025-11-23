from ..core import Stats

class BaseCharacter:
    def __init__(self, name, stats, level, elements):
        self.name     = name
        self.stats    = stats
        self.level    = level
        self.elements = elements #elemental affinities

    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name} - Name : {self.name}, Level : {self.level} - Stats : {self.stats}"
        
