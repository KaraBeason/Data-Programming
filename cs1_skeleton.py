__author__ = ''
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import pandas as pd
from collections import Counter


def main():
    # TODO: put your code to produce the figures here.
    content = pd.read_csv('content.csv')
    #  store the rows we are actually using
    created_time = content.get(['created_time'])
    num_likes = content.get(['num_likes'])
    num_comments = content.get(['num_comments'])
    types = content.get(['type'])
    s = pd.Series(types)
    vc = s.value_counts()
    pass

if __name__ == '__main__':
    main()
