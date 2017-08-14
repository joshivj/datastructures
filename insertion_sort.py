# insertion_sort

def insertion_sort(arr):
    
    # For every index in array
    for i in range(1,len(arr)):
        # Set current values and position
        currentvalue = arr[i]
        position = i
        
        # Sorted Sublist
        while position>0 and arr[position-1]>currentvalue:
            
            arr[position]=arr[position-1]
            position = position-1

        arr[position]=currentvalue

arr = [4,1,7,3,5]
insertion_sort(arr)
print arr