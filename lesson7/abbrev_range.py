def abbrev_range(n: int) -> str:
    if n <= 10:
        return ' '.join(str(x) for x in range(1, n+1))
    elif len(str(n)) < 14:
        suffix = f'... {n}'
        prefix_len = 20 - len(suffix)
        return ''.join(
            f'{x} ' for x in range(1, prefix_len//2 + 1)
        ) + suffix
    else:
        # Our final number is too long to be shown as
        # 1 ... n in 20 characters.
        raise ValueError('Overflow')