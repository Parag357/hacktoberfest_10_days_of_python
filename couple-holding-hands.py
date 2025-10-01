# There are n couples sitting in 2n seats arranged in a row and want to hold hands.

# The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat. The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2n - 2, 2n - 1).

# Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        result=0
        dic={ v:k for k,v in enumerate(row) }
        for i in range(0, len(row), 2):
            parity=row[i] % 2
            target_ele= row[i]+1 if parity == 0 else row[i]-1
            if row[i+1] == target_ele: continue
            nex=row[i+1]
            target_idx=dic[target_ele]
            row[i+1]=row[target_idx]
            row[target_idx]=nex
            dic[nex]=target_idx
            result+=1
        return result
