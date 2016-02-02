from difflib import SequenceMatcher

__author__ = 'sekely'


def num_format(number):
    return number.replace('-', '').replace(' ', '').replace('_', '')


def is_in_row(row, string):
    if not isinstance(row, dict):
        raise TypeError("row should be in dict format")
    if string.lower() in [v.lower() for v in row.values()]:
        return True
    return False


def _similar(s1, s2):
    return SequenceMatcher(None, s1, s2).ratio()


def is_similar(row, string, ratio=0.8):
    if not isinstance(row, dict):
        raise TypeError("row should be in dict format")
    similarities = [_similar(string, val) for val in row.values()]
    return any([r >= ratio for r in similarities])
