import codon_usage
import operator
#seq = raw_input("enter a file: ")
 #takes in sequence file
 #returns min and max codons with freq/1000 in that sequence elijjgalgsdsdga
#f = open(seq).readlines()
def actual_count(seq):
    #seq = raw_input("enter a file: ")
    #f = open(seq).readlines()
    #x = []
    from codon_objects import fun
    t = fun(seq)
    #print(t.dict)
    #print(t.list)
    codon_dict = t.dict
    #print codon_dict
    #codon_dict = codon_usage.usage_calc(f,x)
    total = 0
    for key in codon_dict:
        total+=codon_dict[key]
    #print total

    for x,y in codon_dict.items():
        codon_dict[x] = (float(y)/total)*1000

    #print codon_dict
    return codon_dict
'''from codon_objects import fun
t = fun()
print t.dict
print t.list'''


#print actual_count()
#x = actual_count(f)
#print x
