# This script prepares bulk data from the IRS collecting filings by 527 organizations
# for loading into a database.

data_file = "var/IRS/data/scripts/pofd/download/FullDataFile.txt"
infile = open(data_file,"r", encoding="utf-8")

outfiles = {}

# Create the files
# outfile_headers = open("8872_headers.txt", "w")
# outfile_a = open("8872_schedule_a.txt", "w")
# outfile_b = open("8872_schedule_b.txt", "w")

full_line = ""
append = False

for line in infile: # Read the file line by line
    # Remove carriage returns
    line = line.replace("\r","")
    line = line.replace("\n", "")
    line = line.replace("\\", "")

    if append:
        full_line += line
    else:
        full_line = line

    append = False

    values = full_line.split("|") # Separate the column values by pipe
    linetype = values[0] # Use the value of the first column to determine the line type

    # ignore status messages and multi-line descriptions
    # if len(linetype) > 2:
    #     continue

    # fix problem lines
    count = len(values)
    #expected = 18
    #if linetype == "A" or linetype == "B":
    #    expected = 18
    #else if linetype == "H":
    #    expected = 4
    #else if linetype == "1":
    #    expected = 44
    #else if linetype == "D" or linetype == 'R':
    #    expected = 13
    #else if linetype == "":

    #if count < expected:
    #    append = True
    #    continue

    print(linetype + "," + str(count))

    # if (linetype == "A" or linetype == "B") and count > expected:
    #    print(full_line)

        # difference = expected - count # Calculate the number of missing pipes
        # pipes = ["|"] * difference
        # filler = "".join(pipes)
        # print(line)
        # line = line + filler # Add the missing pipes to the end of the problem line

    if line[-1:] == '|':
        line = line[:-1]

    # if linetype not in outfiles:
        # outfiles[linetype] = open("line_" + linetype + ".txt", "w")

    #outfiles[linetype].write(line)
    #outfiles[linetype].write("\n")


