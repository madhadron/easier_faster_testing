from typing import Dict, Hashable
from math import inf

def maxval(m: Dict[Hashable, int]) -> int:
    if m == {}:
        return -inf
    else:
        return max(m.values())