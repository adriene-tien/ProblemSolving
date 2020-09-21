# LeetCode Easy 
# Reorder Data In Log Files Question 
# String

class Solution:

    # currently not all test cases pass, need to deal with alphanumeric identifiers not being unique 
    # coming back later lol 
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if len(logs) == 0: 
            return []

        ret = []
        letterLogsTracker = {}
        
        for i in range(0, len(logs)): 
            check = logs[i].split()
            if not check[1].isdigit(): 
                    letterLogsTracker[check[0]] = " ".join(check[1:])
            else: 
                ret.append(logs[i])
        
        print(letterLogsTracker)
                
        result = sorted(sorted(letterLogsTracker), key=letterLogsTracker.get)
        result.reverse()
        
        for i in range(0, len(result)): 
            ret.insert(0, " ".join([result[i], letterLogsTracker[result[i]]]))
            
        return ret