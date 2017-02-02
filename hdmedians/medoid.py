"""
Medoid.
"""
import numpy as np


def medoid(a, axis=1, indexonly=False):
    """
    Compute the medoid along the specified axis.

    Returns the medoid of the array elements.

    Parameters
    ----------
    a : array_like
        Input array or object that can be converted to an array.
    axis : int
        Axis along which the medoid is computed. The default
        is to compute the median along the last axis of the array.
    indexonly : bool, optional
        If this is set to True, only the index of the medoid is returned.
    Returns
    -------
    medoid : ndarray or int
    """
    if axis == 1:
        diff = a.T[:, None, :] - a.T
        idx = np.argmin(np.sum(np.sqrt(np.einsum('ijk,ijk->ij',
                                                 diff, diff)), axis=1))
        if indexonly:
            return idx
        else:
            return a[:, idx]
    elif axis == 0:
        diff = a[:, None, :] - a
        idx = np.argmin(np.sum(np.sqrt(np.einsum('ijk,ijk->ij',
                                                 diff, diff)), axis=1))
        if indexonly:
            return idx
        else:
            return a[idx, :]
    else:
        raise ValueError("Array must be two-dimensional.")

# SLOWER:
# idx = np.argmin(np.sum(np.sqrt(np.sum(np.square(a[None,:,:].T-a[None,:,:]),axis=1)),axis=1))
