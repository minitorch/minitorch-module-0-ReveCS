import math
import random
from dataclasses import dataclass
from typing import List, Tuple


def make_pts(N):
    """
    Generates a list of N random points in the unit square [0, 1] x [0, 1].

    Args:
        N (int): The number of points to generate.

    Returns:
        List[Tuple[float, float]]: A list of N random points in the unit square.
    """
    X = []
    for i in range(N):
        x_1 = random.random()
        x_2 = random.random()
        X.append((x_1, x_2))
    return X


@dataclass
class Graph:
    N: int
    X: List[Tuple[float, float]]
    y: List[int]


def simple(N):
    """
    Generates a simple dataset with N points in the unit square [0, 1] x [0, 1].
    The points are classified as 1 if they are in the left half of the square (x < 0.5) and 0 otherwise.

    Args:
        N (int): The number of points to generate.

    Returns:
        Graph: A Graph object containing the generated points and their labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def diag(N):
    """
    Generates a diagonal dataset with N points in the unit square [0, 1] x [0, 1].
    The points are classified as 1 if they are below the line y = x (x + y < 0.5) and 0 otherwise.

    Args:
        N (int): The number of points to generate.

    Returns:
        Graph: A Graph object containing the generated points and their labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 + x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def split(N):
    """
    Generates a split dataset with N points in the unit square [0, 1] x [0, 1].
    The points are classified as 1 if they are in the left or right half of the square (x < 0.2 or x > 0.8) and 0 otherwise.

    Args:
        N (int): The number of points to generate.

    Returns:
        Graph: A Graph object containing the generated points and their labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.2 or x_1 > 0.8 else 0
        y.append(y1)
    return Graph(N, X, y)


def xor(N):
    """
    Generates an XOR dataset with N points in the unit square [0, 1] x [0, 1].
    The points are classified as 1 if they are in the top left or bottom right quadrants (x < 0.5 and y > 0.5 or x > 0.5 and y < 0.5) and 0 otherwise.

    Args:
        N (int): The number of points to generate.

    Returns:
        Graph: A Graph object containing the generated points and their labels.
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 and x_2 > 0.5 or x_1 > 0.5 and x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def circle(N):  
    """
    Generates a circle dataset with N points in the unit square [0, 1] x [0, 1].
    The points are classified as 1 if they are outside the circle centered at (0.5, 0.5) with radius 0.1 and 0 otherwise.

    Args:
        N (int): The number of points to generate.

    Returns:
        Graph: A Graph object containing the generated points and their labels.
    """
    for x_1, x_2 in X:
        x1, x2 = x_1 - 0.5, x_2 - 0.5
        y1 = 1 if x1 * x1 + x2 * x2 > 0.1 else 0
        y.append(y1)
    return Graph(N, X, y)


def spiral(N):
    """
    Generates a spiral dataset with N points in the unit square [0, 1] x [0, 1].
    The points are classified as 1 if they are in the top left or bottom right quadrants (x < 0.5 and y > 0.5 or x > 0.5 and y < 0.5) and 0 otherwise.

    Args:
        N (int): The number of points to generate.

    Returns:
        Graph: A Graph object containing the generated points and their labels.
    """
    def x(t):
        return t * math.cos(t) / 20.0

    def y(t):
        return t * math.sin(t) / 20.0
    X = [(x(10.0 * (float(i) / (N // 2))) + 0.5, y(10.0 * (float(i) / (N //
        2))) + 0.5) for i in range(5 + 0, 5 + N // 2)]
    X = X + [(y(-10.0 * (float(i) / (N // 2))) + 0.5, x(-10.0 * (float(i) /
        (N // 2))) + 0.5) for i in range(5 + 0, 5 + N // 2)]
    y2 = [0] * (N // 2) + [1] * (N // 2)
    return Graph(N, X, y2)


datasets = {'Simple': simple, 'Diag': diag, 'Split': split, 'Xor': xor,
    'Circle': circle, 'Spiral': spiral}
