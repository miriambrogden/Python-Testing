import os
import sys
from itertools import combinations


class BinaryString:

    binaryStrings = [] * 20
    tempStrings = [] * 20
    binaryString = [None] * 20

    # function to generate all binary strings  of lnegth 'n' and print the ones with
    # 'k' 1s in it.
    def genAllBinStrings(self, n: int, k: int, count: int):
        if count == n: 
            for i in range(0, n):
                self.binaryStrings.append(self.binaryString[i])
            value = 0
            value = self.countOnes(self.binaryStrings)
            if value == k:
                print(self.binaryStrings.copy())
                self.tempStrings.append(self.binaryStrings.copy())
            self.binaryStrings.clear()
            return
        self.binaryString[count] = '0'
        self.genAllBinStrings(n, k, count+1)
        self.binaryString[count] = '1'
        self.genAllBinStrings(n, k, count+1)        
        

    # function to genearte all substrings of parameter sting
    # function will call genAllBinStrings with 'n' being the length of string.
    # The function should print only substrings of length 'k' where 'k' is a parameter
    #passed into the function
    def genAllSubStrings(self, k: int, string: str):
        self.genAllBinStrings(len(string), k, 0)
        substring = [''.join(l) for i in range(len(string)) for l in combinations(string, i+1)]
        for i in reversed(substring):
            if (len(i) == k):
                print(i)
            

    ##count the number of ones in binString
    def countOnes(self, binString:list):
        count = 0
        for i in range(0, len(binString)):
            if binString[i] == '1':
                count += 1
        return count
