class Solution:
    def maximumCount(self, nums):
        def lowerBound(nums):
            start, end = 0, len(nums) - 1
            index = len(nums)
            while start <= end:
                mid = (start + end) // 2

                if nums[mid] < 0:
                    start = mid + 1
                else:
                    end = mid - 1
                    index = mid
            return index

        def upperBound(nums):
            start, end = 0, len(nums) - 1
            index = len(nums)

            while start <= end:
                mid = (start + end) // 2

                if nums[mid] <= 0:
                    start = mid + 1
                else:
                    end = mid - 1
                    index = mid

            return index

        positiveCount = len(nums) - upperBound(nums)
        negativeCount = lowerBound(nums)

        return max(positiveCount, negativeCount)
