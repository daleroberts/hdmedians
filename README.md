# Hdmedians

Did you know there is not a unique way to extend the concept of a [median](https://en.wikipedia.org/wiki/Median) to higher dimensions?

This Python package provides a number of fast implementations of **high-dimensional median 
algorithms**. Medians are extremely useful due to their high breakdown point of 50% and have
a number of nice applications in machine learning, computer vision, and high-dimensional statistics.

## Medoid

Given a finite set <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/97c2c0ac5d7c079601abd56a54c9475c.png?invert_in_darkmode" align=middle width=12.577454999999999pt height=22.027169999999977pt/> of <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/2ec6e630f199f589a2402fdf3e0289d5.png?invert_in_darkmode" align=middle width=8.008308pt height=15.034140000000015pt/>-dimensional observation vectors <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/8ce46e21b12b0c15b3683b17029ce564.png?invert_in_darkmode" align=middle width=111.746745pt height=22.698719999999994pt/>, 
the *medoid* <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/273457f251a6f8920e7b6c485c28b74f.png?invert_in_darkmode" align=middle width=13.642034999999998pt height=15.721860000000007pt/> of these observations is given by
<p align="center"><img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/e2ab5aaffe776fde1073a90f83f75a77.png?invert_in_darkmode" align=middle width=202.62825pt height=45.437205pt/></p>

## Geometric Median

Given a finite set <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/97c2c0ac5d7c079601abd56a54c9475c.png?invert_in_darkmode" align=middle width=12.577454999999999pt height=22.027169999999977pt/> of <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/2ec6e630f199f589a2402fdf3e0289d5.png?invert_in_darkmode" align=middle width=8.008308pt height=15.034140000000015pt/>-dimensional observation vectors <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/8ce46e21b12b0c15b3683b17029ce564.png?invert_in_darkmode" align=middle width=111.746745pt height=22.698719999999994pt/>, 
the *geometric median* <img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/fb2c407771af04095047a75aab1127e2.png?invert_in_darkmode" align=middle width=9.973589999999998pt height=22.747889999999988pt/> of these observations is given by
<p align="center"><img src="https://github.com/daleroberts/hdmedians/raw\/master/docs/24a6cad3853187faa18a0cf58c6515c8.png?invert_in_darkmode" align=middle width=204.38385pt height=45.437205pt/></p>
