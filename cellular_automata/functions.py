import itertools


def compose(f, *functions):
    if not functions:
        return f
    else:
        return lambda x: compose(*functions)(f(x))


def _test_compose():
    a = lambda x: x + 3
    b = lambda x: x * 3
    c = lambda x: x * x
    assert compose(a, b, c)(1) == c(b(a(1)))


def flatten(iterable):
    return itertools.chain.from_iterable(iterable)


def _test_flatten():
    nested = [[1, 2, 3], [4], [5, 6, 7], [8], [[9]]]
    flattened = [1, 2, 3, 4, 5, 6, 7, 8, [9]]
    assert list(flatten(nested)) == flattened


if __name__ == "__main__":
    _test_compose()
    _test_flatten()
