

def insertion_sort(lst):
    for i, item in enumerate(lst[1:], start=1):
        j = i
        while j > 0 and lst[j - 1] > item:
            lst[j] = lst[j - 1]
            j = j - 1
        lst[j] = item