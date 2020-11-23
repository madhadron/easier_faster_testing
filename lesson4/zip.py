from typing import List, Tuple, TypeVar
T = TypeVar('T')
U = TypeVar('U')

def zip(xs: List[T], ys: List[U]) -> List[Tuple[T,U]]:
    n = min(len(xs), len(ys))
    result = []
    i = 0
    while i < n:
        result.append((xs[i], ys[i]))
        i += 1
    return result