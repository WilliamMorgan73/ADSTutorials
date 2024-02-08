import random

def median_of_medians (A,i):

    if len(A) <= 5:
        A.sort()
        return A[i]
    else:
        partitions = []
        # divide A into sublists of len 5
        for j in range (0, len(A)-1, 5):
            #Check if the last partition has less than 5 elements
            if j+5 > (len(A)-1):
                partitions.append(A[j:])
            else:
                partitions.append(A[j:j+5])
        
        #Find the median of each partition
        medians = []
        for k in partitions:
            medians.append(median_of_medians(k, len(k)//2))
            
        #Find the median of medians
        mom = median_of_medians(medians, len(medians)//2)
        
        #Partition the list around the median of medians
        left = [j for j in A if j < mom]
        
        right = [j for j in A if j > mom]
    
        #Find the index of the median of medians
        j = len(left)
        
        #If the index of the median of medians is the same as the index we are looking for, return the median of medians
        if i == j:
            return mom
        #If the index of the median of medians is less than the index we are looking for, find the median of the right partition
        elif i > j:
            return median_of_medians(right, i-j-1)
        #If the index of the median of medians is greater than the index we are looking for, find the median of the left partition
        else:
            return median_of_medians(left, i)
        
            
            
        
for i in range(10):
    A = random.sample(range(50000), 50000)
    random.shuffle(A)
    i = random.randint(0, len(A)-1)
    x = median_of_medians(A, i)
    if x == i:
        print('i=%d OK' % i)
    else:
        print('i=%d something is wrong' % i)