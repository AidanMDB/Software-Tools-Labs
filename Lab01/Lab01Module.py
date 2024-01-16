# ######################################################
# Author : Aidan Dannhausen-Brun
# email : adannhau@purdue.edu
# ID : ee364a10
# Date : 1/16/24
# ######################################################
import os # List of module import statements
import sys # Each one on a line
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def oddResult(number_list, string):
    """Odd Number Result
    
    If the string is ”sum”, return the sum of all the elements that are odd in the list. 
    If the string is ”product”, return the product of all the elements that are odd in the list."""

    # DO SOMETHING HERE
    odd_list = []

    for i in number_list:
        if i % 2 == 1:
            odd_list.append(i)

    result = 0

    if string == "sum":
        result = sum(odd_list)
    else:
        result = odd_list[0]
        for i in range(1, len(odd_list)):
            result *= odd_list[i]

    return result
        
# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == "__main__":
    number_list = list(range(1,6))  # [1, 2, 3, 4, 5]
    result = oddResult(number_list, "sum")
    print(result)
    

