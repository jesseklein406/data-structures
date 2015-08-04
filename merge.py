

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]

    sort_left = merge_sort(left)
    sort_right = merge_sort(right)

    return merge(sort_left, sort_right)


def merge(left, right):
    sort = []
    l_index = 0
    r_index = 0
    while l_index < len(left) and r_index() < len(right):
        if left[l_index] <= right[r_index]:
            sort.append(left[l_index])
            l_index += 1
        else:
            sort.append(right[r_index])
            r_index += 1

    if l_index < len(left):
        sort.extend(left[l_index:])
    else:
        sort.extend(right[r_index:])

    return sort
