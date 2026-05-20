class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        stack = []
        third = float('-inf')

        for i in range(len(nums) - 1, -1, -1):

            # nums[i] becomes '1'
            if nums[i] < third:
                return True

            # finding possible '2'
            while stack and nums[i] > stack[-1]:
                third = stack.pop()

            # possible '3'
            stack.append(nums[i])

        return False