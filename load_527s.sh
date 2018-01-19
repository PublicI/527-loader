#!/bin/bash

python get_data.py
python process_data.py
python fix_schedule_a_errors.py
python fix_schedule_b_errors.py
