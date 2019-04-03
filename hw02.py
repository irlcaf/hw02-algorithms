import numpy as np
def findPeak(array,low,high,length):
    if length == 0:
        return False
    else:
        if array[low] > array[low+1]:
            return low
        elif array[high] > array[high-1]:
            return high
        else:
            mid = low + (high-low)/2
            mid = int(mid)
            if(mid != 0 and mid != length-1 and(mid==0 or array[mid-1] <= array[mid]) and (mid == length-1 or array[mid+1] <= array[mid])):
                return mid
            elif (mid > 0 and array[mid-1] > array[mid]):
                return findPeak(np.split(array,low,mid-1),low,(mid-1),length)
            else:
                return findPeak(np.split(array,mid+1,high),(mid+1),high,length)

filename_1 = open(raw_input("Insert the text file:"),'r')
lines = filename_1.readlines()
for line in lines:
    array = np.fromstring(line,dtype=int,sep=',')
filename_1.close()
length = len(array)
print("The peak point is: %d"%array[findPeak(array,0,length-1,length)])

