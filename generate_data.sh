#!/bin/bash
# Generate data files from submodules and commit them

# Ensure submodules are fetched
git submodule update --init --recursive

# Generate the database
python3 create_data.py

# Generate messages
python3 po/tojson.py

echo "Data files generated. Commit jsdb.js and po/messages.js to your repo."