def heapify(arr):
    # Root is at index 0 in array.
    # Left child of i-th node is at (2*i + 1)th index.
    # Right child of i-th node is at (2*i + 2)th index.
    # Parent of i-th node is at (i-1)/2 index.
        
    for i in range(0, len(arr)):
            
        # Check if current node is a leaf
            
        if (2*i + 1) >= len(arr) or (2*i +2) >= len(arr):
            break
            
        # Check if left child is greater than current node
        if arr[(2*i + 1)] > arr[i]:
            # Check if right child is greater than left child
            if arr[2*i + 2] > arr[2*i + 1]:
                # Swap current node with right child
                arr[i], arr[2*i + 2] = arr[2*i + 2], arr[i]
            else:
                # Swap current node with left child
                arr[i], arr[2*i + 1] = arr[2*i + 1], arr[i]
                    
    return arr

def heapSort(arr):
        
    result = []
        
    while len(arr) >= 2:
        #Heapify arr
        arr = heapify(arr)
        # Swap the last and first index
        arr[0], arr[-1] = arr[-1], arr[0]
        # Remove the last index
        result.append(arr.pop())
        
    # Handle the case when the length of arr is 1
    if arr:
        result.append(arr[0])
        
    
    # Return result
        
    return result
