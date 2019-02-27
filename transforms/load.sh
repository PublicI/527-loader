#!/bin/bash

psql -f ./transforms/create.sql
psql -c "COPY irs527_filings FROM STDIN WITH CSV DELIMITER '|' QUOTE E'\b'" < "line_2.txt"
psql -c "COPY irs527_contributions FROM STDIN WITH CSV DELIMITER '|' QUOTE E'\b'" < "line_A.txt"
psql -c "COPY irs527_expenditures FROM STDIN WITH CSV DELIMITER '|' QUOTE E'\b'" < "line_B.txt"
