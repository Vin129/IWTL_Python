# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
# 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# https://leetcode-cn.com/problems/merge-intervals/solution/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

