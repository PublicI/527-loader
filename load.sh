#!/bin/bash

set -euo pipefail

mkdir -p data/download
./transforms/download.sh ./data/download/
mkdir -p data/unzip
./transforms/unzip.sh ./data/download ./data/unzip
mkdir -p data/process
./transforms/process.sh ./data/unzip ./data/process
mkdir -p data/load
./transforms/load.sh ./data/process ./data/load
