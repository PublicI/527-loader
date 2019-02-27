#!/bin/bash

set -euo pipefail

wget -O $1"/fullData" -nv https://forms.irs.gov/app/pod/dataDownload/fullData
