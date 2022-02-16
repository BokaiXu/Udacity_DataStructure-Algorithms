#### Explanation:    
The array contains two sorted array. If I can find the pivot index, I can search value in the two sorted arrays with O(log(n)) time complexity. For the function that look for the pivot index, I can use binary search. Every time compare the value of middle index and the start index. The pivot value is either in the same side of the first value or in the opposite side of the first value. This function is also O(log(n)) time complexity. 
#### Time complexity:
O(log(n))
#### Space complexity:
O(log(n))