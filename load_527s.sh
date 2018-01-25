#!/bin/bash

wget -N https://forms.irs.gov/app/pod/dataDownload/fullData
unzip fullData
# python get_data.py
python process_data.py
# python fix_schedule_a_errors.py
# python fix_schedule_b_errors.py
psql -U politics -h db.fivetwentyseven.com -f create.sql
psql -U politics -h db.fivetwentyseven.com -c "COPY irs527_filings FROM STDIN WITH CSV DELIMITER '|' QUOTE E'\b'" < "8872_headers.txt" politics
psql -U politics -h db.fivetwentyseven.com -c "COPY irs527_contributions FROM STDIN WITH CSV DELIMITER '|' QUOTE E'\b'" < "8872_schedule_a.txt" politics
psql -U politics -h db.fivetwentyseven.com -c "COPY irs527_expenditures FROM STDIN WITH CSV DELIMITER '|' QUOTE E'\b'" < "8872_schedule_b.txt" politics
rm -rf var
rm 8872_headers.txt
rm 8872_schedule_a.txt
rm 8872_schedule_b.txt
