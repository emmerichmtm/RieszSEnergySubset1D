# Minimizing Riesz s-Energy in Ordered Points

This repository contains a Python implementation to solve the problem of minimizing the Riesz s-energy of a subset of points chosen from a sorted list. Two methods are provided:

- **Dynamic Programming (DP):** An efficient approach that breaks the problem into subproblems.
- **Brute Force:** An exhaustive method that enumerates all possible subsets to identify the optimal configuration.

**License:** This work is licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

## Problem Statement

Given a sorted list of points `x` (in increasing order) and a parameter `s > 0`, the goal is to select a subset `S` of `k` points that minimizes the Riesz s-energy defined by

$$
E(S) = \sum_{p < q \in S} \frac{1}{(x[q] - x[p])^s}
$$

The code assumes that the input list `x` is strictly increasing, ensuring that all differences (gaps) are positive.

## Files

- **`main.py`**: Contains the complete implementation, including the dynamic programming and brute force methods, as well as example cases.
- **`README.md`**: This file, which provides an overview and documentation for the project.

## Usage

Ensure that you have Python 3 installed. You can run the script directly from the command line:

```bash
python main.py
