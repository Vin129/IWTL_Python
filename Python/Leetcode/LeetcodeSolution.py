class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        num = 0
        index = 0
        d = dict()
        while(index<len(s)):
            if s[index] in d:
                index = d[s[index]]
                d.clear()
            else:
                d[s[index]] = index
            if num < len(d):
                num = len(d)
            index = index + 1
        return num

    #136
    def singleNumber(self, nums: List[int]) -> int:
        n = nums[0]
        if len(nums) == 1:
            return n
        for x in range(1,len(nums)):
            n = n^nums[x]
        return n




