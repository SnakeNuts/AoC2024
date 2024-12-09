def parse_character_matrix(lines: list[str]) -> list[list]:
    """Parse a set of strings into a 2D character matrix. Dimension is not guaranteed.

    Args:
        lines (list[str]): Lines which will be split into characters and put into 2D array

    Returns:
        list[list]: 2D array of characters
    """
    matrix = list()
    for line in lines:
        matrix_row = list()
        for character in line.strip():
            matrix_row.append(character)
        matrix.append(matrix_row)
    return matrix


def parse_int_matrix(lines: list[str], delimiter: chr = ' ') -> list[list]:
    """Parse a set of strings into a 2D int matrix. Dimension is not guaranteed

    Args:
        lines (list[str]): Lines which will be split into ints and put into a 2D array
        delimiter (chr): delimiter separating the ints

    Returns:
        list[list]: 2d array of integers
    """
    raise NotImplementedError("Not Yet Implemented")

