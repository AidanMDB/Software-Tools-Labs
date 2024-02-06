#!/bin/bash

# ######################################################
# Author : < Aidan Dannhausen-Brun >
# email : < adannhau@purdue.edu >
# ID : < ee364a10 >
# Date : < 2/6/2024 >
# ######################################################
# Write your sequence of statements here .

echo "$(wc -c --bytes circuits/circuit*.dat | sort -h | head -n 1 | egrep -o "[0-9]{2}-[0-9]-[0-9]{2}" | xargs -I {} grep {} maps/projects.dat | egrep -o "[A-X0-9]+-[A-X0-9]+-[A-X0-9]+-[A-X0-9]+-[A-X0-9]+")"

exit 0