class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hash set length
        return len(nums)!=len(set(nums))

# Complexity
# Space complexity usually refers to additional memory exclud input
# for this problem, the complexity is dominated by set(nums)
# - Time: O(n)
# - Space: O(n)