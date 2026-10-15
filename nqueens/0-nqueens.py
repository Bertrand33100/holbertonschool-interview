#!/usr/bin/python3
"""Solves the N Queens problem."""
import sys


def solve(n):
    """Find all solutions for placing n queens on an n×n board."""
    solutions = []
    queens = []

    def is_safe(row, col):
        for r, c in enumerate(queens):
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append([[r, c] for r, c in enumerate(queens)])
            return
        for col in range(n):
            if is_safe(row, col):
                queens.append(col)
                backtrack(row + 1)
                queens.pop()

    backtrack(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for solution in solve(n):
        print(solution)
