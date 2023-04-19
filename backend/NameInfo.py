from dataclasses import dataclass

@dataclass
class NameInfo:
    name: str = "Jeff"
    yearRangeStart: int = 2011
    yearRangeEnd: int = 2019
    gender: chr = 'X'
    race: str = "All"