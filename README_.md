# High-dimensional medians

Fast implementations of some high-dimensional medians.


## Medoid

Given a finite set $\mathbb{X}$ of $p$-band pixel observations modelled by 
vectors $\mathbb{X}=\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}$, the medoid $\mathbf{m}$
of these observations is
$$
  \mathbf{m} := \operatorname{argmin}_{\mathbf{x} \in \mathbb{X}} \sum_{i=1}^n \|\mathbf{x} - \mathbf{x}_i\|.
$$
