
def run_1(input_file_name):
  run(input_file_name)

def run_2(input_file_name):
  run(input_file_name, dampner = True)

def run(input_file_name, dampner = False):
  safe_count = 0
  with open(input_file_name) as input:
    reports = input.readlines()
    for report in reports:
      safe_count += is_report_safe(report, dampner)
  print(safe_count)

def is_report_safe(report, dampner) -> int:
  differences = list()
  levels = report.split()
  errors = 0
  for index in range(1, len(levels)):
    difference = int(levels[index]) - int(levels[index - 1])
    if abs(difference) < 1 or abs(difference) > 3:
      errors += 1
    differences.append(difference)
  # check if all differences are either up or down
  if not all_same_sign(differences):
    errors += 1
  if errors == 0:
    return 1
  else:
    if dampner and errors == 1:
      return 1
    else:
      return 0

def all_same_sign(numbers):
  sign = numbers[0] >= 0
  return all((num >= 0) == sign for num in numbers)


if __name__ == "__main__":
  run_2("day_02_input.txt")