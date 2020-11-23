from typing import List, TypeVar
T = TypeVar('T')

def head(xs: List[T]) -> T:
    if xs == []:
        raise ValueError('Cannot take head of empty list.')
    else:
        return xs[0]