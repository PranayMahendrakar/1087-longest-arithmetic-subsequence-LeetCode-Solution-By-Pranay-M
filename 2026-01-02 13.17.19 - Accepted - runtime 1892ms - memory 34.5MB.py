class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        # dp[i][diff] = length of longest arithmetic subsequence ending at i with difference diff
        dp = [{} for _ in range(n)]
        result = 2
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                # If j already has a sequence with this diff, extend it
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                result = max(result, dp[i][diff])
        
        return result