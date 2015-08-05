
def quick(lst):
    if len(lst) < 1:
        return lst
    pivot = lst[0]
    left = [x for x in lst[1:] if x <= pivot]
    right = [x for x in lst[1:] if x > pivot]
    left_sort = quick(left)
    right_sort = quick(right)
    return left_sort + pivot + right_sort