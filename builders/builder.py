# builders/builder.py: 
from abc import ABC, abstractmethod
from magic_square import MagicSquare
@abstractmethod
class MagicSquareBuilder(ABC):
    def build(self, n: int) -> MagicSquare:
        pass
