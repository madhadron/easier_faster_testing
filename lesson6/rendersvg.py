from typing import NamedTuple, List, Tuple

class ColoredLineSegments(NamedTuple):
    color: int # 0 to 15
    vertices: List[Tuple[float, float]]

def renderSvg(shape: ColoredLineSegments) -> str:
    CGA_COLORS = [
        'black', 'blue', 'green', 'cyan', 'red',
        'magenta', 'brown', 'lightgray', 'darkgray',
        'lightblue', 'lightgreen', 'lightcyan',
        'lightred', 'lightmagenta', 'yellow', 'white',
    ]
    if shape.color < 0 or shape.color > 15:
        raise ValueError(f'Color must be in [0, 15], found {shape.color}')

    vertices_str = ' '.join(
        f'{x},{y}' for (x, y) in shape.vertices
    )
    polyline = f'<polyline points="{vertices_str}" stroke="currentColor" />'
    return f'<g color="{CGA_COLORS[shape.color]}">{polyline}</g>'