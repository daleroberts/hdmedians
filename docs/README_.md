# Hdmedians

Did you know there is not a unique way to extend the concept of a [median](https://en.wikipedia.org/wiki/Median) to higher dimensions?

This Python package provides a number of fast implementations of various **high-dimensional median 
algorithms** for multivariate data. Medians are extremely useful due to their high breakdown point of 50% and have
a number of nice applications in machine learning, computer vision, and high-dimensional statistics.

### Medoid

Given a finite set $\mathbb{X}$ of $p$-dimensional observation vectors $\mathbb{X}=\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}$, 
the [medoid](https://en.wikipedia.org/wiki/Medoid) $\mathbf{m}$ of these observations is given by
$$
  \mathbf{m} := \operatorname{argmin}_{\mathbf{x} \in \mathbb{X}} \sum_{i=1}^n \|\mathbf{x} - \mathbf{x}_i\|.
$$

#### Examples

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

Only return the index.
```{python}
>>> hd.medoid(X, indexonly=True)
6
>>> X[:,6]
array([12, 51, 47, 42, 23, 69])
```

### Geometric Median

The [geometric median](https://en.wikipedia.org/wiki/Geometric_median) is also known as the 1-median, spatial median,
Euclidean minisum, or Torricelli point. Given a finite set $\mathbb{X}$ of $p$-dimensional observation vectors $\mathbb{X}=\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}$, 
the geometric median $\hat{\mu}$ of these observations is given by
$$
  \hat \mu := \operatorname{argmin}_{\mathbf{x} \in \mathbb{R}^p} \sum_{i=1}^n \|\mathbf{x} - \mathbf{x}_i\|.
$$
Note there is a subtle difference between the definition of the geometric median and the medoid: the search space 
for the solution differs (i.e., "$\mathbf{x} \in \mathbf{R}^p$" vs. "$\mathbf{x} \in \mathbb{X}$") and has the 
effect that the medoid returns one of the observations in $\mathbb{X}$ whereas the geometric median can be described 
as a synthetic (not physically observed) observation.