"""
Tests.
"""

import numpy as np
import hdmedians as hd
import sys

from numpy.testing import assert_equal, assert_array_almost_equal
from nose.tools import assert_true

DATA1 = np.array([[693, 990, 1281, 2101, 3524, 2577],
                  [606, 898, 1128, 1962, 2992, 2106],
                  [509, 831, 932, 2287, 3113, 2188],
                  [466, 796, 870, 2380, 2903, 1953],
                  [527, 814, 888, 2456, 2835, 1841],
                  [721, 966, 1227, 2249, 3577, 2693],
                  [670, 926, 1213, 2218, 3574, 2719],
                  [809, 1058, 1375, 2272, 3860, 2936],
                  [864, 1115, 1454, 2299, 3630, 2843],
                  [793, 1029, 1353, 2212, 3774, 3010],
                  [849, 1143, 1592, 2483, 4121, 3138],
                  [847, 1149, 1606, 2472, 4179, 3326],
                  [841, 1146, 1609, 2487, 4200, 3375],
                  [893, 1169, 1640, 2525, 4191, 3302],
                  [833, 1099, 1556, 2478, 4190, 3367],
                  [690, 978, 1296, 2603, 3844, 2945],
                  [364, 706, 548, 3763, 2381, 1273],
                  [666, 1084, 1527, 3130, 3665, 2435],
                  [500, 749, 938, 2499, 3031, 2146],
                  [558, 821, 1082, 2384, 3259, 2341],
                  [756, 1058, 1456, 2287, 3306, 2501],
                  [478, 590, 798, 1105, 1385, 990],
                  [482, 710, 972, 1909, 2769, 1822],
                  [248, 618, 378, 3899, 1921, 938],
                  [308, 659, 522, 3281, 1987, 1100]],
                 dtype=np.float32)

def test_medoid_shape():
    a = np.random.normal(1, size=(6, 10))
    # no axis defined
    m = hd.medoid(a)
    assert_equal(m.shape, (6, ))
    # axis zero
    m = hd.medoid(a, axis=0)
    assert_equal(m.shape, (10, ))
    # axis one
    m = hd.medoid(a, axis=1)
    assert_equal(m.shape, (6, ))
 
def test_medoid_in_set():
    a = np.random.normal(1, size=(6, 10))
    s = [list(x) for x in a.T]
    m = hd.medoid(a)
    idx = s.index(list(m))
    assert_true(idx <= 10)