from CodeWord import *
from math import log2

def binary(num:int):
    tmp=""
    if num<0:
        exit()
    if num<=1:
        return num
    while num//2!=1:
        tmp=str(num%2)+tmp
        num=num//2
    return str(num//2)+str(num%2)+tmp

class Code:
    def __init__(self):
        self.list=[]
        self.length=0
    
    def __str__(self):
        text="["
        if self.length>0:
            for i in range(self.length):
                elt=self.list[i]
                if i<self.length-1:
                    text+=elt.value+" "
                else:
                    text+=elt.value
            text+="]"
        return text
    
    def add_codeword(self, wc: CodeWord):
        self.list.append(wc)
        self.length+=1
    
    def information_rate(self):
        c=len(self)
        result=[]
        for i in range(self.length):
            n=self.list[i].length
            result.append((1/n)*log2(c))
        
        return result
    
    def best_codeword_transmited(self, received_wc, reliability):
        tmp=[]
        for i in range(self.length):
            tmp.append(self.list[i].likely_transmited(received_wc, reliability))
        
        result=[]
        min_val=min(tmp)
        for i in range(len(tmp)):
            if tmp[i]==min_val:
                result.append(self.list[i])
        return result
    
    def drop_codeword(self, wc: CodeWord):
        if wc in self.list:
            self.list.remove(wc)
            self.length-=1
    
    def build_matrix_distance(self):
        matrix=[]
        for i in range(self.length):
            line=[]
            for j in range(i+1):
                res=self.list[i]+self.list[j]
                line.append(res.poids())
            matrix.append(line)
        tmp=[]
        for j in range(self.length):
            for i in range(j, self.length):
                if matrix[i][j]==1:
                    tmp.append(self.list[i])
        
        return matrix  
    
    def build_all_codeword(self, length:int):
        elt=f"{0:0{length}}"
        wc=CodeWord(elt)
        self.add_codeword(wc)
        for num in range(1,(2**length)):
            tmp=binary(num)
            elt=f"{int(tmp):0{length}}"
            wc=CodeWord(elt)
            self.add_codeword(wc)
        return self

                
    
if __name__=="__main__":
    code=Code()
    code.build_all_codeword(4)
    print(code)
