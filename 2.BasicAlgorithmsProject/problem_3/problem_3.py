def merge_sort(arr):
    """
    This function sort the array.
    """
    if len(arr)<=1:
        return arr
    left=0
    right=len(arr)
    middle=(left+right)//2
    left_array=merge_sort(arr[left:middle])
    right_array=merge_sort(arr[middle:right])
    return merge(left_array,right_array)

def merge(left_array,right_array):
    """
    This function merge and sort two sorted array together.
    """
    result=[]
    left_index=0
    right_index=0
    while left_index<len(left_array) and right_index<len(right_array):
        if left_array[left_index]>right_array[right_index]:
            result.append(left_array[left_index])
            left_index+=1
        else:
            result.append(right_array[right_index])
            right_index+=1
    if left_index<len(left_array):
        result+=left_array[left_index:]
    if right_index<len(right_array):
        result+=right_array[right_index:]
    return result

def rearrange(arr):
    """
    This function call the merge_sort() function and return the result of this question.
    """
    if len(arr)==0:
        return 'Array is empty!'
    if len(arr)==1:
        return arr
    result=[]
    str1=''
    str2=''
    sorted_array=merge_sort(arr)
    for index, value in enumerate(sorted_array):
        if index%2==0:
            str1+=str(value)
        else:
            str2+=str(value)
    result.append(int(str1))
    result.append(int(str2))
    return result

#Test
print(rearrange([1,3,4,2,5])) # Should return [531, 42]
print(rearrange([0,3,4,6,4])) # Should return [640, 43]
print(rearrange([3,5,2,6,3,6,3,5])) # Should return [6533, 6532]
print(rearrange([1])) # Should return [1]
print(rearrange([])) # Should return Array is empty!
