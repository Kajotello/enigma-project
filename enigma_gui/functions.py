def to_number(char: str) -> int:
    return ord(char) - 65


def to_letter(int: int) -> str:
    return chr(int+65)
