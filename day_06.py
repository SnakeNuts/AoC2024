import numpy as np

class guard_map():
    def __init__(self, map_text: list[str]):
        self.obstacles = set()
        y_counter = 0
        for line in map(str.strip, map_text):
            self.map_size = len(line)
            x_counter = 0
            for position in line:
                if position == "#":
                    self.obstacles.add((x_counter, y_counter))
                if position == "^":
                    self.guard_pos_x = x_counter
                    self.guard_pos_y = y_counter
                x_counter += 1
            y_counter += 1
        self.direction_x = 0
        self.direction_y = -1


    
    def move(self) -> bool:
        new_x = self.guard_pos_x + self.direction_x
        new_y = self.guard_pos_y + self.direction_y
        if new_x < 0 or new_y < 0 or new_x > self.map_size or new_y > self.map_size:
            return False
        
        if (new_x, new_y) in self.obstacles:
            # bonk, turn 90 degrees 


if __name__ == "__main__":
    with open("day_06_test_input.txt") as input:
        map_text = input.readlines()
        current_map = guard_map(map_text)
        current_map.move()

