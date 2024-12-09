from utils import matrix

def run_1(filename):
    with open(filename) as input:
        lines = input.readlines()
        puzzle = matrix.CharacterMatrix(lines)
        total = 0
        for y in range(puzzle.height):
            for x in range(puzzle.width):
                if puzzle.get(x,y) == 'X':
                    total += check_xmas(puzzle, x, y)
        print(total)

def run_2(filename):
    with open(filename) as input:
        lines = input.readlines()
        puzzle = matrix.CharacterMatrix(lines)
        total = 0
        for y in range(puzzle.height):
            for x in range(puzzle.width):
                if puzzle.get(x,y) == 'A':
                    total += check_x_mas(puzzle, x, y)
        print(total)
        
def check_x_mas(puzzle, x: int, y: int) -> int:
    diag1 = False
    diag2 = False
    if (puzzle.get(x+1,y-1) == 'M' and puzzle.get(x-1,y+1) == 'S') or (puzzle.get(x+1,y-1) == 'S' and puzzle.get(x-1,y+1) == 'M'):
        diag1 = True
    if (puzzle.get(x+1,y+1) == 'M' and puzzle.get(x-1,y-1) == 'S') or (puzzle.get(x+1,y+1) == 'S' and puzzle.get(x-1,y-1) == 'M'):
        diag2 = True
    if diag1 and diag2:
        return 1
    else:
        return 0
    


def check_xmas(puzzle, x: int, y: int) -> int:
    xmas_count = 0
    # ->
    if puzzle.get(x+1,y+0) == 'M' and puzzle.get(x+2,y+0) == 'A' and puzzle.get(x+3,y+0) == 'S':
        xmas_count += 1
    # \
    if puzzle.get(x+1,y+1) == 'M' and puzzle.get(x+2,y+2) == 'A' and puzzle.get(x+3,y+3) == 'S':
        xmas_count += 1
    # v
    if puzzle.get(x+0,y+1) == 'M' and puzzle.get(x+0,y+2) == 'A' and puzzle.get(x+0,y+3) == 'S':
        xmas_count += 1
    # /
    if puzzle.get(x-1,y+1) == 'M' and puzzle.get(x-2,y+2) == 'A' and puzzle.get(x-3,y+3) == 'S':
        xmas_count += 1
    # -
    if puzzle.get(x-1,y+0) == 'M' and puzzle.get(x-2,y+0) == 'A' and puzzle.get(x-3,y+0) == 'S':
        xmas_count += 1
    # \
    if puzzle.get(x-1,y-1) == 'M' and puzzle.get(x-2,y-2) == 'A' and puzzle.get(x-3,y-3) == 'S':
        xmas_count += 1
    # ^
    if puzzle.get(x+0,y-1) == 'M' and puzzle.get(x+0,y-2) == 'A' and puzzle.get(x+0,y-3) == 'S':
        xmas_count += 1
    # /
    if puzzle.get(x+1,y-1) == 'M' and puzzle.get(x+2,y-2) == 'A' and puzzle.get(x+3,y-3) == 'S':
        xmas_count += 1
    return xmas_count


if __name__ == "__main__":
    run_2("day_04_input.txt")