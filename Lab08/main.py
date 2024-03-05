from math import sqrt

def is_prime(number):
    #NOTE: 
    # This is a very inefficient way to check for a prime numbers. Since this
    # is just checking if a number is prime, you might want to just use a 
    # smaller prime number for testing

    if number < 2:
        return False

    for i in range(2, int(sqrt(number)) + 1):
        if(number % i == 0):
            return False
    
    return True

def combine_variables(a, b):
    # This is where we combine the variables a and b
    # Don't worry much about what this does, just try to see if 
    # there are any extra cases to test

    return_value = a ^ b

    for i in range(0, a+b):
        return_value ^= (a ^  b)

    j = 1

    while return_value < 0:
        return_value += j
        j += 1

    return return_value

def main(a, b):
    # For each operand we will do the following:
    #   - If an operand is an integer we will see if it is EVEN, PRIME, or 
    #     ODD (a non-prime odd number)
    #   - If an operand is a character, we will convert it to its ASCII integer value
    #
    # This process is repeated for both operands so make sure to check each 
    # possible combination of operands (should need 8 tests or more)
    #
    # Finally, the variables are combined in the function combine_variables().
    #
    # Make sure to check each of the helper functions to see if there are any 
    # notes on operation or any branches to keep track of in testing

    if type(a) == int:
        if a % 2 == 0:
            print("First operand is even")
        elif is_prime(a):
            print("First operand is prime")
        else:
            print("First operand is an odd composite number")
    elif type(a) == str:
        print("First operand is a character")
        #ord() => converts ascii to hex
        a = ord(a)
    else:
        raise ValueError("\n\nFirst operand can only be an integer, character, or string!\n\n")

    #Checking second operand:
    if type(b) == int:
        if b % 2 == 0:
            print("Second operand is even")
        elif is_prime(b):
            print("Second operand is prime")
        else:
            print("Second operand is an odd composite number")
    elif type(b) == str:
        print("Second operand is a character")
        #ord() => converts ascii to hex
        b = ord(b)
    else:
        raise ValueError("\n\Second operand can only be an integer, character, or string!\n\n")

    print(combine_variables(a, b))

    return  
