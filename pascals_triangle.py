from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1] * (i + 1) for i in range(numRows)]   # "1" is the first one

        for i in range(2, numRows):   # Starts from 2 cuz of 1 and i is row and j is column. 
            for j in range(1, i):     # Diagonal column is the same column
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

        return pascal