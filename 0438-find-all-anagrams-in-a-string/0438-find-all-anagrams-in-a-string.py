from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        res = []

        pMap = Counter(p)
        sMap = Counter()
        left = 0

        # sliding window - iterate through
        for right in range(len(s)):

#         6. Add current character to window frequency map
#    - window_map[s[right]] += 1
            sMap[s[right]] += 1

# 7. Check if window is too big
#    - If (right - left + 1) > pattern_length:
#      a. Remove leftmost character from window map
#         - window_map[s[left]] -= 1
#         - If count becomes 0, delete the key
#      b. Move left pointer right: left += 1
            if (right - left + 1) > len(p):
                sMap[s[left]] -= 1
                if sMap[s[left]] == 0:
                    del sMap[s[left]]
                left += 1

        # 8. Check if current window matches pattern
        #    - If window_map == pattern_map:
        #      a. Add left pointer to result list
            if sMap == pMap:
                res.append(left)

        return res

        