import re
from parse import parse

def run_1(filename):
    with open(filename) as input:
        total = 0
        code = input.read()
        search_result = re.findall(r"mul\(\d+,\d+\)", code)
        for mul in search_result:
            total += run_multiply(mul)
        print(total)

def run_2(filename):
    with open(filename) as input:
        total = 0
        code = input.read()
        mul_on = True
        code_counter = 0
        while code_counter <= len(code):
            print(f"counter: {code_counter}")
            if mul_on:
                mul_match = re.match(r"mul\(\d+,\d+\)", code[code_counter:])
                if mul_match:
                    total += run_multiply(mul_match.group())
                    code_counter += len(mul_match.group())
                    continue
                dont_match = re.match(r"don't\(\)", code[code_counter:])
                if dont_match:
                    mul_on = False
                    code_counter += len(dont_match.group())
                    continue
                code_counter += 1
            else:
                do_match = re.match(r"do\(\)", code[code_counter:])
                if do_match:
                    mul_on = True
                    code_counter += len(do_match.group())
                    continue
                code_counter += 1
        print(total)




def run_multiply(multiply):
    r = parse("mul({:d},{:d})",multiply)
    return r[0] * r[1]

if __name__ == "__main__":
    run_2("day_03_input.txt")
