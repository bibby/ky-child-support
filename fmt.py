def to_double(val):
    if not val:
        return 0
    return int(val * 100) / 100
