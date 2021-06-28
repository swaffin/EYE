
from characters.personnage import Personnage

class Guerrier(Personnage):
    def __init__(self):
        super().__init__(500, 50, 80, 10)

    def __repr__(self):
        return super().__repr__()