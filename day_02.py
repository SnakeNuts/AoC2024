from itertools import combinations

def run_1(input_file_name):
  safe_count = 0
  with open(input_file_name) as input:
    reports = input.readlines()
    for report in reports:
      levels = report.split()
      error_count = errors_in_report(levels)
      safe_count += (error_count < 1)
  print(safe_count)

def run_2(input_file_name):
  safe_count = 0
  with open(input_file_name) as input:
    reports = input.readlines()
    for report in reports:
      levels = report.split()
      error_count = errors_in_report(levels)
      if error_count == 0:
        safe_count += 1
      else:
        for new_report in combinations(levels,len(levels)-1):
          if errors_in_report(new_report) == 0:
            safe_count += 1
            break
        
  print(safe_count)





def errors_in_report(levels) -> int:
  differences = list()
  errors = 0
  for index in range(1, len(levels)):
    difference = int(levels[index]) - int(levels[index - 1])
    if abs(difference) < 1 or abs(difference) > 3:
      errors += 1
    differences.append(difference)
  # check if all differences are either up or down
  if not all_same_sign(differences):
    errors += 1
  return errors

def all_same_sign(numbers):
  sign = numbers[0] >= 0
  return all((num >= 0) == sign for num in numbers)


if __name__ == "__main__":
  run_1("day_02_input.txt")
  run_2("day_02_input.txt")