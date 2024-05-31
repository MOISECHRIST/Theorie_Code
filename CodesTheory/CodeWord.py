'''
Dans ce package je vais stocker toutes les fonctions pour la manipulation des codes binaires 
Dans le cadre de la theorie des codes.s
'''
def verif_binary(bin_wordcode : str):
    BINARY=["0","1"]
    i=0
    while i<len(bin_wordcode):
       if bin_wordcode[i] not in BINARY :
           return False
       i+=1
    return True

class CodeWord :

    def __init__(self, elt:str):
        self.value=elt
        self.length=len(elt)

    def __str__(self) -> str:
        return self.value
    
    def __add__(self , otherwc):
        str1=self.value
        str2=otherwc.value
        if len(str1)==len(str2):
            str3=""
            for i in range(self.length):
                if str1[i]==str2[i]:
                    str3+="0"
                else:
                    str3+="1"
            return CodeWord(str3)
        else :
            print("addition impossible :: Les mots de codes doivent avoir la meme taille")
            exit()
    
    def __mul__(self, otherwc):
        str1=self.value
        str2=otherwc.value
        if len(str1)==len(str2):
            str3=""
            for i in range(self.length):
                str3+=str(int(str1[i])*int(str2[i]))
            return CodeWord(str3)
        else :
            print("multiplication impossible :: Les mots de codes doivent avoir la meme taille")
            exit()
    
    def __eq__(self, otherwc):
        return self.value==otherwc.value
    
    def __ne__(self, otherwc):
        return self.value!=otherwc.value
    
    def count_digit(self, digit):
        nb=0
        for i in range(self.length):
            if self.value[i]==str(digit):
                nb+=1
        return nb
    
    def add_pair_digit(self):
        nb_0=self.count_digit(0)
        nb_1=self.count_digit(1)
        
        if nb_0 % 2 != 0:
            self.value+="0"

        if nb_1 % 2 != 0:
            self.value+="1"
        
        return self

    def repeat_check(self):
        wc=self.value
        self.value+=wc+wc
        return self
    
    def poids(self):
        nb=0
        for i in range(self.length):
            if self.value[i]=="1":
                nb+=1
        return nb
    
    def distance(self, ortherwc):
        res=self+ortherwc
        return res.poids()
    
    def likely_transmited(self, received_wc, reliability):
        d=self.distance(received_wc)
        n=self.length
        return (reliability**(n-d))*((1-reliability)**d)

if __name__=="__main__":
    entry1=input("Entrer le mot de code : ")
    if verif_binary(entry1):
        wc1 = CodeWord(entry1)
    
    entry2=input("Entrer le mot de code : ")
    if verif_binary(entry2):
        wc2 = CodeWord(entry2)
    
    print(wc1.poids())
    print(wc1!=wc2)



    
    