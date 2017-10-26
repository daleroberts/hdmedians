# Copyright (C) 2016-2017 Dale Roberts - All Rights Reserved

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
        ssum = np.einsum('ijk,ijk->ij', diff, diff)
        idx = np.argmin(np.sum(np.sqrt(ssum), axis=1))
        if indexonly:
            return idx
        else:
            return a[:, idx]

    if axis == 0:
        diff = a[:, None, :] - a
        ssum = np.einsum('ijk,ijk->ij', diff, diff)
        idx = np.argmin(np.sum(np.sqrt(ssum), axis=1))
        if indexonly:
            return idx
        else:
            return a[idx, :]

    raise IndexError("axis {} out of bounds".format(axis)) 


def nanmedoid(a, axis=1, indexonly=False):
    """
    Compute the medoid along the specified axis, omitting
    observations containing NaNs.

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
        ssum = np.einsum('ijk,ijk->ij', diff, diff)
        dist = np.nansum(np.sqrt(ssum), axis=1) 
        mask = np.isnan(a).any(axis=0)
        dist[mask] = np.nan
        idx = np.nanargmin(dist)
        if indexonly:
            return idx
        else:
            return a[:, idx]

    if axis == 0:
        diff = a[:, None, :] - a
        ssum = np.einsum('ijk,ijk->ij', diff, diff)
        dist = np.nansum(np.sqrt(ssum), axis=1) 
        mask = np.isnan(a).any(axis=1)
        dist[mask] = np.nan
        idx = np.nanargmin(dist)
        if indexonly:
            return idx
        else:
            return a[idx, :]

    raise IndexError("axis {} out of bounds".format(axis)) 
