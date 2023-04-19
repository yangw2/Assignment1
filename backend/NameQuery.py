from dataclasses import dataclass

@dataclass
class NameQuery:
    name: str = "jeff"
    yearRangeStart: int = 2011
    yearRangeEnd: int = 2019
    gender: chr = 'X'
    amountNames: int = 1
    race: str = "All"
    sortingStyle: int = 1