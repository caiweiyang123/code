class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

if __name__ == '__main__':
    list1 = [0,1,2,0,2,6,0,7]
    s =Solution()
    s.moveZeroes(list1)