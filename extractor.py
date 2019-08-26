import re


def read(filename='huawei_user_loc_lost.txt'):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]


def write(lines):
    with open('output_user_location.txt', "w", encoding='utf-8') as file:
        for line in lines:
            file.write(f'{line}\r\n')
        file.flush()


if __name__ == "__main__":
    alllines = read()
    # line_parts = [line.split() for line in alllines]
    # multiparts_linestrs = ['\t'.join(lp) for lp in line_parts if len(lp) > 1]
    multiparts_lines = [line for line in alllines if re.search(r'\w+\s+\w+', line)]
    write(multiparts_lines)
