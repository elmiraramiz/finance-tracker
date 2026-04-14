from dataclasses import dataclass
from datetime import datetime

@dataclass
class Transaction:
    id: int
    amount: float
    category: str
    type: str       # income or expense
    date: str       # YYYY-MM-DD
    description: str = ""