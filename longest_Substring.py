 def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen={}
        l=0
        max_length=0

        for r, char in enumerate(s):

            if char in last_seen and last_seen[char]>=l:
                l=last_seen[char]+1

            last_seen[char]=r
            
            if r-l+1 > max_length:
                max_length=r-l+1

        return max_length      
        