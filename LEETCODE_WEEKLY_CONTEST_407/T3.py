class Solution:
    def maxOperations(self, s: str) -> int:
        operations = 0
        count_1 = 0
        i = 0
        while i < len(s):
            if s[i] == '1':
                count_1 += 1
            elif s[i] == '0' and s[i - 1] != '0':
                operations += count_1
            i += 1
        return operations
