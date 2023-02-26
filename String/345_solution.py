class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        lst = [ch for ch in s]
        reverse = []

        for i in range(len(lst)):
            if lst[i] in vowels:
                reverse.append(lst[i])
                lst[i] = 'nl'
        
        for i in range(len(lst)):
            if lst[i] == 'nl':
                lst[i] = reverse.pop()
        
        return ''.join(lst)
