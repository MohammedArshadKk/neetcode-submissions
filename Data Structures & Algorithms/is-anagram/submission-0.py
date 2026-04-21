class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print()
        if len(s) != len(t):
            return False
        hashTable={}
        for char in s:
            hashTable[char]= hashTable.get(char,0)+1
        for char in t:
            if char not in hashTable:
                return False
            hashTable[char]= hashTable[char] - 1
            if hashTable[char]<0:
                return False

        return True    