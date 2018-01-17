# The purpose of this script is to download and unzip 527 organizations' data.

import glob
import os
import requests
import shutil
import time
import zipfile

# Download the file
with open ("527.zip", "wb") as fd:
	URL = "https://forms.irs.gov/app/pod/dataDownload/fullData"
	fd.write(requests.get(URL).content)

# Unzip the file
zip_ref = zipfile.ZipFile("527.zip", "r")
zip_ref.extractall("527")
zip_ref.close()

txt_files = glob.glob("./527/**/*.txt", recursive=True) # Find the text file containing the 527 data buried deep within the unzipped folder

# Copy the text file containing the 527 data to the current directory
for file in txt_files:
	if os.path.isfile(file):
		shutil.copy(file,".")

print("Data downloaded and unzipped.")

time.sleep(3)
