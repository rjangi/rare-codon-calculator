# A Python program to to return multiple
# values from a method using class
class CodonLists():

    def __init__(self, seq):

        from codon_usage import usage_calc
        codon_list = []
        #seq = raw_input()
        f = open(seq).readlines()
        codon_dict = usage_calc(f, codon_list)
        values = list(codon_dict.values())
        self.dict = codon_dict
        self.list = codon_list
        #self.list2 = values

def fun(seq):

    return CodonLists(seq)


# Driver code to test above method
#t = fun()
#print(t.dict)
#print(t.list)