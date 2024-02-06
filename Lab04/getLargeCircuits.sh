#!/bin/bash

# ######################################################
# Author : < Aidan Dannhausen-Brun >
# email : < adannhau@purdue.edu >
# ID : < ee364a10 >
# Date : < 2/6/2024 >
# ######################################################
# Write your sequence of statements here .

echo "$(wc -c --bytes circuits/circuit*.dat | egrep "[2-9][0-9]{2}" | sort -h | egrep -o "[0-9]{2}-[0-9]-[0-9]{2}" | sort -ru)"


exit 0