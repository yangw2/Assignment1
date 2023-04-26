from dataclasses import dataclass, field

@dataclass
class NameInfo:
    name: str = "Jeff"
    sex: chr = "m"
    dataByYear: dict = field(default_factory= lambda: {
        '2011' : {
            'Asian' : 10
        }
    })

@dataclass
class NameQuery:
    name: str = "jeff"
    yearRangeStart: int = 2011
    yearRangeEnd: int = 2019
    gender: chr = 'X'
    amountNames: int = 1
    race: str = "All"
    sortingStyle: int = 1