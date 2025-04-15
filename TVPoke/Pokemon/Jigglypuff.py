from TVPoke.BaseClasses.PokeTypes import Fairy
from TVPoke.BaseClasses.Move import Move

class Jigglypuff(Fairy):
    def __init__(self):
        moves = [
            Move("Charm", "Fairy", 0),
            Move("Pound", "Normal", 40),
            Move("Disarming voice", "Fairy", 40),
            Move("Body slam", "Normal", 85)
        ]
        super().__init__("Jigglypuff", 115, moves, "./TVPoke/Pokemon/imgs/Jigglypuff.webp")