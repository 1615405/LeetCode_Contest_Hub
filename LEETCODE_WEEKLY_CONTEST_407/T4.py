class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        def minOperationsToZero(nums: List[int]) -> int:
            """
            计算将给定的整数数组 nums 通过一系列的加一或减一操作转换成全零数组所需的最小操作次数。
            操作定义为在任意连续子数组上进行的统一加一或减一。
            """
            pos, neg = max(0, nums[0]), min(0, nums[0])
            for i in range(1, len(nums)):
                diff = nums[i] - nums[i - 1]
                if diff > 0:
                    pos += diff
                elif diff < 0:
                    neg += diff
            return max(pos, -neg)
        changes = [num - tar for (num, tar) in zip(nums, target)]
        return minOperationsToZero(changes)
