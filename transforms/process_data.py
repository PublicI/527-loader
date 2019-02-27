# This script splits an IRS data file containing records on the activities
# of 527 organizations into files suitable for loading into database tables.

from io import open
import sys


fields_per_type = {
    'H': 5,
    'F': 5,
    '1': 44,
    '2': 50,
    'A': 18,
    'B': 18,
    'D': 14,
    'E': 6,
    'R': 14
}
print(sys.argv[1])
path = sys.argv[1]
file = open(path, 'r', encoding='utf-8')

out_files = {}
out_line = ''
line_count = 0


def writeLine(line):
    if line[-1:] == '|':
        line = line[:-1]

    if line_type not in out_files:
        out_files[line_type] = open('line_' + line_type + '.txt', 'w')

    out_files[line_type].write(line + '\n')


for line in file:
    # remove new line characters
    line = line.replace('\r', '')
    line = line.replace('\n', '')

    values = (out_line + line).split('|')  # separate the column values by pipe
    line_type = values[0]  # use the first column value as the line type

    if line_type not in fields_per_type:
        print('unrecognized line type: ' + line_type)
        continue

    fields = len(values)
    expected = fields_per_type[line_type]

    if fields < expected:
        out_line += line
        continue
    elif fields == expected:
        writeLine(out_line + line)
        line_count += 1
    else:  # truncated line, appending later lines didn't help, so add pipes
        difference = expected - fields  # calculate the number of missing pipes
        pipes = ['|'] * difference
        filler = ''.join(pipes)
        out_line = out_line + filler  # add missing pipes
        writeLine(out_line)
        writeLine(line)
        line_count += 2

    if line_type == 'F' and int(values[-2]) != line_count-2:
        print('record count mismatch: wrote ' +
              str(line_count-2) + ' but expected ' + values[-2])

    out_line = ''
