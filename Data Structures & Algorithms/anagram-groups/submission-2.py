class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for word in strs: 
            freq = [0] * 26 # address i is letter freq, value is freq count
            
            for letter in word: 
                freq[ ord(letter) - ord('a')] += 1
            answer[tuple(freq)].append(word)

        return list(answer.values())