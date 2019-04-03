import numpy as np
def findPeak(array):
    low=0
    high= len(array)-1
    length = len(array)-1
    while True:
        mid = (high+low)//2
        if mid > 0 and array[mid] < array[mid-1]:
            high = mid
        elif mid < length and array[mid] < array[mid+1]:
            low = mid
        else: 
            return mid
            
filename_1 = open(raw_input("Insert the text file:"),'r')
lines = filename_1.readlines()
for line in lines:
   array = np.fromstring(line,dtype=int,sep=',')
filename_1.close()
print("The peak point is: %d"%array[findPeak(array)])
