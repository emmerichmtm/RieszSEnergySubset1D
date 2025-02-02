# Minimizing Riesz s-Energy in Ordered Points

This repository contains a Python implementation to solve the problem of minimizing the Riesz s-energy of a subset of points chosen from a sorted list. Two methods are provided:

- **Dynamic Programming (DP):** An efficient approach that breaks the problem into subproblems.
- **Brute Force:** An exhaustive method that enumerates all possible subsets to identify the optimal configuration.

**License:** This work is licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

## Citation

If you use this code in your research, please consider citing it as follows:

**APA Style:**

Emmerich, M. T. M. (2025). *Riesz s-Energy Subset 1D* [Source code]. GitHub. https://github.com/emmerichmtm/RieszSEnergySubset1D

**BibTeX:**

## Citation

If you use this code in your research, please consider citing it as follows:

**APA Style:**

Emmerich, M. (2025, February 2). *Riesz s-Energy Subset 1D* [Source code]. GitHub. https://github.com/emmerichmtm/RieszSEnergySubset1D

**BibTeX:**
```bibtex
@misc{Emmerich2025RieszSEnergySubset1D,
  author       = {Michael Emmerich},
  title        = {Riesz s-Energy Subset 1D},
  year         = {2025},
  month        = feb,
  day          = {2},
  howpublished = {\url{https://github.com/emmerichmtm/RieszSEnergySubset1D}},
  note         = {Source code},
}
```

# Dynamic Programming for Riesz \(s\)-Energy Subset Selection

This repository contains implementations of dynamic programming (DP) algorithms for selecting a representative subset of points that minimizes the Riesz \(s\)-energy. In general, the Riesz \(s\)-Energy Subset Selection problem is NP hard in arbitrary dimensions (see [Pereverdieva et al., 2024](https://arxiv.org/abs/2410.18900)). However, for structured cases such as the 1-D case and the 2-D Pareto front, efficient DP schemes can be used.

## Overview

The goal is to select a subset 
\[
S = \{P_{i_1}, P_{i_2}, \dots, P_{i_k}\}
\]
from a set of \(n\) points so that the energy
\[
E(S)=\sum_{1\le p<q\le k}\frac{1}{d(P_{i_p},P_{i_q})^s}
\]
is minimized, where \(d(P, Q)\) is the Euclidean distance and \(s > 0\) is a given parameter.

- **1-D Case:**  
  When the points are real numbers (sorted in increasing order), the DP algorithm exploits the monotonicity in the distances and computes the optimal subset efficiently. The code includes both the DP solution and a brute force verification to double-check optimality.

- **2-D Pareto Front:**  
  In the biobjective setting, the points are non-dominated and sorted by increasing \(f_1\) (with decreasing \(f_2\)). A similar DP approach is applied to compute the optimal subset from the Pareto front. Again, a brute force search is available to verify the DP results.

## Included Code

- **`dp_1d.py`**:  
  Contains the implementation for the 1-D Riesz \(s\)-Energy Subset Selection problem.

- **`pareto2d.py`**:  
  Contains the dynamic programming solution for the 2-D Pareto front case.  
  This script computes, from a sorted non-dominated set of 2-D points, the subset that minimizes the Riesz \(s\)-energy.

## TikZ Illustrations

The LaTeX document provided in this repository also includes TikZ examples to illustrate:
- A 1-D example.
- Two 2-D examples with non-dominated points and their selected subsets.

These visualizations help in understanding how the DP algorithm selects the representative subset.

## Running the Code

To run any of the Python scripts, use:

```bash
python main.py



```bash
python pareto2d.py
