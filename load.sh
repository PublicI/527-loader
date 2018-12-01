#!/bin/bash

set -euo pipefail

wget -nv https://forms.irs.gov/app/pod/dataDownload/fullData
unzip fullData
python process_data.py
psql -f create.sql
psql -c "COPY irs527_filings FROM STDIN WITH CSV DELIMITER '|' QUOTE E'\b'" < "line_2.txt"
psql -c "COPY irs527_contributions FROM STDIN WITH CSV DELIMITER '|' QUOTE E'\b'" < "line_A.txt"
psql -c "COPY irs527_expenditures FROM STDIN WITH CSV DELIMITER '|' QUOTE E'\b'" < "line_B.txt"
rm -rf var
rm *.txt
rm fullData
