#!/bin/bash

rm fullData
wget https://forms.irs.gov/app/pod/dataDownload/fullData
unzip fullData
python process_data.py
psql -U politics -h db.fivetwentyseven.com -f create.sql
psql -U politics -h db.fivetwentyseven.com -c "COPY irs527_filings FROM STDIN WITH CSV DELIMITER '|' QUOTE E'\b'" < "line_2.txt" politics
psql -U politics -h db.fivetwentyseven.com -c "COPY irs527_contributions FROM STDIN WITH CSV DELIMITER '|' QUOTE E'\b'" < "line_A.txt" politics
psql -U politics -h db.fivetwentyseven.com -c "COPY irs527_expenditures FROM STDIN WITH CSV DELIMITER '|' QUOTE E'\b'" < "line_B.txt" politics
rm -rf var
rm *.txt
