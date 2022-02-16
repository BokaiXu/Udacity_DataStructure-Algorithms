Since the group class has group and user, to figure out whether a user is in a group is to write a recursive fuction.
If a user is in the group, return True. If a user is not in the group and there is no group in the group, return False.
Else recursively call the function to check the group of group.

For this recursion, the time complexity should be O(depth of the recursion).
The space complexity should be O(1) since we did not use extra memory other than the input.