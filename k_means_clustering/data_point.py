"""


Keyword arguments:
argument -- description
Return: return_description
"""


from __future__ import annotations
from typing import Iterator, Tuple, List, Iterable
from math import sqrt


class DataPoint:
    def __init__(self, initial: Iterable[float]) -> None:
        self._originals: Tuple[float, ...] = Tuple(initial)
        self.dimensions: Tuple[float, ...] = Tuple(initial)

    @property
    def num_dimensions(self) -> int:
        return len(self.dimensions)

    def distance(self, other: DataPoint) -> float:
        """Calcula a distância entre dois DataPoints
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        
        combined: Iterator[Tuple[float, float]] = zip(self.dimensions, other.dimensions)
        differences: List[float] = [(x - y) ** 2 for x, y in combined]
        return sqrt(sum(differences))

    def __eq__(self, other: object) -> bool:
        """Compara se dois pontos de dados comutáveis são iguais
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if not isinstance(other, DataPoint):
            return NotImplemented
        return self.dimensions == other.dimensions

    def __repr__(self) -> str:
        """Torna os dados legíveis para depuração
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        
        return self._originals.__repr__()