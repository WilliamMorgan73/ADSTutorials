import random

def partition(A, left, right, pivotIndex):
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[right] = A[right], A[pivotIndex]  # Move pivot to end
    storeIndex = left
    for i in range(left, right):
        if A[i] < pivotValue:
            A[storeIndex], A[i] = A[i], A[storeIndex]
            storeIndex += 1
    A[right], A[storeIndex] = A[storeIndex], A[right]  # Move pivot to its final place
    return storeIndex

def randomiseQuickSelect(A, i, left, right):
    """Returns the ith smallest element of A

    Args:
        A (Array): Array of integers
        i (Integer): Index of the element to be found
        left (Integer): Left index of the array
        right (Integer): Right index of the array
    """

    #Base case - if the list has only one element, return it
    if left == right:
        return A[left]

    # Choose a random pivotIndex between left and right
    pivotIndex = random.randint(left, right)

    # Get the index where the pivot is in sorted position
    pivotIndex = partition(A, left, right, pivotIndex)

    # The pivot is in its sorted position, so pivotIndex = i
    if i == pivotIndex:
        return A[pivotIndex]
    # If i is less than the pivot index
    elif i < pivotIndex:
        return randomiseQuickSelect(A, i, left, pivotIndex - 1)
    else:
        # If i is more than the pivot index
        return randomiseQuickSelect(A, i, pivotIndex + 1, right)
    
    
for i in range(10):
    A = random.sample(range(50000), 50000)
    random.shuffle(A)
    i = random.randint(0, len(A)-1)
    x = randomiseQuickSelect(A, i, 0, len(A)-1)
    if x == i:
        print('i=%d OK' % i)
    else:
        print('i=%d something is wrong' % i)