class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ans = []
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        for word in words:
            code = ""
            for char in word:
                code += codes[(ord(char)) - ord('a')]
            ans.append(code)
            
        return len(set(ans))