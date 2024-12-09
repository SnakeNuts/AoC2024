from utils import matrix

puzzle = list()

def run_1(filename):
    with open(filename) as input:
        lines = input.readlines()
        puzzle = matrix.CharacterMatrix(lines)

        for y in range(puzzle.height):
            for x in range(puzzle.width):
                check_xmas(x, y)
        

def check_xmas(x: int, y: int) -> int:
    pass

if __name__ == "__main__":
    run_1("day_04_test_input.txt")