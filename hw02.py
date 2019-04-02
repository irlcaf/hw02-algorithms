import numpy as np

def findPeak(array,low,high,length):
    mid = low + (high-low)/2
    mid = int(mid)

    if((mid==0 or array[mid-1] <= array[mid]) and (mid == length-1 or array[mid+1] <= array[mid])):
        return mid
    elif array[low] >= array[low+1]:
        return low
    elif array[high] >= array[high-1]:
        return high
    elif (mid > 0 and array[mid-1] > array[mid]):
        return findPeak(array,low,(mid-1),length)
    else:
        return findPeak(array,(mid+1),high,length)

filename_1 = open(raw_input("Please enter the file name with the array of integers:"),'r')
lines = filename_1.readlines()
for line in lines:
    array = np.fromstring(line,dtype=int,sep=",")
filename_1.close()
print(array)
length = len(array)

print("The peak point is: ",array[findPeak(array,0,length-1,length)])
