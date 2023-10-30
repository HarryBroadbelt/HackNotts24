
class Dungeon:
    def __init__(self, difficulty):
        self.__difficulty = difficulty


    @property
    def difficulty(self):
        return self.__difficulty
    
    @difficulty.setter
    def difficulty(self, new_difficulty):
        self.__difficulty = new_difficulty
    
