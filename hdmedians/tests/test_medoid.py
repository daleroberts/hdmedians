"""
Tests.
"""

import numpy as np
import hdmedians as hd

from numpy.testing import assert_equal, assert_array_almost_equal
from nose.tools import assert_true, assert_raises

# shape (6, 25)
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
                  [308, 659, 522, 3281, 1987, 1100]]).T


def test_medoid_shape_noaxis():
    a = np.random.normal(1, size=(6, 10))
    m = hd.medoid(a)
    assert_equal(m.shape, (6, ))


def test_medoid_shape_axis_zero():
    a = np.random.normal(1, size=(6, 10))
    m = hd.medoid(a, axis=0)
    assert_equal(m.shape, (10, ))


def test_medoid_shape_axis_one():
    a = np.random.normal(1, size=(6, 10))
    m = hd.medoid(a, axis=1)
    assert_equal(m.shape, (6, ))


def test_medoid_in_set_random():
    a = np.random.normal(1, size=(6, 10))
    s = [list(x) for x in a.T]
    m = hd.medoid(a)
    idx = s.index(list(m))
    assert_true(idx > -1)


def test_medoid_noaxis():
    m = hd.medoid(DATA1)
    r = np.array([721,  966, 1227, 2249, 3577, 2693])
    assert_equal(m, r)


def test_medoid_axis_zero():
    m = hd.medoid(DATA1, axis=0)
    r = np.array([1281, 1128, 932, 870, 888,
                  1227, 1213, 1375, 1454, 1353,
                  1592, 1606, 1609, 1640, 1556,
                  1296, 548, 1527, 938, 1082,
                  1456, 798, 972, 378, 522])
    assert_equal(m, r)


def test_medoid_axis_one():
    m = hd.medoid(DATA1, axis=1)
    r = np.array([721,  966, 1227, 2249, 3577, 2693])
    assert_equal(m, r)


def test_medoid_axis_bad():
    assert_raises(IndexError, hd.medoid, DATA1, axis=2)


def test_medoid_noaxis_indexonly():
    m = hd.medoid(DATA1, indexonly=True)
    assert_equal(m, 5)


def test_medoid_axis_zero_indexonly():
    m = hd.medoid(DATA1, axis=0, indexonly=True)
    assert_equal(m, 2)


def test_medoid_axis_one_indexonly():
    m = hd.medoid(DATA1, axis=1, indexonly=True)
    assert_equal(m, 5)


def test_medoid_1d():
    data = np.ones((1, 3))
    m = hd.medoid(data, axis=1)
    r = np.median(data, axis=1)
    assert_array_almost_equal(m, r, decimal=3)


def test_medoid_one_obs():
    data = np.array([[1.0, 2.0, 1.0]])
    m = hd.medoid(data, axis=0)
    r = np.array([1.0, 2.0, 1.0])
    assert_array_almost_equal(m, r, decimal=3)


def test_medoid_two_obs():
    data = np.array([[1.0, 2.0, 1.0],
                     [2.0, 1.0, 1.0]])
    m = hd.medoid(data, axis=0)
    r = np.array([1.0, 2.0, 1.0])
    assert_array_almost_equal(m, r, decimal=3)


def test_nanmedoid_two_obs():
    data = np.array([[1.0, np.nan, 1.0],
                     [2.0, 1.0, 1.0]])
    m = hd.nanmedoid(data, axis=0)
    r = np.array([2.0, 1.0, 1.0])
    assert_array_almost_equal(m, r, decimal=3)


def test_nanmedoid_all_nan():
    data = np.array([[np.nan, np.nan, np.nan],
                     [np.nan, np.nan, np.nan]])
    assert_raises(ValueError, hd.nanmedoid, data)


def test_nanmedoid_axis_zero():
    data = np.array([[1.0, np.nan, 1.0],
                     [2.0, 1.0, 1.0]])
    m = hd.nanmedoid(data, axis=0)
    r = np.array([2.0, 1.0, 1.0])
    assert_array_almost_equal(m, r, decimal=3)


def test_nanmedoid_axis_one():
    data = np.array([[1.0, np.nan, 1.0],
                     [2.0, 1.0, 1.0]])
    m = hd.nanmedoid(data, axis=1)
    r = np.array([1.0, 2.0])
    assert_array_almost_equal(m, r, decimal=3)


def test_nanmedoid_axis_zero_indexonly():
    data = np.array([[1.0, np.nan, 1.0],
                     [2.0, 1.0, 1.0]])
    m = hd.nanmedoid(data, axis=0, indexonly=True)
    assert_equal(m, 1)


def test_nanmedoid_axis_one_indexonly():
    data = np.array([[1.0, np.nan, 1.0],
                     [2.0, 1.0, 1.0]])
    m = hd.nanmedoid(data, axis=1, indexonly=True)
    assert_equal(m, 0)


def test_nanmedoid_axis_bad():
    assert_raises(IndexError, hd.nanmedoid, DATA1, axis=2)


def test_nanmedoid_two_obs():
    data = np.array([[1.0, np.nan, 1.0],
                     [2.0, 1.0, 1.0]])
    m = hd.nanmedoid(data, axis=0)
    r = np.array([2.0, 1.0, 1.0])
    assert_array_almost_equal(m, r, decimal=3)


def test_nanmedoid_all_nan():
    data = np.array([[np.nan, np.nan, np.nan],
                     [np.nan, np.nan, np.nan]])
    assert_raises(ValueError, hd.nanmedoid, data)
