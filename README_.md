# High-dimensional medians

Fast implementations of some high-dimensional medians.


### Medoid

Given a finite set $\mathbb{X}$ of $p$-band pixel observations modelled by vectors $\mathbb{X}=\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}$, the medoid of these observations is
$$
  \text{medoid} := \operatorname{argmin}_{\mathbf{x} \in \mathbb{X}} \sum_{i=1}^n \|\mathbf{x} - \mathbf{x}_i\|.
$$

Testing again and again and again $20\pi$