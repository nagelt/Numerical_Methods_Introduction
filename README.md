# Introduction to numerical methods using Jupyter Notebooks

A set of Jupyter Notebooks demonstrating various numerical methods in Python. Among those are:


- Single-step time integration: Euler forward and backward, Crank-Nicolson.
- Finite difference, finite element, collocation, subdomain, least-squares methods
- Iterative Picard and Newton-Raphsons solution methods
- Stabilization methods: Mass lumping and finite increment calculus
- First aspects of localization of softening material models
- Concepts of staggered and monolithic coupling schemes


Illustrative examples chosen include first order models, beam bending theories and Terzaghi consolidation. 

The notebooks mainly make use of

- numpy
- scipy
- matplotlib
- ipywidgets
- sympy

The latter allows an interactive adaptation of parameters to immediatly illustrate their effect, e.g. the time-step size.

The notebooks can be viewed with nbviewer, see https://jupyter.org/, or can now also be run interactively using binder (available through nbviewer).

See https://nagelt.github.io

*Comments and contributions are welcome.*

**Related publication:**

Kern, D., & Nagel, T. (2022). An experimental numerics approach to the terrestrial brachistochrone. GAMM Archive for Students, 4(1), 29–35. https://doi.org/10.14464/gammas.v4i1.512
