class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # An Anagram is a word or phrase formed by rearranging the letters
        # of a different word or phrase, typically using all the original
        # letters exactly once.

        if len(t) == len(s):
            # dict keeping track of all words
            letter_and_their_counts = {}

            # adding each character and its count
            for char in s:
                if char in letter_and_their_counts:
                    letter_and_their_counts[char] += 1
                else:
                    letter_and_their_counts[char] = 1

            # removing each character and its count
            # deleting if count is 0

            for char in t:
                if char in letter_and_their_counts:
                    letter_and_their_counts[char] -= 1
                    if letter_and_their_counts[char] == 0:
                        del letter_and_their_counts[char]

            # if dictionary is empty, all character with the counts were found
            # from t in s
            if len(letter_and_their_counts) == 0:
                return True

        return False


solution = Solution()
print(solution.isAnagram("a", "ab"))
