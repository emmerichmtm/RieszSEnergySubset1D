import math
import itertools

def euclidean_distance(p, q):
    """
    Compute the Euclidean distance between two 2-D points p and q.
    """
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

def dp_subset_selection(points, k, s):
    """
    Perform dynamic programming to select a subset of k points (from the
    list 'points') that minimizes the Riesz s-energy.

    Parameters:
        points: A list of 2-D tuples representing Pareto points.
                (Assumed to be sorted by the first coordinate ascending, 
                 and the second coordinate descending.)
        k:      The desired number of points in the representative subset.
        s:      The parameter in the Riesz s-energy (e.g., s=1).

    Returns:
        A tuple (final_energy, final_subset) where:
            - final_energy is the total Riesz s-energy of the selected subset.
            - final_subset is a list of indices corresponding to the selected points.
    """
    n = len(points)
    # dp[r][i] will store (energy, subset) for selecting r points from points[0:i+1]
    # with points[i] as the last selected point.
    dp = [[None] * n for _ in range(k + 1)]
    
    # Base case: selecting 1 point yields zero energy.
    for i in range(n):
        dp[1][i] = (0.0, [i])
    
    # Fill the DP table for r = 2, 3, ..., k.
    for r in range(2, k + 1):
        for i in range(r - 1, n):  # i must be at least r-1 (0-indexed)
            best_energy = float('inf')
            best_subset = None
            # Try all possible previous endpoints p for the (r-1)-subset.
            for p in range(r - 2, i):
                if dp[r - 1][p] is None:
                    continue
                prev_energy, subset = dp[r - 1][p]
                extra_cost = 0.0
                # Compute the extra cost for adding points[i] to the subset.
                for q in subset:
                    dist = euclidean_distance(points[q], points[i])
                    if dist == 0:
                        extra_cost = float('inf')
                        break
                    extra_cost += 1.0 / (dist ** s)
                candidate_energy = prev_energy + extra_cost
                if candidate_energy < best_energy:
                    best_energy = candidate_energy
                    best_subset = subset + [i]
            dp[r][i] = (best_energy, best_subset)
    
    # Select the best overall subset from dp[k][i] for i in range(k-1, n)
    final_energy = float('inf')
    final_subset = None
    for i in range(k - 1, n):
        if dp[k][i] is None:
            continue
        energy, subset = dp[k][i]
        if energy < final_energy:
            final_energy = energy
            final_subset = subset

    return final_energy, final_subset

def brute_force_subset_selection(points, k, s):
    """
    Perform a brute-force search to select a subset of k points from 'points'
    that minimizes the Riesz s-energy.

    Parameters:
        points: A list of 2-D tuples representing Pareto points.
        k:      The desired number of points.
        s:      The parameter in the Riesz s-energy.
    
    Returns:
        A tuple (best_energy, best_subset) where best_subset is a list of indices.
    """
    n = len(points)
    best_energy = float('inf')
    best_subset = None
    # Enumerate all combinations of k indices.
    for subset in itertools.combinations(range(n), k):
        energy = 0.0
        valid = True
        for i in range(k):
            for j in range(i + 1, k):
                dist = euclidean_distance(points[subset[i]], points[subset[j]])
                if dist == 0:
                    valid = False
                    break
                energy += 1.0 / (dist ** s)
            if not valid:
                break
        if valid and energy < best_energy:
            best_energy = energy
            best_subset = list(subset)
    return best_energy, best_subset

def run_example(points, k, s, example_number):
    print("Example {}:".format(example_number))
    print("Points (sorted by first coordinate ascending, second coordinate descending):")
    for idx, point in enumerate(points):
        print("P{}: {}".format(idx + 1, point))
    dp_energy, dp_subset = dp_subset_selection(points, k, s)
    bf_energy, bf_subset = brute_force_subset_selection(points, k, s)
    
    print("\nDP Selected subset indices:", dp_subset)
    print("DP Selected subset points:", [points[i] for i in dp_subset])
    print("DP Total Riesz s-energy (s = {}): {:.3f}".format(s, dp_energy))
    
    print("\nBrute Force Selected subset indices:", bf_subset)
    print("Brute Force Selected subset points:", [points[i] for i in bf_subset])
    print("Brute Force Total Riesz s-energy (s = {}): {:.3f}".format(s, bf_energy))
    
    if dp_subset == bf_subset and abs(dp_energy - bf_energy) < 1e-6:
        print("\nThe DP solution matches the brute-force solution.")
    else:
        print("\nThe DP solution does NOT match the brute-force solution.")
    print("--------------------------------------------------\n")

def main():
    # Example 1: 
    # Points from a biobjective problem: f1 in (1,5,8,13,15,17) and f2 in (15,10,4,3,2,1).
    points1 = [
        (1, 15),   # P1
        (5, 10),   # P2
        (8, 4),    # P3
        (13, 3),   # P4
        (15, 2),   # P5
        (17, 1)    # P6
    ]
    k1 = 3
    s = 1
    run_example(points1, k1, s, example_number=1)
    
    # Example 2:
    # A second set of non-dominated points, sorted by the first coordinate ascending
    # and the second coordinate descending.
    points2 = [
        (2, 20),   # P1
        (4, 18),   # P2
        (6, 16),   # P3
        (9, 12),   # P4
        (11, 8),   # P5
        (14, 5),   # P6
        (17, 3)    # P7
    ]
    k2 = 3
    run_example(points2, k2, s, example_number=2)

if __name__ == '__main__':
    main()
