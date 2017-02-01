"""
Medoid implementations.
"""
import numpy as np

def euclidean(x, y):
    return np.sqrt(np.sum(np.square(x - y)))

def medoid(a, axis=None, keepdims=False, indexonly=False):
    """
    Compute the medoid along the specified axis.

    Returns the medoid of the array elements.
    Parameters
    ----------
    a : array_like
        Input array or object that can be converted to an array.
    axis : int
        Axis or axes along which the medians are computed. The default
        is to compute the median along the last axis of the array.
    keepdims : bool, optional
        If this is set to True, the axes which are reduced are left
        in the result as dimensions with size one. With this option,
        the result will broadcast correctly against the original `arr`.
    Returns
    -------
    medoid : ndarray
        A new array holding the result. If the input contains integers
        or floats smaller than ``float64``, then the output data-type is
        ``np.float64``.  Otherwise, the data-type of the output is the
        same as that of the input. If `out` is specified, that array is
        returned instead.
    """
    if axis == 0:
        a = a.T

    _, n = a.shape
    d = np.empty(n)
    for i in range(n):
        d[i] = np.sum([euclidean(a[:, i], a[:, j])
                       for j in range(n) if j != i])
    i = np.argmin(d)

    if indexonly:
        return i
    else:
        return a[:, i]
