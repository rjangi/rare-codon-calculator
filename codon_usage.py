from itertools import islice
#AUGCUUGUAAGCAGCUUG
#ABCDEFGHIJKLMNO
#seq = raw_input("Enter sequence")
#seq = raw_input("enter a file: ")
#f = open(seq).readlines()


#codon_list = []
def usage_calc(f, codon_list):

    #seq = raw_input("enter a file: ")
    #f = open(seq).readlines()

    #codon_dict={'ATG':0,}
    codon_dict={'TAG':0,'AGA':0,'ACC':0, 'ATG':0, 'ACA': 0, 'AAA': 0, 'ATC': 0, 'AAC': 0, 'ATA': 0, 'AGG': 0, 'CCT': 0, 'ACT': 0, 'AGC':0, 'AAG': 0, 'CTT': 0, 'CAT': 0, 'AAT': 0, 'ATT': 0, 'CTG': 0, 'CTA': 0, 'CTC': 0, 'CAC': 0, 'ACG': 0, 'CCG': 0, 'AGT': 0, 'CAG': 0, 'CAA': 0, 'CCC': 0, 'TAT': 0, 'GGT': 0, 'TGT': 0, 'CGA': 0, 'CCA': 0, 'CGC': 0, 'GAT': 0, 'CGG':0, 'TTT': 0, 'TGC': 0, 'GGG': 0, 'TGA': 0, 'GGA': 0, 'TGG': 0, 'GGC': 0, 'TAC': 0, 'TTC': 0, 'TCG':0, 'TTA': 0, 'TTG': 0, 'CGT': 0, 'GAA': 0, 'TCA': 0, 'GCA': 0, 'GTA': 0, 'GCC': 0, 'GTC': 0, 'GCG': 0, 'GTG': 0, 'GAG': 0, 'GTT':0, 'GCT':0, 'GAC': 0, 'TCC': 0, 'TAA': 0, 'TCT': 0}

    count = 0
    linecount = 0
    #for i in range(len(f)):
    for i in range(len(f)):
        if f[i][0]!= '>':
            #numeric_freq = {}
            linecount += 1
            if ((len(f[i])-1)%3)==0:
                #print f[i]
                for x in range(0,len(f[i])/3):
                    codon = list(islice(f[i],x*3,(x+1)*3))
                    if codon:
                        #print str(codon)
                        codon_string = ''.join(codon)
                        #print codon_string
                        codon_list.append(codon_string)
                        codon_dict[codon_string]=codon_dict[codon_string]+1
                        count+=1
                        #print codon_string
                #numeric_freq = {x: codon_list.count(x) for x in codon_list}
                #print numeric_freq
            else:

                '''print "Sequence must have elements in multiples of 3"'''
                #print f[i]
                #print linecount
    #total_seq = ''.join(codon_list)
    #print total_seq
    #mrna_seq(codon_list)
    #print codon_dict
    return codon_dict

#print usage_calc(f, codon_list)

def mrna_seq(seq):
    f = open(seq).readlines()
    #print f
    codon_list = []
    count = 0
    linecount = 0
    # for i in range(len(f)):
    for i in range(len(f)):
        if f[i][0] != '>':
            # numeric_freq = {}
            linecount += 1
            #print (len(f[i])-1)
            if ((len(f[i]) - 1) % 3) == 0:
                #print f[i]
                for x in range(0, len(f[i]) / 3):
                    codon = list(islice(f[i], x * 3, (x + 1) * 3))
                    if codon:
                        # print str(codon)
                        codon_string = ''.join(codon)
                        # print codon_string
                        codon_list.append(codon_string)
                        #codon_dict[codon_string] = codon_dict[codon_string] + 1
                        count += 1
                        # print codon_string
                        # numeric_freq = {x: codon_list.count(x) for x in codon_list}
                        # print numeric_freq
            else:

                '''print "Sequence must have elements in multiples of 3"'''
                # print f[i]
                # print linecount
    # total_seq = ''.join(codon_list)
    # print total_seq
    # mrna_seq(codon_list)
    #return codon_dict
    #total_sequence = ''.join(codon_list)
    return codon_list

'''seq = raw_input('protein: ')
x = mrna_seq(seq)
print x
print len(x)
print (len(x))/3'''