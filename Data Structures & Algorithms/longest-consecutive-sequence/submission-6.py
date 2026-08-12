class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num=sorted(set(nums))
        count=1
        longest=0
        for i in range(len(num)-1):
            if num[i+1]==num[i]+1:
                count+=1
            else:
                longest=max(count,longest)
                count=1
        longest=max(count,longest)
        return longest
            
        
            


        