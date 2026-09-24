class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate sum of first window
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Slide the window
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        
        # Must return a double/float (maximum average)
        return max_sum / k