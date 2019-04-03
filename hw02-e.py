import numpy as np
def findPeak(array):
    low=0
    high= len(array)-1
    length = len(array)-1
    if array[low] > array[low+1]:
        print("Peak is in the lower corner: %d"%array[low])
    elif array[high] > array[high-1]:
        print("Peak is in the upper corner: %d"%array[high])
    elif np.count_nonzero(array == array[0]) == len(array):
        print("All the elements are the same, peak is:%d" %array[0])
    elif(all(array[i] <= array[i+1] for i in range(len(array)-1))):
        print("Array is sorted, peak is: %d"%array[high])
    elif(all(array[i] <= array[i-1] for i in range(len(array)-1,0,-1))):
        print("Array is sorted, peak is: %d" %darray[low])  
    else:
        while True:
            mid = (high+low)//2
            if mid > 0 and array[mid] < array[mid-1]:
                high = mid
            elif mid < length and array[mid] < array[mid+1]:
                low = mid
            else: 
                print("The peak is:%d "%array[mid])
                break
            
filename_1 = open(raw_input("Insert the text file:"),'r')
lines = filename_1.readlines()
for line in lines:
   array = np.fromstring(line,dtype=int,sep=',')
filename_1.close()
findPeak(array)
