#!/bin/bash

# ######################################################
# Author : < Aidan Dannhausen-Brun >
# email : < adannhau@purdue.edu >
# ID : < ee364a10 >
# Date : < 2/6/2024 >
# ######################################################
# Write your sequence of statements here .

student_id=$(grep "$1" maps/students.dat | awk '{print $4 }')
echo "$(grep -lr "$student_id" circuits | xargs -I {} egrep -o "[A-Z]{3}-[0-9]{3}" {} | sort -u)"


exit 0