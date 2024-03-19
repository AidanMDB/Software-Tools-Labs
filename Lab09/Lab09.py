# ######################################################
# Author :      Aidan Dannhausen-Brun
# email :       adannhau@purdue.edu
# ID :          ee364a10
# Date :        3/19/24
# ######################################################

import random as rng
import time

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################


def exp(i, n):
    if not isinstance(i, int):
        raise TypeError("input i must be of type int")

    if not isinstance(n, int):
        raise TypeError("input n must be of type int")

    return i ** n


def gen_rand_string():
    str_len = rng.randrange(0, 1000)
    out = ""
    for i in range(0, str_len):
        out += chr(rng.randrange(32, 126))

    return out


def gen_rand_list():
    out = []
    for i in range(0, rng.randrange(0, 1000)):
        out.append(gen_rand_string)

    return out


def gen_non_int():
    return rng.randrange(0, 1, 0.001)


def fuzz_lists():
    for i in range(100):
        exp(gen_rand_list, gen_rand_list)


def fuzz_strings():
    for i in range(100):
        exp(gen_rand_string, gen_rand_string)


def fuzz_non_int():
    for i in range(100):
        exp(gen_non_int, gen_non_int)


def test_growing_size(input):
    start = time.time()
    exp(input, 9999)
    end = time.time()
    print(end-start)
    if (end - start) >= 4:
        print(f"failed at exponent of {input}")


# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
# Write anything here to test your code .

# fuzz_non_int()
# fuzz_strings()
# fuzz_lists()
test_growing_size(10**900)
# 4.352830410003662 time to run
# failed at input of 10000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000000000000000000000000000000000
# 00000000000000000000000000
