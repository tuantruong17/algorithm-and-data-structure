# solution for leetcode problem https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        lookup = [None, None, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []
        def helper(current):
            print(current)
            if len(current) == len(digits):
                result.append(current)
                return
            digit = digits[len(current)]
            for letter in lookup[int(digit)]:
                helper(current + letter)
        helper("")
        return result
        