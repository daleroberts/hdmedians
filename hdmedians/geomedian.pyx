# Copyright (C) 2017 Dale Roberts - All Rights Reserved

# cython: cdivision=True
# cython: boundscheck=False
# cython: nonecheck=False
# cython: wraparound=False

import numpy as np
import warnings

from libc.math cimport isnan, sqrt, acos, fabs

cimport numpy as cnp

ctypedef fused floating:
    cnp.float32_t
    cnp.float64_t

ctypedef cnp.float32_t float32_t
ctypedef cnp.float64_t float64_t

cdef floating dot(floating[:] x, floating[:] y) nogil:
    cdef size_t n = x.shape[0]
    cdef size_t i = 0
    cdef float64_t result = 0.
    for i in range(n):
        result += x[i] * y[i]
    return <floating>result

cdef floating sum(floating[:] x) nogil:
    cdef size_t n = x.shape[0]
    cdef float64_t total = 0.
    for i in range(n):
        total += x[i]
    return <floating>total

cdef floating nansum(floating[:] x) nogil:
    cdef size_t n = x.shape[0]
    cdef float64_t total = 0.
    for i in range(n):
        if not isnan(x[i]):
            total += x[i]
    return <floating>total

cdef floating dist_naneuclidean(floating[:] x, floating[:] y) nogil:
    cdef size_t n = x.shape[0]
    cdef float64_t d = 0.
    cdef float64_t tmp
    for i in range(n):
        if (not isnan(x[i])) and (not isnan(y[i])):
            tmp = x[i] - y[i]
            d += tmp * tmp
    return <floating>sqrt(d)

cdef floating dist_euclidean(floating[:] x, floating[:] y) nogil:
    cdef size_t n = x.shape[0]
    cdef float64_t d = 0.
    cdef float64_t tmp
    for i in range(n):
        tmp = x[i] - y[i]
        d += tmp * tmp
    return <floating>sqrt(d)

cdef floating norm_euclidean(floating[:] x) nogil:
    cdef size_t n = x.shape[0]
    cdef float64_t d = 0.
    for i in range(n):
        d += x[i] * x[i]
    return <floating>sqrt(d)

cdef geomedian_axis_zero(floating[:, :] X, floating eps=1e-7,
                         size_t maxiters=500):
    cdef size_t p = X.shape[0]
    cdef size_t n = X.shape[1]

    cdef floating[:] y = np.mean(X, axis=0)

    if p == 0:
        return y

    if floating is cnp.float32_t:
        dtype = np.float32
    else:
        dtype = np.float64

    cdef floating[:] D = np.empty(p, dtype=dtype)
    cdef floating[:] Dinv = np.empty(p, dtype=dtype)
    cdef floating[:] W = np.empty(p, dtype=dtype)
    cdef floating[:] T = np.empty(n, dtype=dtype)
    cdef floating[:] y1 = np.empty(n, dtype=dtype)
    cdef floating[:] R = np.empty(n, dtype=dtype)

    cdef floating dist, Dinvs, total, r, rinv, tmp, Di
    cdef size_t nzeros = p
    cdef size_t iteration

    with nogil:
        iteration = 0
        while iteration < maxiters:

            for i in range(p):
                Di = dist_euclidean(X[i, :], y)
                if fabs(Di) > eps:
                    Dinv[i] = 1. / Di
                else:
                    Dinv[i] = 0.
                D[i] = Di

            Dinvs = sum(Dinv)

            for i in range(p):
                W[i] = Dinv[i] / Dinvs

            for j in range(n):
                total = 0.
                for i in range(p):
                    if fabs(D[i]) > eps:
                        total += W[i] * X[i, j]
                T[j] = total

            nzeros = p
            for i in range(p):
                if fabs(D[i]) > eps:
                    nzeros -= 1

            if nzeros == 0:
                y1 = T
            elif nzeros == p:
                break
            else:
                for j in range(n):
                    R[j] = (T[j] - y[j]) * Dinvs
                r = norm_euclidean(R)
                if r > eps:
                    rinv = nzeros/r
                else:
                    rinv = 0.
                for j in range(n):
                    y1[j] = max(0, 1-rinv)*T[j] + min(1, rinv)*y[j]

            dist = dist_euclidean(y, y1)
            if dist < eps:
               break

            y[:] = y1
            iteration = iteration + 1
    
    return y

