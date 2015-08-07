import math
import string


def radix_integer(lst):
    exp = int(math.log10(max(lst) + 1))
    for i in range(exp):
        buckets = [[]] * 10
        for x in lst:
            buckets[x % 10 ** (i + 1) // 10 ** i].append(x)
        result = reduce(lambda x, y: x + y, buckets)
    return result


def radix_string(lst):
    max_string = max([len(x) for x in lst])
    ordinal = dict(zip(string.printable, range(1, len(string.printable) + 1)))
    ordinal[''] = 0
    for i in max_string:
        buckets = [[]] * len(ordinal)
        for item in lst:
            c = item[i: i + 1]
            buckets[ordinal[c]].append(item)
        result = reduce(lambda x, y: x + y, buckets)
    return result
