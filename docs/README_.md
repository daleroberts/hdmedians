# Hdmedians

Did you know there is not a unique way to extend the concept of a [median](https://en.wikipedia.org/wiki/Median) to higher dimensions?

This Python package provides a number of fast implementations of various **high-dimensional median 
algorithms** for multivariate data. Medians are extremely useful due to their high breakdown point of 50% and have
a number of nice applications in machine learning, computer vision, and high-dimensional statistics.

## Medoid

Given a finite set $\mathbb{X}$ of $p$-dimensional observation vectors $\mathbb{X}=\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}$, 
the medoid $\mathbf{m}$ of these observations is given by
$$
  \mathbf{m} := \operatorname{argmin}_{\mathbf{x} \in \mathbb{X}} \sum_{i=1}^n \|\mathbf{x} - \mathbf{x}_i\|.
$$

## Geometric Median

Given a finite set $\mathbb{X}$ of $p$-dimensional observation vectors $\mathbb{X}=\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}$, 
the geometric median $\hat{\mu}$ of these observations is given by
$$
  \hat \mu := \operatorname{argmin}_{\mathbf{x} \in \mathbb{R}^p} \sum_{i=1}^n \|\mathbf{x} - \mathbf{x}_i\|.
$$
Note there is a subtle difference between the definition of the geometric median and the medoid: the search space 
for the solution differs (i.e., "$\mathbf{x} \in \mathbf{R}^p$" vs. "$\mathbf{x} \in \mathbb{X}$") and has the 
effect that the medoid returns one of the observations in $\mathbb{X}$ whereas the geometric median can be described 
as a synthetic (not physically observed) observation.