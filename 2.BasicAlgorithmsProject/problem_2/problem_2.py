def find_pivot_index(arr,left,right):
    """
    This function finds the pivot index of the rotated sorted array.
    input: arr-rotated sorted arry, left-first index of the array, right-last index of the array.
    output: The index of the pivot.
    """
    if left>=right:
        return -1
    middle=(left+right)//2
    if arr[middle]>arr[middle+1]:
    # arr[middle] is the maximum
        return middle+1
    elif arr[middle]<arr[middle-1]:
    # arr[middle] is the minimum
        return middle
    elif arr[left]>arr[middle]:
    # pivot is in the left part
        return find_pivot_index(arr,left,middle-1)
    else:
    # pivot is in the right part
        return find_pivot_index(arr,middle+1,right)

def find_value_recursion(arr,left,right,target):
    """
    This function finds the target value in the sorted array.
    input: arr-sorted array, left-first index of the array, right-last index of the array, target-the target value.
    output: The index of the target value, if not exists return -1.
    """
    middle=(left+right)//2
    if arr[middle]==target:
        return middle
    if left>=right:
        return -1
    elif arr[middle]>target:
    # target is in the left part of the sorted array
        return find_value_recursion(arr,left,middle-1,target)
    else:
    # target is in the right part of the sorted array
        return find_value_recursion(arr,middle+1,right,target)

def find_value(arr,target):
    """
    This function looks for whether the target is in the array returns the index or -1.
    input: array-rotated sorted array, target-the target value needed to be found.
    output: The index of the target if found or -1 if target not exists in the array.
    """
    if len(arr)==0:
        return 'Array is empty!'
    left=0
    right=len(arr)-1
    # find the pivot index
    pivot_index=find_pivot_index(arr,left,right)
    # look for target from left sorted array
    left=find_value_recursion(arr,left,pivot_index-1,target)
    # look for target from right sorted arry
    right=find_value_recursion(arr,pivot_index,right,target)
    return max(left,right)

#Test
arr=[6,7,8,9,3,4,5]
print(find_value(arr,10)) # Should return -1

arr=[6,7,8,9,3,4,5]
print(find_value(arr,6)) # Should return 0

arr=[6,7,8,9,3,4,5]
print(find_value(arr,5)) # Should return 6

arr=[6,7,8,9,3,4,5]
print(find_value(arr,9)) # Should return 3

arr=[6,7,8,9,3,4,5]
print(find_value(arr,3)) # Should return 4

arr=[6,7,8,9,3,4,5]
print(find_value(arr,7)) # Should return 1

arr=[]
print(find_value(arr,7)) # Should return Array is empty!

arr=[1,2,3,4,5]
print(find_value(arr,3)) # Should return 2