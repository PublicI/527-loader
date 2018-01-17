# The purpose of this script is to process 527 organizations' 8872 header (committee information), 8872 schedule A (contributions) and 8872 schedule B (expenditures) records.

import time

line_2_header = "Record Type|Form Type|Form ID Number|PERIOD Begin Date|PERIOD End Date|Initial Report Indicator|Amended Report Indicator|Final Report Indicator|Change of Address Indicator|ORGANIZATION NAME|EIN|MAILING ADDRESS 1|MAILING ADDRESS 2|MAILING ADDRESS CITY|MAILING ADDRESS STATE|MAILING ADDRESS ZIP CODE|MAILING ADDRESS ZIP EXT|E_MAIL ADDRESS|ORG FORMATION DATE|CUSTODIAN NAME|CUSTODIAN ADDRESS 1|CUSTODIAN ADDRESS 2|CUSTODIAN ADDRESS CITY|CUSTODIAN ADDRESS STATE|CUSTODIAN ADDRESS ZIP CODE|CUSTODIAN ADDRESS ZIP EXT|CONTACT PERSON NAME|CONTACT ADDRESS 1|CONTACT ADDRESS 2|CONTACT ADDRESS CITY|CONTACT ADDRESS STATE|CONTACT ADDRESS ZIP CODE|CONTACT ADDRESS ZIP EXT|BUSINESS ADDRESS 1|BUSINESS ADDRESS 2|BUSINESS ADDRESS CITY|BUSINESS ADDRESS STATE|BUSINESS ADDRESS ZIP CODE|BUSINESS ADDRESS ZIP EXT|QTR INDICATOR|MONTHLY RPT MONTH|PRE ELECT TYPE|PRE or POST ELECT DATE|PRE or POST ELECT STATE|SCHED_A_IND|TOTAL_SCHED_A|SCHED_B_IND|TOTAL_SCHED_B|INSERT_DATETIME\n"

line_a_header = "Record Type|Form ID Number|SCHED A ID|ORG NAME|EIN|CONTRIBUTOR NAME|CONTRIBUTOR ADDRESS 1|CONTRIBUTOR ADDRESS 2|CONTRIBUTOR ADDRESS CITY|CONTRIBUTOR ADDRESS STATE|CONTRIBUTOR ADDRESS ZIP CODE|CONTRIBUTOR ADDRESS ZIP EXT|CONTRIBUTOR EMPLOYER|CONTRIBUTION AMOUNT|CONTRIBUTOR OCCUPATION|AGG CONTRIBUTION YTD|CONTRIBUTION DATE\n"

line_b_header = "Record Type|Form ID Number|SCHED B ID|ORG NAME|EIN|RECIPIENT NAME|RECIPIENT ADDRESS 1|RECIPIENT ADDRESS 2|RECIPIENT ADDRESS CITY|RECIPIENT ADDRESS ST|RECIPIENT ADDRESS ZIP CODE|RECIPIENT ADDRESS ZIP EXT|RECIPIENT EMPLOYER|EXPENDITURE AMOUNT|RECIPIENT OCCUPATION|EXPENDITURE DATE|EXPENDITURE PURPOSE\n"

data_file = "FullDataFile.txt"
infile = open(data_file,"r", encoding="utf-8")

# Create the files
outfile_headers = open("8872_headers.txt", "w")
outfile_headers.write(line_2_header)

outfile_a = open("8872_schedule_a.txt", "w")
outfile_a.write(line_a_header)

outfile_b = open("8872_schedule_b.txt", "w")
outfile_b.write(line_b_header)

linecount = 0 # Set the line count at zero prior to writing data to the outfiles

for line in infile: # Read the file line by line
	linecount += 1 # Increase the line count by one as each line is written

	# Remove carriage returns
	line = line.replace("\r","")
	line = line.replace("\n", "")
	print("Processed " + str(linecount) + " lines.") # Print the number of lines processed 
	values = line.split("|") # Separate the column values by pipe
	linetype = values[0] # Use the value of the first column to determine the line type

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

time.sleep(3)
