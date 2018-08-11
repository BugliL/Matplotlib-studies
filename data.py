import re

REAL_NUMBER_RE = r'([-+]?[0-9]*\.?[0-9]+[eE][-+]?[0-9]+?)'
REAL_NUMBER_RE2 = r'[-+]?[0-9]*\.?[0-9]+'
real_number_re = re.compile(REAL_NUMBER_RE2)

with open('data.txt') as FH:
    lines = FH.readlines()

matrix = []
lines = lines[13:-32]
for line in lines:
    parsed_line = real_number_re.findall(line)
    fn = lambda x: eval(str(x).lstrip('0')) if x != '000' else 0
    num_line = [fn(x) for x in parsed_line]
    # print(num_line)
    matrix.append(num_line)