cdef geomedian_axis_one(floating[:, :] X, floating eps=1e-7,
                           size_t maxiters=500):
    cdef size_t p = X.shape[0]
    cdef size_t n = X.shape[1]

    cdef floating[:] y = np.mean(X, axis=1)

    if n == 1:
        return y

    if floating is cnp.float32_t:
        dtype = np.float32
    else:
        dtype = np.float64

    cdef floating[:] D = np.empty(n, dtype=dtype)
    cdef floating[:] Dinv = np.empty(n, dtype=dtype)
    cdef floating[:] W = np.empty(n, dtype=dtype)
    cdef floating[:] T = np.empty(p, dtype=dtype)
    cdef floating[:] y1 = np.empty(p, dtype=dtype)
    cdef floating[:] R = np.empty(p, dtype=dtype)

    cdef floating dist, Dinvs, total, r, rinv, tmp, Di
    cdef size_t nzeros = n
    cdef size_t iteration

    with nogil:
        iteration = 0
        while iteration < maxiters:

            for i in range(n):
                Di = dist_euclidean(X[:, i], y)
                D[i] = Di
                if fabs(Di) > eps:
                    Dinv[i] = 1. / Di
                else:
                    Dinv[i] = 0.

            Dinvs = sum(Dinv)

            for i in range(n):
                W[i] = Dinv[i] / Dinvs

            for j in range(p):
                total = 0.
                for i in range(n):
                    if fabs(D[i]) > eps:
                        total += W[i] * X[j, i]
                T[j] = total

            nzeros = n
            for i in range(n):
                if fabs(D[i]) > eps:
                    nzeros -= 1

            if nzeros == 0:
                y1 = T
            elif nzeros == n:
                break
            else:
                for j in range(p):
                    R[j] = (T[j] - y[j]) * Dinvs
                r = norm_euclidean(R)
                if r > eps:
                    rinv = nzeros/r
                else:
                    rinv = 0.
                for j in range(p):
                    y1[j] = max(0, 1-rinv)*T[j] + min(1, rinv)*y[j]

            dist = dist_euclidean(y, y1)
            if dist < eps:
               break

            y[:] = y1
            iteration = iteration + 1
            
    return y



cdef nangeomedian_axis_zero(floating[:, :] X, floating eps=1e-7,
                            size_t maxiters=500):
    cdef size_t p = X.shape[0]
    cdef size_t n = X.shape[1]

    cdef floating nan = <floating>float('NaN')

    cdef floating[:] y = np.nanmean(X, axis=0)

    if floating is cnp.float32_t:
        dtype = np.float32
    else:
        dtype = np.float64

    cdef floating[:] D = np.empty(p, dtype=dtype)
    cdef floating[:] Dinv = np.empty(p, dtype=dtype)
    cdef floating[:] W = np.empty(p, dtype=dtype)
    cdef floating[:] T = np.empty(n, dtype=dtype)
    cdef floating[:] y1 = np.empty(n, dtype=dtype)
    cdef floating[:] R = np.empty(n, dtype=dtype)

    cdef floating dist, Dinvs, total, r, rinv, tmp, Di
    cdef size_t nzeros = p
    cdef size_t iteration

    with nogil:
        iteration = 0
        while iteration < maxiters:

            for i in range(p):
                Di = dist_euclidean(X[i, :], y)
                if fabs(Di) > 0.:
                    Dinv[i] = 1. / Di
                else:
                    Dinv[i] = nan
                D[i] = Di

            Dinvs = nansum(Dinv)

            for i in range(p):
                W[i] = Dinv[i] / Dinvs

            for j in range(n):
                total = 0.
                for i in range(p):
                   tmp = W[i] * X[i, j]
                   if not isnan(tmp):
                       total += tmp
                T[j] = total

            nzeros = p
            for i in range(p):
                if isnan(D[i]):
                    nzeros -= 1
                elif fabs(D[i]) > 0.:
                    nzeros -= 1

            if nzeros == 0:
                y1 = T
            elif nzeros == p:
                break
            else:
                for j in range(n):
                    R[j] = (T[j] - y[j]) * Dinvs
                r = norm_euclidean(R)
                if r > 0.:
                    rinv = nzeros/r
                else:
                    rinv = 0.
                for j in range(n):
                    y1[j] = max(0, 1-rinv)*T[j] + min(1, rinv)*y[j]

            dist = dist_euclidean(y, y1)
            if dist < eps:
               break

            y[:] = y1
            iteration = iteration + 1
            
    return y1

