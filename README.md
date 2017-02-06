# Hdmedians

Did you know there is not a unique way to extend the concept of a [median](https://en.wikipedia.org/wiki/Median) to higher dimensions?

This Python package provides a number of fast implementations of various **high-dimensional median 
algorithms** for multivariate data. Medians are extremely useful due to their high breakdown point of 50% and have
a number of nice applications in machine learning, computer vision, and high-dimensional statistics.

This package currently has implementations of [medoid](#medoid) and [geometric median](#geometric-median) with 
support for missing data using `NaN`. It is easily installed by typing
```{sh}
<img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/e434f6de38c995d9cdab973d767d796a.png?invert_in_darkmode" align=middle width=165.973665pt height=79.41153pt/>\mathbb{X}<img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/e9e392f5b0eee55a2e294bf737406c2f.png?invert_in_darkmode" align=middle width=18.555075pt height=21.879660000000005pt/>p<img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/9a69db764ef42f26b8985aeca3d39ba9.png?invert_in_darkmode" align=middle width=223.20886499999997pt height=21.879660000000005pt/>\mathbb{X}=\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}<img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/3701f7a72ee07d118cb3f467e211f9dd.png?invert_in_darkmode" align=middle width=393.643965pt height=22.698719999999994pt/>\mathbf{m}<img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/cc257b70884a684ce6ddee390d176508.png?invert_in_darkmode" align=middle width=206.505915pt height=21.879660000000005pt/><img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/d860dc5ef8ee9b2127def8a8ed2ddebd.png?invert_in_darkmode" align=middle width=215.679915pt height=26.71283999999997pt/><img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/4180412801f6665b049a3d631c19f4ef.png?invert_in_darkmode" align=middle width=1172.9552999999999pt height=560.80596pt/>\mathbb{X}<img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/e9e392f5b0eee55a2e294bf737406c2f.png?invert_in_darkmode" align=middle width=18.555075pt height=21.879660000000005pt/>p<img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/9a69db764ef42f26b8985aeca3d39ba9.png?invert_in_darkmode" align=middle width=223.20886499999997pt height=21.879660000000005pt/>\mathbb{X}=\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}<img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/1f2a72531e5a196233138861065999e5.png?invert_in_darkmode" align=middle width=145.703085pt height=21.879660000000005pt/>\hat{\mu}<img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/cc257b70884a684ce6ddee390d176508.png?invert_in_darkmode" align=middle width=206.505915pt height=21.879660000000005pt/><img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/95da31970158bdbe88c4b5eeeb7a01af.png?invert_in_darkmode" align=middle width=217.43551499999998pt height=26.71283999999997pt/><img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/8f4b5485b718ef52ec71fce98d4342b0.png?invert_in_darkmode" align=middle width=942.6732150000001pt height=22.698719999999994pt/>\mathbf{x} \in \mathbf{R}^p<img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/75f7da71476ed18018bb65dc5103af7f.png?invert_in_darkmode" align=middle width=33.965745pt height=15.312659999999976pt/>\mathbf{x} \in \mathbb{X}<img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/ec16505f0720df975846ae08cf9bbd39.png?invert_in_darkmode" align=middle width=446.99506499999995pt height=22.698719999999994pt/>\mathbb{X}$ whereas the geometric median can be described 
as a synthetic (not physically observed) observation.

#### Examples

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

### References

  * Small, C. G. (1990). [A survey of multidimensional medians](http://www.jstor.org/stable/1403809). *International Statistical Review/Revue Internationale de Statistique*, 263-277.

  
