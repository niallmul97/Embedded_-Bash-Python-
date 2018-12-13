def selectionSort(alist):
    for i in range(len(alist)):

        # Find the minimum element in remaining
        minPosition = i

        for j in range(i + 1, len(alist)):
            if alist[minPosition] > alist[j]:
                minPosition = j

        # Swap the found minimum element with minPosition
        temp = alist[i]
        alist[i] = alist[minPosition]
        alist[minPosition] = temp

    return alist


print(selectionSort([5, 2, 1, 9, 0, 4, 6]))