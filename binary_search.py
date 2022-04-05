def binarySearch(searchList, target):
    lowIdx = -1
    highIdx = len(searchList)
    while highIdx - lowIdx > 1:
        midIdx = lowIdx + (highIdx - lowIdx) // 2
        current = searchList[midIdx]
        if target == current: return midIdx
        elif target < current: highIdx = midIdx
        else: lowIdx = midIdx
    return -1