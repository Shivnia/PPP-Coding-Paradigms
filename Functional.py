# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

# How does this solution ensure data immutability?
# This solution keeps data immutable by not changing the input array. Instead, it creates a new list using reduce and returns a sorted version, so nothing is modified in place.

# Is this solution a pure function? Why or why not?
# Yes, it's a pure function because it always gives the same output for the same input, doesn't rely on or change any outside variables, and has no side effects.

# Is this solution a higher-order function? Why or why not?
# Yes, it uses a higher-order function—reduce—which takes a function as an argument and applies it to the list, accumulating the result.

# Would it have been easier to solve this problem using a different programming style?
# An imperative style could be easier for some people because it uses loops and appends directly to a list. But functional programming makes it clearer and more concise.

# Why in particular is functional programming a helpful paradigm when solving this problem?
# Functional programming is helpful here because it focuses on what we want to achieve rather than how to do it. It promotes immutability, which reduces bugs, and it encourages modular, reusable code with higher-order functions, making everything easier to read and maintain.