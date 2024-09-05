"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def mul(x:float, y:float) -> float:
    """
    Multiplies two floating-point numbers.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The product of x and y.
    """
    return x * y

def id(x:float) -> float:
    """
    Returns the input value.

    Args:
        x: The input value.

    Returns:
        The input value.
    """
    return x

def add(x:float, y:float) -> float:
    """
    Adds two floating-point numbers.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The sum of x and y.
    """
    return x + y

def neg(x:float) -> float:
    """
    Negates a floating-point number.

    Args:
        x: The number to negate.

    Returns:
        The negated number.
    """
    return -x

def lt(x:float, y:float) -> bool:
    """
    Checks if one floating-point number is less than another.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        True if x is less than y, False otherwise.
    """
    return x < y

def eq(x:float, y:float) -> float:
    """
    Checks if two floating-point numbers are equal.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        True if x is equal to y, False otherwise.
    """
    return x == y

def max(x:float, y:float) -> float:
    """
    Returns the larger of two floating-point numbers.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The maximum of x and y.
    """
    return x if x > y else y

def is_close(x:float, y:float) -> bool:
    """
    Checks if two floating-point numbers are close in value.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        True if x and y are close, False otherwise.
    """
    return abs(x - y) < 1e-2

def sigmoid(x:float) -> float:
    """
    Calculates the sigmoid function of a floating-point number.

    Args:
        x: The input number.

    Returns:
        The result of the sigmoid function applied to x.
    """
    return 1.0 / (1.0 + math.exp(-x)) if x >= 0 else math.exp(x) / (1.0 + math.exp(x))

def relu(x:float) -> float:
    """
    Applies the ReLU activation function to a floating-point number.

    Args:
        x: The input number.

    Returns:
        The result of the ReLU function applied to x.
    """
    return x if x >= 0 else 0

def log(x:float) -> float:
    """
    Calculates the natural logarithm of a floating-point number.

    Args:
        x: The input number.

    Returns:
        The result of the natural logarithm applied to x.
    """
    return math.log(x)

def exp(x:float) -> float:
    """
    Calculates the exponential function of a floating-point number.

    Args:
        x: The input number.

    Returns:
        The result of the exponential function applied to x.
    """
    return math.exp(x)

def inv(x:float) -> float:
    """
    Calculates the reciprocal of a floating-point number.

    Args:
        x: The input number.

    Returns:
        The result of the reciprocal function applied to x.
    """
    return 1.0 / x

def log_back(x: float, y: float) -> float:
    """
    Computes the derivative of log times a second arg.
    
    Args:
        x: The input value.
        y: The second argument to multiply with the derivative.
    
    Returns:
        The result of the derivative of log(x) multiplied by y.
    """
    return (d(math.log(x))/dx) * y

def inv_back(x:float, y:float) -> float:
    """
    Computes the derivative of the reciprocal function times a second arg.
    
    Args:
        x: The input value.
        y: The second argument to multiply with the derivative.
    
    Returns:
        The result of the derivative of the reciprocal function applied to x.
    """
    return (-1 / x**2) * y

def relu_back(x:float, y:float) -> float:
    """
    Computes the derivative of the ReLU function times a second arg.
    
    Args:
        x: The input value.
        y: The second argument to multiply with the derivative.
    
    Returns:
        The result of the derivative of the ReLU function applied to x.
    """
    return (x > 0) * y






# ##     0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.

def map(f: Callable[[float], float], iter: Iterable[float]) -> Iterable[float]:
    """
    Applies a given function to each element of an iterable and returns a new iterable.

    Args:
        f: The function to apply to the iterable.
        iter: The iterable to map over.

    Returns:
        A new iterable with the results of applying f to each element of iter.
    """
    return [f(x) for x in iter]

def zipWith(f: Callable[[float, float], float], iter1: Iterable[float], iter2: Iterable[float]) -> Iterable[float]:
    """
    Combines elements from two iterables by applying a given function to corresponding elements and returns a new iterable.
    
    Args:
        f: The function to apply to both iterables.
        iter1: The first iterable.
        iter2: The second iterable.
    
    Returns:
        A new iterable with the results of applying f to corresponding elements of iter1 and iter2.
    """
    return [f(x, y) for x, y in zip(iter1, iter2)]

def reduce(f: Callable[[float], float], iter: Iterable[float], value: float) -> float:
    """
    Reduces an iterable to a single value by applying a given function cumulatively and returns the value.
    
    Args:
        f: The function to apply cumulatively.
        iter: The iterable to reduce.
        value: The initial value to start the reduction.
        
    Returns:
        The result of applying f cumulatively to the elements of iter.
    """
    for x in iter:
        value = f(value, x)
    return value

def negList(iter: Iterable[float]) -> Iterable[float]:
    """
    Negates each element in the input iterable.
    
    Args:
        iter: The input iterable.
    
    Returns:
        A new iterable with each element negated.
    """
    return map(neg, iter)    

def addLists(iter1: Iterable[float], iter2: Iterable[float]) -> Iterable[float]:
    """
    Adds corresponding elements from two iterables.
    
    Args:
        iter1: The first iterable.
        iter2: The second iterable.
    
    Returns:
        A new iterable with the results of adding corresponding elements of iter1 and iter2.
    """
    return zipWith(add, iter1, iter2)

def sum(iter: Iterable[float]) -> float:
    """
    Sums all elements in the input iterable.
    
    Args:
        iter: The input iterable.
    
    Returns:
        The sum of all elements in the iterable.
    """
    return reduce(add, iter, 0)

def prod(iter: Iterable[float]) -> float:
    """
    Multiplies all elements in the input iterable.
    
    Args:
        iter: The input iterable.
    
    Returns:
        The product of all elements in the iterable.
    """
    return reduce(mul, iter, 1)

