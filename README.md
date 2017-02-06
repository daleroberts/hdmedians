# Hdmedians

Did you know there is not a unique way to extend the concept of a [median](https://en.wikipedia.org/wiki/Median) to higher dimensions?

This Python package provides a number of fast implementations of various **high-dimensional median 
algorithms** for multivariate data. Medians are extremely useful due to their high breakdown point of 50% and have
a number of nice applications in machine learning, computer vision, and high-dimensional statistics.

### Medoid

Given a finite set <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/97c2c0ac5d7c079601abd56a54c9475c.png?invert_in_darkmode" align=middle width=12.577454999999999pt height=22.027169999999977pt/> of <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/2ec6e630f199f589a2402fdf3e0289d5.png?invert_in_darkmode" align=middle width=8.008308pt height=15.034140000000015pt/>-dimensional observation vectors <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/8ce46e21b12b0c15b3683b17029ce564.png?invert_in_darkmode" align=middle width=111.746745pt height=22.698719999999994pt/>, 
the [medoid](https://en.wikipedia.org/wiki/Medoid) <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/273457f251a6f8920e7b6c485c28b74f.png?invert_in_darkmode" align=middle width=13.642034999999998pt height=15.721860000000007pt/> of these observations is given by
<p align="center"><img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/e2ab5aaffe776fde1073a90f83f75a77.png?invert_in_darkmode" align=middle width=202.62825pt height=45.437205pt/></p>

#### Example

Create a random NumPy array:
```{python}
>>> import numpy as np
>>> X = np.random.normal(1, size=(6, 10))
```

Find the medoid:
```{python}
>>> import hdmedians as hd
>>> hd.medoid(X)
array([ 0.98290681,  1.48956002,  0.4354181 ,  2.65441153,  1.526411, 0.25340115])
```

### Geometric Median

The [geometric median](https://en.wikipedia.org/wiki/Geometric_median) is also known as the 1-median, spatial median,
Euclidean minisum, or Torricelli point. Given a finite set <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/97c2c0ac5d7c079601abd56a54c9475c.png?invert_in_darkmode" align=middle width=12.577454999999999pt height=22.027169999999977pt/> of <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/2ec6e630f199f589a2402fdf3e0289d5.png?invert_in_darkmode" align=middle width=8.008308pt height=15.034140000000015pt/>-dimensional observation vectors <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/8ce46e21b12b0c15b3683b17029ce564.png?invert_in_darkmode" align=middle width=111.746745pt height=22.698719999999994pt/>, 
the geometric median <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/fb2c407771af04095047a75aab1127e2.png?invert_in_darkmode" align=middle width=9.973589999999998pt height=22.747889999999988pt/> of these observations is given by
<p align="center"><img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/24a6cad3853187faa18a0cf58c6515c8.png?invert_in_darkmode" align=middle width=204.38385pt height=45.437205pt/></p>
Note there is a subtle difference between the definition of the geometric median and the medoid: the search space 
for the solution differs (i.e., "<img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/af3d250893976cd65ed71ec1c3590423.png?invert_in_darkmode" align=middle width=46.69797pt height=22.61654999999999pt/>" vs. "<img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/fb31cf585f23aa9aadb4bd16aa2d71f8.png?invert_in_darkmode" align=middle width=41.445029999999996pt height=22.027169999999977pt/>") and has the 
effect that the medoid returns one of the observations in <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/97c2c0ac5d7c079601abd56a54c9475c.png?invert_in_darkmode" align=middle width=12.577454999999999pt height=22.027169999999977pt/> whereas the geometric median can be described 
as a synthetic (not physically observed) observation.
