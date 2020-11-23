from typing import List

def format_names(names: List[str]) -> str:
    if names == []:
        return "No one"
    elif len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return f'{names[0]} and {names[1]}'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]}, and {names[2]}'
    elif len(names) < 26:
        return f'{names[0]}, {names[1]}, and {len(names)-2} others'
    else:
        return f'{len(names)} people'