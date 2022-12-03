import functools as ft
import operator as op


def sum_iterable(iterable_input):
    return ft.reduce(op.add, iterable_input)