cdef nangeomedian_axis_one(floating[:, :] X, floating eps=1e-7,
                           size_t maxiters=500):
    cdef size_t p = X.shape[0]
    cdef size_t n = X.shape[1]

    cdef floating nan = <floating>float('NaN')

    cdef floating[:] y = np.nanmean(X, axis=1)

    if floating is cnp.float32_t:
        dtype = np.float32
    else:
        dtype = np.float64

    cdef floating[:] D = np.empty(n, dtype=dtype)
    cdef floating[:] Dinv = np.empty(n, dtype=dtype)
    cdef floating[:] W = np.empty(n, dtype=dtype)
    cdef floating[:] T = np.empty(p, dtype=dtype)
    cdef floating[:] y1 = np.empty(p, dtype=dtype)
    cdef floating[:] R = np.empty(p, dtype=dtype)

    cdef floating dist, Dinvs, total, r, rinv, tmp, Di
    cdef size_t nzeros = n
    cdef size_t iteration

    with nogil:
        iteration = 0
        while iteration < maxiters:

            for i in range(n):
                Di = dist_euclidean(X[:, i], y)
                if fabs(Di) > 0.:
                    Dinv[i] = 1. / Di
                else:
                    Dinv[i] = nan
                D[i] = Di

            Dinvs = nansum(Dinv)

            for i in range(n):
                W[i] = Dinv[i] / Dinvs

            for j in range(p):
                total = 0.
                for i in range(n):
                   tmp = W[i] * X[j, i]
                   if not isnan(tmp):
                       total += tmp
                T[j] = total

            nzeros = n
            for i in range(n):
                if isnan(D[i]):
                    nzeros -= 1
                elif fabs(D[i]) > 0.:
                    nzeros -= 1

            if nzeros == 0:
                y1 = T
            elif nzeros == n:
                break
            else:
                for j in range(p):
                    R[j] = (T[j] - y[j]) * Dinvs
                r = norm_euclidean(R)
                if r > 0.:
                    rinv = nzeros/r
                else:
                    rinv = 0.
                for j in range(p):
                    y1[j] = max(0, 1-rinv)*T[j] + min(1, rinv)*y[j]

            dist = dist_euclidean(y, y1)
            if dist < eps:
               break

            y[:] = y1
            iteration = iteration + 1
            
    return y1

cpdef geomedian(floating[:, :] X, size_t axis=1, floating eps=1e-8,
                 size_t maxiters=1000):
    """Calculates a Geometric Median for an array `X` of
    shape (p,n).

    If the median is calculated across axis=1 (default)
    (the axis of size n) an array of size (p,1) is
    returned.
    """
    if axis == 0:
        return geomedian_axis_zero(X, eps, maxiters)

    if axis == 1:
        return geomedian_axis_one(X, eps, maxiters)
        
    raise IndexError("axis {} out of bounds".format(axis)) 


cpdef nangeomedian(floating[:, :] X, size_t axis=1, floating eps=1e-7,
                 size_t maxiters=500):
    """Calculates a Geometric Median for an array `X` of
    shape (p,n).

    If the median is calculated across axis=1 (default)
    (the axis of size n) an array of size (p,1) is
    returned.
    
    Missing values should be assigned as `np.nan`.
    """
    if axis == 0:
        ngood = np.count_nonzero(~np.isnan(X).any(axis=1))
        if ngood == 0:
            raise ValueError("All-NaN slice encountered")
        elif ngood < 3:
            return np.nanmedian(X, axis=axis)
        else:
            return nangeomedian_axis_zero(X, eps, maxiters)

    if axis == 1:
        ngood = np.count_nonzero(~np.isnan(X).any(axis=0))
        if ngood == 0:
            raise ValueError("All-NaN slice encountered")
        elif ngood < 3:
            return np.nanmedian(X, axis=axis)
        else:
            return nangeomedian_axis_one(X, eps, maxiters)

    raise IndexError("axis {} out of bounds".format(axis)) 
