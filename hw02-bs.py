def findPeak(array,l,r):
    while l <= r:
        mid = l + r/2
        x = array[mid]
        if array[mid]>array[mid+1] and array[mid] > array[mid-1]:
            return mid
        elif array[mid] < x:
            l = mid+1
        else:
            r = mid+1

array = [2,3,4,10,40,50]
print(findPeak(array,0,len(array)-1))
