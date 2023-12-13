class Solution:
    def rotate(self, nums: List[int], k: int) -> None:


        if(len(nums) <= 1):
            return nums
        while(k > len(nums)):
            k = k - len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums

