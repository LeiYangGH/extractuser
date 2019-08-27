# -*- coding: utf-8 -*-

import re
import sys


def read(filename='huawei_user_loc_check.txt'):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]


def write(lines, out_file):
    with open(out_file, "w", encoding='utf-8') as file:
        for line in lines:
            file.write(f'{line}\r\n')
        file.flush()


# 43.6667° N, 70.2667° W
# 50°50'20"N•118°58'37"W

# N 51°31' 0'' / W 0°2' 0''
reg_locnums_1 = re.compile(r"N\s*(\d+)\s*°\s*(\d+)\s*'\s*(\d+)\s*''\s*[\s\S]*W\s*(\d+)\s*°\s*(\d+)\s*'\s*(\d+)\s*''\s*")


def replace_chars(line):
    line = line.replace(r'ÜT:', '')
    line = line.replace(r'|', ',')
    line = line.replace(r'!', ',')
    return line


def tidy_locnums(line):
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
    return line


reg_comma = re.compile(r"([^/^,\d]{5,})\s*[,，,/][\s\S]*")


def keep_first_section(line, notes=False):
    match = reg_comma.search(line)
    if match:
        # print(match.group(1))
        if notes:
            sys.stdout.buffer.write(line.encode('utf-8'))
            print()
        try:
            line = reg_comma.sub(r'\1', line)
            if notes:
                sys.stdout.buffer.write(line.encode('utf-8'))
                print()
                print('-' * 70)
        except Exception as e:
            if notes:
                print('*' * 70)
                sys.stdout.buffer.write(line.encode('utf-8'))
    return line


reg_ch_jp = re.compile(r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f\(\)\d\.]{5,}')


def keep_key_jpa(line, notes=False):
    match_ch_jp = reg_ch_jp.search(line)
    if not match_ch_jp:
        return line
    matched_ch_jp_text = match_ch_jp.group(0)
    # if notes:
        # sys.stdout.buffer.write(matched_ch_jp_text)
        # print(matched_ch_jp_text)
    # loopcnt = 0

    for key in ['东京', '東京', '大阪', '横滨', '名古屋', '神户', '福冈', '京都', '札幌', '仙台', '广岛']:
        if key in matched_ch_jp_text:
            try:
                print(line)
                # loopcnt += 1
                # print(loopcnt)
                if notes:
                    # sys.stdout.buffer.write(line.encode('utf-8'))
                    print(line)
                    print()
                line = line.replace(matched_ch_jp_text, key)
                if notes:
                    # sys.stdout.buffer.write(line.encode('utf-8'))
                    print(line)
                    print()
                    print('-' * 70)
            except:
                pass
            break

    return line




if __name__ == "__main__":
    alllines = read()
    print(len(alllines))
    alllines = [replace_chars(line) for line in alllines]

    loc_lines = [line for line in alllines if reg_locnums_1.search(line)]
    non_loc_lines = [line for line in alllines if not reg_locnums_1.search(line)]

    loc_lines = [tidy_locnums(line) for line in loc_lines]

    non_loc_lines = [keep_first_section(line, notes=True) for line in non_loc_lines]
    non_loc_lines = [keep_key_jpa(line, notes=True) for line in non_loc_lines]


    print(len(loc_lines))
    print(len(non_loc_lines))
    write(loc_lines,"output_loc_lines.txt")
    write(non_loc_lines,"output_non_loc_lines.txt")
    print('all done.')
