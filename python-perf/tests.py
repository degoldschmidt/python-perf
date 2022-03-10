import math, random
import numpy as np
from timer import timed

@timed
def append_numbers(dims):
    outlist = []
    for i in range(dims):
        outlist.append(i)
    return outlist

@timed
def gen_random_numbers(dims):
    outlist = []
    for i in range(dims):
        outlist.append(random.random())
    return outlist

@timed
def square_numbers(dims):
    outlist = []
    for i in range(dims):
        outlist.append(i*i)
    return outlist