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


def test_geomedian_shape_noaxis():
    a = np.random.normal(1, size=(6, 10))
    m = hd.geomedian(a)
    assert_equal(m.shape, (6, ))


def test_geomedian_shape_axis_zero():
    a = np.random.normal(1, size=(6, 10))
    m = hd.geomedian(a, axis=0)
    assert_equal(m.shape, (10, ))


def test_geomedian_shape_axis_one():
    a = np.random.normal(1, size=(6, 10))
    m = hd.geomedian(a, axis=1)
    assert_equal(m.shape, (6, ))


def test_geomedian_noaxis():
    m = hd.geomedian(DATA1.astype(np.float32))
    r = np.array([684.9332, 962.1752, 1247.556, 2340.647, 3473.594, 2584.103])
    assert_array_almost_equal(m, r, decimal=3)


def test_geomedian_axis_zero():
    m = hd.geomedian(DATA1.astype(np.float32), axis=0)
    r = np.array([1374.029, 1206.014, 1107.71, 1045.085, 1059.543, 1362.539, 1341.17,
                  1496.717, 1542.327, 1475.737, 1667.315, 1689.629, 1694.82, 1718.672,
                  1655.421, 1444.762, 861.6774, 1573.617, 1099.888, 1211.265, 1483.749,
                  772.4884, 1042.317, 709.8128, 777.8592])
    assert_array_almost_equal(m, r, decimal=3)


def test_geomedian_axis_one():
    m = hd.geomedian(DATA1.astype(np.float32), axis=1)
    r = np.array([684.9332, 962.1752, 1247.556, 2340.647, 3473.594, 2584.103])
    assert_array_almost_equal(m, r, decimal=3)


def test_geomedian_same_values():
    data = np.ones((4, 2))
    m = hd.geomedian(data, axis=1)
    print(np.sum(m))
    r = np.median(data, axis=1)
    assert_array_almost_equal(m, r, decimal=3)


def test_geomedian_1d():
    data = np.ones((1, 3))
    m = hd.geomedian(data, axis=1)
    r = np.median(data, axis=1)
    assert_array_almost_equal(m, r, decimal=3)


def test_geomedian_one_obs():
    data = np.array([[1.0, 2.0, 1.0]])
    m = hd.geomedian(data, axis=0)
    r = np.array([1.0, 2.0, 1.0])
    assert_array_almost_equal(m, r, decimal=3)


def test_geomedian_two_obs():
    data = np.array([[1.0, 2.0, 1.0],
                     [2.0, 1.0, 1.0]])
    m = hd.geomedian(data, axis=0)
    r = np.array([1.5, 1.5, 1.0])
    assert_array_almost_equal(m, r, decimal=3)


def test_nangeomedian_axis_zero_one_good():
    data = np.array([[1.0, np.nan, 1.0],
                     [2.0, 1.0, 1.0]])
    m = hd.nangeomedian(data, axis=0)
    r = np.nanmedian(data, axis=0)
    assert_array_almost_equal(m, r, decimal=3)


def test_nangeomedian_axis_one_two_good():
    data = np.array([[1.0, np.nan, 1.0],
                     [2.0, 1.0, 1.0]])
    m = hd.nangeomedian(data, axis=1)
    r = np.nanmedian(data, axis=1)
    assert_array_almost_equal(m, r, decimal=3)


def test_nangeomedian_axis_bad():
    data = np.array([[1.0, np.nan, 1.0],
                     [2.0, 1.0, 1.0]])
    assert_raises(IndexError, hd.nangeomedian, data, axis=2)


def test_nangeomedian_all_nan():
    data = np.array([[np.nan, np.nan, np.nan],
                     [np.nan, np.nan, np.nan]])
    assert_raises(ValueError, hd.nangeomedian, data)
