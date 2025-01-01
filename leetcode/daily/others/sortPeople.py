from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hash_people = {}
        for index in range(len(names)):
            hash_people[heights[index]] = names[index]

        hash_people = dict(sorted(hash_people.items(), reverse=True))

        heights = list(hash_people.keys())
        names = list(hash_people.values())

        return names
    
Solution().sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170])