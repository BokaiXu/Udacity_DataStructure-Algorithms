#### Explanation:
If we can get the function to put the `0`s and `2`s in the correct positions, this will aotumatically cause the `1`s to be in the correct positions as well.We need two pointers to keep track of the position of the last 0 and the first 2. Then traverse the array, if the value is 0 or 2, we exchange the value with the last 0 or first 2. Then move the pointers. If the value is 1, we do nothing and keep traversing the array. 
#### Time complexity:
Since we only do one traverse, the time complexity is O(n). 
#### Space complexity:
The space complexity is O(1) since there is no extra space used.