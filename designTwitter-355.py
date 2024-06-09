'''
  self.count will be used to count the number of tweets
  self.tweetMap will map userId to an array of [count, tweetId]
  the reason we have the count is so we can grab the 10 most recent ones 
  self.followMap will map userId to a set(followerId) this is easy to retrieve all, add and delete elements
  the tricky part here is to grab the 10 most recent tweets from the followers.
  to do so, we will grab the most recent tweets from everyone in the following list. then add all of them to a max Heap. Since we only want the 10 most recent ones, a heap will be very efficient. we will need the information about where the tweetID was retrieved so we can add the most recent tweet after this one. So everytime we pop from the heap, we add back the next recent tweet from the list we retrieved this tweet from.
'''

from collections import defaultdict
import heapq
from typing import List


class Twitter:
    #posts
    #posts need to have a timeline
    #follows
    def __init__(self):
        self.count = 0 #number of tweets
        self.tweetMap = defaultdict(list) #userID => list[count, tweetID]
        self.followMap = defaultdict(set) #userID => set(followerID)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 #we will use a maxHeap below so we will decrement it for 
                    #more recent posts so we don't need to worry about *-1 later

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = [] #we want the most recent tweets from the followers here
        res = []
        self.followMap[userId].add(userId) #edge case 
        for followerId in self.followMap[userId]:
            if followerId in self.tweetMap:
                tweets = self.tweetMap[followerId] 
                recentIdx = len(tweets) - 1
                count, tweetId = self.tweetMap[followerId][recentIdx]
                maxHeap.append([count, tweetId, followerId, recentIdx])
        #now the heap has the most recent tweets from all followers
        heapq.heapify(maxHeap) #python sorts by first value so the count
        while maxHeap and len(res) < 10:
            count, tweetId, followerId, recentIdx = heapq.heappop(maxHeap)
            res.append(tweetId)
            #add the next most recent tweet of the selected user back to the heap
            if recentIdx - 1 >= 0:
                count, tweetId = self.tweetMap[followerId][recentIdx - 1]
                heapq.heappush(maxHeap, [count, tweetId, followerId, recentIdx - 1])
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)