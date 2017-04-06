# Hdmedians

Did you know there is no unique way to mathematically extend the concept of a
[median](https://en.wikipedia.org/wiki/Median) to higher dimensions?

Various definitions for a **high-dimensional median** exist and this Python
package provides a number of fast implementations of these definitions.
Medians are extremely useful due to their high breakdown point (up to 50%
contamination) and have a number of nice applications in machine learning,
computer vision, and high-dimensional statistics.

<p align="center">
<img src="https://rawgit.com/daleroberts/hdmedians/master/docs/fig1.svg" width=600px height=180px />
</p>

This package currently has implementations of [medoid](#medoid) and [geometric
median](#geometric-median) with support for missing data using `NaN`. 

### Installation

The latest version of the package is always available on [pypi](https://pypi.python.org/pypi/hdmedians), 
so can be easily installed by typing:
```{sh}
pip3 install hdmedians
```

## Medoid

Given a finite set <img src="https://rawgit.com/daleroberts/hdmedians/master/docs/97c2c0ac5d7c079601abd56a54c9475c.svg?invert_in_darkmode" align=middle width=12.577454999999999pt height=22.027169999999977pt/> of <img src="https://rawgit.com/daleroberts/hdmedians/master/docs/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode" align=middle width=8.008308pt height=15.034140000000015pt/>-dimensional observation vectors <img src="https://rawgit.com/daleroberts/hdmedians/master/docs/8ce46e21b12b0c15b3683b17029ce564.svg?invert_in_darkmode" align=middle width=111.746745pt height=22.698719999999994pt/>, 
the [medoid](https://en.wikipedia.org/wiki/Medoid) <img src="https://rawgit.com/daleroberts/hdmedians/master/docs/273457f251a6f8920e7b6c485c28b74f.svg?invert_in_darkmode" align=middle width=13.642034999999998pt height=15.721860000000007pt/> of these observations is given by
<p align="center"><img src="https://rawgit.com/daleroberts/hdmedians/master/docs/e2ab5aaffe776fde1073a90f83f75a77.svg?invert_in_darkmode" align=middle width=202.62825pt height=45.437205pt/></p>

The current implementation of `medoid` is in vectorized Python and can handle
any data type supported by
[ndarray](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html).
If you would like the algorithm to take care of missing values encoded as `nan`
then you can use the `nanmedoid` function.

### Examples

Create an 6 x 10 array of random integer observations.
```{python}
>>> import numpy as np
>>> X = np.random.randint(100, size=(6, 10))
array([[12,  9, 61, 76,  2, 17, 12, 11, 26,  0],
       [65, 72,  7, 64, 21, 92, 51, 48,  9, 65],
       [39,  7, 50, 56, 29, 79, 47, 45, 10, 52],
       [70, 12, 23, 97, 86, 14, 42, 90, 15, 16],
       [13,  7,  2, 47, 80, 53, 23, 59,  7, 15],
       [83,  2, 40, 12, 22, 75, 69, 61, 28, 53]])
```

Find the medoid, taking the last axis as the number of observations.
```{python}
>>> import hdmedians as hd
>>> hd.medoid(X)
array([12, 51, 47, 42, 23, 69])
```

Take the first axis as the number of observations.
```{python}
>>> hd.medoid(X, axis=0)
array([39,  7, 50, 56, 29, 79, 47, 45, 10, 52])
```

Since the medoid is one of the observations, the `medoid` function has the ability to only return the index if required.
```{python}
>>> hd.medoid(X, indexonly=True)
6
>>> X[:,6]
array([12, 51, 47, 42, 23, 69])
```

## Geometric Median

The [geometric median](https://en.wikipedia.org/wiki/Geometric_median) is also known as the 1-median, spatial median,
Euclidean minisum, or Torricelli point. Given a finite set <img src="https://rawgit.com/daleroberts/hdmedians/master/docs/97c2c0ac5d7c079601abd56a54c9475c.svg?invert_in_darkmode" align=middle width=12.577454999999999pt height=22.027169999999977pt/> of <img src="https://rawgit.com/daleroberts/hdmedians/master/docs/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode" align=middle width=8.008308pt height=15.034140000000015pt/>-dimensional observation vectors <img src="https://rawgit.com/daleroberts/hdmedians/master/docs/8ce46e21b12b0c15b3683b17029ce564.svg?invert_in_darkmode" align=middle width=111.746745pt height=22.698719999999994pt/>, 
the geometric median <img src="https://rawgit.com/daleroberts/hdmedians/master/docs/fb2c407771af04095047a75aab1127e2.svg?invert_in_darkmode" align=middle width=9.973589999999998pt height=22.747889999999988pt/> of these observations is given by
<p align="center"><img src="https://rawgit.com/daleroberts/hdmedians/master/docs/24a6cad3853187faa18a0cf58c6515c8.svg?invert_in_darkmode" align=middle width=204.38385pt height=45.437205pt/></p>
Note there is a subtle difference between the definition of the geometric median and the medoid: the search space 
for the solution differs and has the effect that the medoid returns one of the true observations whereas the geometric median can be described 
as a synthetic (not physically observed) observation.

The current implementation of `geomedian` uses Cython and can handle `float64`
or `float32`. If you would like the algorithm to take care of missing values
encoded as `nan` then you can use the `nangeomedian` function.

### Examples

Create an 6 x 10 array of random `float64` observations.
```{python}
>>> import numpy as np
>>> np.set_printoptions(precision=4, linewidth=200)
>>> X = np.random.normal(1, size=(6, 10))
array([[ 1.1079,  0.5763,  0.3072,  1.2205,  0.8596, -1.5082,  2.5955,  2.8251,  1.5908,  0.4575],
       [ 1.555 ,  1.7903,  1.213 ,  1.1285,  0.0461, -0.4929, -0.1158,  0.5879,  1.5807,  0.5828],
       [ 2.1583,  3.4429,  0.4166,  1.0192,  0.8308, -0.1468,  2.6329,  2.2239,  0.2168,  0.8783],
       [ 0.7382,  1.9453,  0.567 ,  0.6797,  1.1654, -0.1556,  0.9934,  0.1857,  1.369 ,  2.1855],
       [ 0.1727,  0.0835,  0.5416,  1.4416,  1.6921,  1.6636,  1.6421,  1.0687,  0.6075, -0.0301],
       [ 2.6654,  1.6741,  1.1568,  1.3092,  1.6944,  0.2574,  2.8604,  1.6102,  0.4301, -0.3876]])
>>> X.dtype
dtype('float64')
```

Find the geometric median, taking the last axis as the number of observations.
```{python}
>>> import hdmedians as hd
>>> np.array(hd.geomedian(X))
array([ 1.0733,  0.8974,  1.1935,  0.9122,  0.9975,  1.3422])
```

Take the first axis as the number of observations.
```{python}
>>> np.array(hd.geomedian(X, axis=0))
array([ 1.4581,  1.6377,  0.7147,  1.1257,  1.0493, -0.091 ,  1.7907,  1.4168,  0.9587,  0.6195])
```

Convert to `float32` and compute the geometric median.
```{python}
>>> X = X.astype(np.float32)
>>> m = hd.geomedian(X)
```

## References

  * Small, C. G. (1990). [A survey of multidimensional medians](http://www.jstor.org/stable/1403809). *International Statistical Review/Revue Internationale de Statistique*, 263-277.
