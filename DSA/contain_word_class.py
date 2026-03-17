class ContainWord:

    def solution(self,source,target):
    
        present = True
    
        for ch in target:
        
            if ch not in source:

                present = False

                break

        return present
    
cnw_inst = ContainWord()
print(cnw_inst.solution("traviduxtechnology","vridautx"))