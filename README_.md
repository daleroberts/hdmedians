# High-dimensional medians

Fast implementations of some high-dimensional medians.


### Medoid

Given a finite set $\mathbb{X}$ of $p$-band pixel observations modelled by vectors $\mathbb{X}=\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}$, the medoid of these observations is
$$
  \text{medoid} := \argmin_{\x \in \X} \sum_{i=1}^n \|\x - \x_i\|.
$$

Testing again and again and again