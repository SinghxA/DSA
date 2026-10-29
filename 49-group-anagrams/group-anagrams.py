
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        same = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in same:
                same[key] = [word]
            else:
                same[key].append(word)

        return list(same.values())
