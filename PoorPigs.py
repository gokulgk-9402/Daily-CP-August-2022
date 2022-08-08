class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        
        per_feed = log2(buckets)
        allowed_feeds = ceil(minutesToTest/minutesToDie)
        
        if allowed_feeds == 1:
            return ceil(per_feed)
        
        return ceil(per_feed / log2(allowed_feeds+1))