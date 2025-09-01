
#  N metting in one room 
from typing import List
class meeting:
    def __init__(self, start,end,pos):
        self.start = start
        self.end = end
        self.pos = pos


class Solution:
    def maxmeeting(self, s,e , n):
        meet = [meeting(s[i], e[i] ,i+1) for i in range(n)]
        sorted(meet , key = lambda x: (x.end , x.pos))
        answer = []
        limit = meet[0].end
        answer.append(meet[0].pos)
        for i in range(1,n):
            if meet[i].start > limit:
                limit = meet[i].end
                answer.append(meet[i].pos)
        for i in answer:
            print(i)


if __name__ =="__main__":
    obj = Solution()
    n = 6
    start = list(map(int,input().split()))
    end = list(map(int, input().split()))
    obj.maxmeeting(start , end ,n)
