# -*- coding: utf-8 -*-

import re


def read(filename='huawei_user_loc_check.txt'):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]


def write(lines):
    with open('output_user_location.txt', "w", encoding='utf-8') as file:
        for line in lines:
            file.write(f'{line}\r\n')
        file.flush()


# 43.6667° N, 70.2667° W
# 50°50'20"N•118°58'37"W

# N 51°31' 0'' / W 0°2' 0''
reg_locnums_1 = re.compile(r"N\s*(\d+)\s*°\s*(\d+)\s*'\s*(\d+)\s*''\s*[\s\S]*W\s*(\d+)\s*°\s*(\d+)\s*'\s*(\d+)\s*''\s*")


def tidy_locnums(line):
    line = line.replace(r'ÜT:', '')
    match = reg_locnums_1.search(line)
    if match:
        print(line)
        try:
            line = reg_locnums_1.sub(r'\1.\2\3,\4.\5\6', line)
            print(line)
            print('-' * 70)
        except Exception as e:
            print('*' * 70)
            print(line)

if __name__ == "__main__":
    alllines = read()
    print(len(alllines))
    [tidy_locnums(line) for line in alllines]
