class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        SampleSet = set()
        
        for j in emails:
            first, last = j.split("@")
            drift = ""
            
            for i in first:
                if i== ".":
                    continue

                if i =="+":
                    break
                
                drift += i

            SampleSet.add(drift+ "@" + last)

        return len(SampleSet)
        
