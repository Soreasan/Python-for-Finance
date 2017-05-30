#!/usr/bin/env python
# Accessing Elements
import numpy as np

def test_run():
    a = np.array([(20, 25, 10, 23, 26, 32, 10, 5, 0), (0, 2, 50, 20, 0, 1, 28, 5, 0)])
    print a

    # Calculating the mean
    mean = a.mean()
    print mean

    # masking
    print a[a < mean]

    # We can also change the values in the array with the mask
    a[a < mean] = mean
    print a

if __name__ == "__main__":
    test_run()
