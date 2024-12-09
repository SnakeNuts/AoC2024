from utils import matrix

def run_1(filename):
    with open(filename) as input:
        lines = input.readlines()
        puzzle = matrix.parse_character_matrix(lines)

        for x in range(len(puzzle[0])):
            for y in range(len(puzzle)):
                print(puzzle[x][y], end='')
            print()
        

if __name__ == "__main__":
    run_1("day_04_test_input.txt")