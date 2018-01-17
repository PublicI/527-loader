# The purpose of this script is to fix errors with the 8872 Schedule B data.

infile = open("8872_schedule_b.txt", "r")
outfile = open("8872_schedule_b_fixed.txt", "w")

header = infile.readline() # Write the header row

linenum = 0 # Set the line number at zero prior to reading data from the infile

problems = 0 # Set the problem lines count at zero prior to reading data from the infile

counts = {}

while True:
	linenum += 1 # Increase the line number by one as each line is read
	line = infile.readline() # Read the file line by line
	line = line.replace("\r", "") # Remove carriage returns
	line = line.replace("\\", "") # What is this doing?

	if not line: # Stop when all lines have been read
		break

	count = line.count("|") # Count the number of pipes on each line
	if count != 17:
		print(linenum, count)
		problems += 1 # Increase the problem lines count by one as each line with fewer than 17 pipes is read
		difference = 17 - count # Calculate the number of missing pipes
		pipes = ["|"] * difference
		filler = "".join(pipes)
		line = line + filler # Add the missing pipes to the end of the problem line

	outfile.write(line) # Populate the file

print(str(problems) + " Schedule B problem records fixed.")
