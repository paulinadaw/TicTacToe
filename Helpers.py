from itertools import groupby


def all_equal(iterable):
    """Returns True if all the elements are equal to each other"""
    # https://docs.python.org/3/library/itertools.html#itertools-recipes
    g = groupby(iterable)
    return next(g, True) and not next(g, False)
