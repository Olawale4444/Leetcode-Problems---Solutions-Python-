class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        newArr = s.split(" ")
        Arr2 = []
        for i in newArr:
            if len(Arr2) == k:
                break
            else:
                Arr2.append(i+" ")        
        return "".join(Arr2).strip()
