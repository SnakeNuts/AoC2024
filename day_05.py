from collections import defaultdict
from parse import parse

def run1(filename: str):
    rules_lines = list()
    update_lines = list()
    with open(filename) as input:
        do_rules = True
        for line in input:
            if line.strip() == "":
                do_rules = False
                continue
            if do_rules:
                rules_lines.append(line)
            else:
                update_lines.append(line)
    
    rules = defaultdict(list)
    for rule_line in rules_lines:
        rule_parse = parse("{:d}|{:d}", rule_line.strip())
        rules[rule_parse[0]].append(rule_parse[1])
    
    total_middle = 0
    # for any given page X, if that page appears in the rules dictionary, any pages that are in the list attached should not already be seen previously.
    for update_line in update_lines:
        seen_pages = list()
        correct_update = True
        update_pages = list(map(int, update_line.strip().split(',')))
        for page in update_pages:
            seen_pages.append(page)
            if page in rules.keys():
                for rule_page in rules[page]:
                    if rule_page in seen_pages:
                        # wrong!
                        correct_update = False
        if correct_update:
            middle = len(update_pages) // 2
            print(f"{update_pages} is correct {middle}")
            total_middle += update_pages[middle]
    print(total_middle)


if __name__ == "__main__":
    run1("day_05_input.txt")