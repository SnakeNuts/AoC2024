class Matrix:

    def get(self, x, y):
        if x >= 0 and y >= 0 and x < len(self._internalMatrix[0]) and y < len(self._internalMatrix):
            return self._internalMatrix[y][x]
        else:
            return None


class CharacterMatrix(Matrix):

    def __init__(self, lines):
        self._internalMatrix = list()
        for line in lines:
            matrix_row = list()
            for character in line.strip():
                matrix_row.append(character)
            self._internalMatrix.append(matrix_row)
        self.width = len(self._internalMatrix[0])
        self.height = len(self._internalMatrix)



class IntMatrix(Matrix):

    def __init__(lines, delimiter):
        pass

    def parse_int_matrix(lines: list[str], delimiter: chr = ' ') -> list[list]:
        """Parse a set of strings into a 2D int matrix. Dimension is not guaranteed

        Args:
            lines (list[str]): Lines which will be split into ints and put into a 2D array
            delimiter (chr): delimiter separating the ints

        Returns:
            list[list]: 2d array of integers
        """
        raise NotImplementedError("Not Yet Implemented")

