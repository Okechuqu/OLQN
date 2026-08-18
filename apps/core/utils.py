def normalise_phone(value: str) -> str:
    return "".join(character for character in value if character.isdigit() or character == "+")
