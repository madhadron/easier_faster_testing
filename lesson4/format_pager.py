def format_pager(
    current_item: int, total_items: int, items_per_page: int,
    left_arrow: str, right_arrow: str
) -> str:
    current_page = math.floor(current_item / items_per_page) + 1
    last_page = math.ceil(total_items / items_per_page)

    numbers = ' '.join(
        f'*{i}*' if i == current_page else f'{i}'
        for i in range(1, last_page+1)
    )

    result = ""
    if current_page != 1:
        result += left_arrow + ' '
    result += numbers
    if current_page != last_page:
        result += ' ' + right_arrow

    return result