from dataclasses import dataclass

@dataclass
class ServiceDescription:
    name: str
    dept: set
    value: int