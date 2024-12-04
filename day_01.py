from collections import defaultdict


def run_1(input_file_name):
  left_numbers = list()
  right_numbers = list()
  with open(input_file_name) as input:
    lines = input.readlines()
    for line in lines:
      numbers = line.split()
      left_numbers.append(int(numbers[0]))
      right_numbers.append(int(numbers[1]))
  left_numbers.sort()
  right_numbers.sort()

  total_difference = 0
  
  for counter in range(len(left_numbers)):
    difference = abs(left_numbers[counter] - right_numbers[counter])
    print(f"difference between {left_numbers[counter]} and {right_numbers[counter]} is {difference}")
    total_difference += difference

  print(total_difference)

def run_2(input_file_name):
  left_numbers = list()
  right_numbers = defaultdict(int)
  with open(input_file_name) as input:
    lines = input.readlines()
    for line in lines:
      numbers = line.split()
      left_numbers.append(int(numbers[0]))
      right_numbers[int(numbers[1])] += 1

  similarity_score = 0
  for number in left_numbers:
    similarity_score += number * right_numbers[number]

  print(similarity_score)

if __name__ == "__main__":
  run_1("day_01_input.txt")