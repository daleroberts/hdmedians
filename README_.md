# High-dimensional medians

Did you know there is not a unique way to extend the concept of a [median](https://en.wikipedia.org/wiki/Median) to higher dimensions?

This Python package provides a number of fast implementations of high-dimensional median 
algorithms. Medians are extremely useful due to their high breakdown point of 50% and have
a number of nice applications in machine learning, computer vision, and high-dimensional statistics.

## Medoid

Given a finite set $\mathbb{X}$ of $p$-dimensional observation vectors $\mathbb{X}=\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}$, 
the medoid $\mathbf{m}$ of these observations is given by
$$
  \mathbf{m} := \operatorname{argmin}_{\mathbf{x} \in \mathbb{X}} \sum_{i=1}^n \|\mathbf{x} - \mathbf{x}_i\|.
$$

## Geometric Median