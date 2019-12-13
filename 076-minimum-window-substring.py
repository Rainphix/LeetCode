import collections
class Solution:
    # def minWindow(self, s: str, t: str) -> str:
    #     # Time Limited
    #     t_dict = collections.Counter(t)
    #     s_dict = collections.Counter(s)
    #
    #     left, right = 0, 0
    #
    #     if self.judgement(s_dict, t_dict) == False:
    #         return ""
    #
    #     minString = [float("inf"), 0, 0]
    #
    #     while(right < len(s)+1):
    #         print(str(left) + " " + str(right))
    #         cur_dict = collections.Counter(s[left: right])
    #         if self.judgement(cur_dict, t_dict) == False:
    #             right += 1
    #         else:
    #             if right - left < minString[0]:
    #                 minString = [right-left, left, right]
    #             while(self.judgement(cur_dict, t_dict) and left < right):
    #                 left += 1
    #                 print("change the left!")
    #                 cur_dict = collections.Counter(s[left: right])
    #                 if right - left < minString[0]:
    #                     minString = [right - left, left, right]
    #
    #     print(minString)
    #     return s[minString[1]-1: minString[2]]
    #
    # def judgement(self, s_dict, t_dict):
    #     for i in t_dict.keys():
    #         try:
    #             if t_dict.get(i) > s_dict.get(i):
    #                 return False
    #         except:
    #             return False
    #     return True

    # def minWindow(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: str
    #     """
    #
    #     if not t or not s:
    #         return ""
    #
    #     # Dictionary which keeps a count of all the unique characters in t.
    #     dict_t = Counter(t)
    #
    #     # Number of unique characters in t, which need to be present in the desired window.
    #     required = len(dict_t)
    #
    #     # left and right pointer
    #     l, r = 0, 0
    #
    #     # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
    #     # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
    #     formed = 0
    #
    #     # Dictionary which keeps a count of all the unique characters in the current window.
    #     window_counts = {}
    #
    #     # ans tuple of the form (window length, left, right)
    #     ans = float("inf"), None, None
    #
    #     while r < len(s):
    #
    #         # Add one character from the right to the window
    #         character = s[r]
    #         window_counts[character] = window_counts.get(character, 0) + 1
    #
    #         # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
    #         if character in dict_t and window_counts[character] == dict_t[character]:
    #             formed += 1
    #
    #         # Try and co***act the window till the point where it ceases to be 'desirable'.
    #         while l <= r and formed == required:
    #             character = s[l]
    #
    #             # Save the smallest window until now.
    #             if r - l + 1 < ans[0]:
    #                 ans = (r - l + 1, l, r)
    #
    #             # The character at the position pointed by the `left` pointer is no longer a part of the window.
    #             window_counts[character] -= 1
    #             if character in dict_t and window_counts[character] < dict_t[character]:
    #                 formed -= 1
    #
    #             # Move the left pointer ahead, this would help to look for a new window.
    #             l += 1
    #
    #             # Keep expanding the window once we are done co***acting.
    #         r += 1
    #     return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

    def minWindow(self, s: str, t: str) -> str:

        s_dict = collections.Counter(s)
        t_dict = collections.Counter(t)

        if self.judgement(s_dict, t_dict) == False:
            return ""

        left, right = 0, 0

        required = len(t_dict)
        formed = 0

        windows_count = {}

        ans = float("inf"), 0, 0

        while(right < len(s)):

            letter = s[right]
            windows_count[letter] = windows_count.get(letter, 0) + 1

            if letter in t_dict and windows_count[letter] == t_dict[letter]:
                formed += 1

            while left <= right and formed == required:

                letter = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right-left+1, left, right)

                windows_count[letter] -= 1

                if letter in t_dict and windows_count[letter] < t_dict[letter]:
                    formed -= 1

                left += 1
            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

    def judgement(self, s_dict, t_dict):
        for i in t_dict.keys():
            try:
                if t_dict.get(i) > s_dict.get(i):
                    return False
            except:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    print(s.minWindow(S,T))