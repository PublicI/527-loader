# The purpose of this script is to process 527 organizations' 8872 header (committee information), 8872 schedule A (contributions) and 8872 schedule B (expenditures) records.

data_file = "var/IRS/data/scripts/pofd/download/FullDataFile.txt"
infile = open(data_file,"r", encoding="utf-8")

# Create the files
outfile_headers = open("8872_headers.txt", "w")
outfile_a = open("8872_schedule_a.txt", "w")
outfile_b = open("8872_schedule_b.txt", "w")

linecount = 0 # Set the line count at zero prior to writing data to the outfiles

for line in infile: # Read the file line by line
    linecount += 1 # Increase the line count by one as each line is written

    # Remove carriage returns
    line = line.replace("\r","")
    line = line.replace("\n", "")
    line = line.replace("\\", "")
    values = line.split("|") # Separate the column values by pipe
    linetype = values[0] # Use the value of the first column to determine the line type

    # fix problem lines
    count = len(values)
    expected = 18
    if (linetype == "A" or linetype == "B") and count != expected:
        difference = expected - count # Calculate the number of missing pipes
        pipes = ["|"] * difference
        filler = "".join(pipes)
        line = line + filler # Add the missing pipes to the end of the problem line

    if line[-1:] == '|':
        line = line[:-1]

    # Populate the files
    if linetype == "2":
        outfile_headers.write(line)
        outfile_headers.write("\n")

    elif linetype == "A":
        outfile_a.write(line)
        outfile_a.write("\n")

    elif linetype == "B":
        outfile_b.write(line)
        outfile_b.write("\n")

print("Data processed.")

