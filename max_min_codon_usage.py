

def protein_creator(seq):
    from Bio.Seq import Seq
    from Bio.Alphabet import generic_dna
    from codon_usage import mrna_seq

    m_rna = mrna_seq(seq)
    x = ''.join(m_rna)
    coding_strand = Seq(x, generic_dna)
    protein = str(coding_strand.translate())
    return protein
def protein_list(seq):
    seqx = list(protein_creator(seq))
    return seqx
#seq = raw_input('protein')
#print protein_list(seq)
#seq = raw_input('protein: ')
#print protein_list(seq)
#seq1 = raw_input('protein: ')
#print protein_creator(seq1)

def actual_counter(seq1, seq2):
    #print ('Enter the protein sequence here')
    #from codon_objects import fun

    #strand = fun(seq1)

    #m_rna = strand.list
    from codon_usage import mrna_seq

    m_rna = mrna_seq(seq1)
    #print('Enter genome file here:')
    from actual_codon_usage import actual_count
    codon_dict = actual_count(seq2)
    from collections import OrderedDict
    actual_dict = OrderedDict()
    #actual_dict = {}
    for i in range(len(m_rna)):
        #codon = m_rna[i]
        #print m_rna[i]
        actual_dict[m_rna[i]] = codon_dict[m_rna[i]]
    #print m_rna
    #print len(m_rna)
    #print len(actual_dict)
    return actual_dict

#seq1 = raw_input('protein: ')
#seq2 = raw_input('genome: ')
#print actual_counter(seq1, seq2)




def max_min_counter(seq1,seq2):
    #from codon_usage import mrna_seq

    #m_rna = mrna_seq(seq1)
    protein = protein_creator(seq1)
    #print('what is going on')
    from actual_codon_usage import actual_count
    #coding_dna = []
    #print('Enter genome file here:')
    codon_dict = actual_count(seq2)
    codon_table = {'I': ['ATT', 'ATC', 'ATA'], 'L': ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'],
                   'V': ['GTT', 'GTC', 'GTA', 'GTG'], 'F': ['TTT', 'TTC'], 'M': ['ATG'], 'C': ['TGT', 'TGC'],
                   'A': ['GCT', 'GCC', 'GCA', 'GCG'], 'G': ['GGT', 'GGC', 'GGA', 'GGG'],
                   'P': ['CCT', 'CCC', 'CCA', 'CCG'], 'T': ['ACT', 'ACC', 'ACA', 'ACG'],
                   'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], 'Y': ['TAT', 'TAC'], 'W': ['TGG'],
                   'Q': ['CAA', 'CAG'], 'N': ['AAT', 'AAC'], 'H': ['CAT', 'CAC'], 'E': ['GAA', 'GAG'],
                   'D': ['GAT', 'GAC'], 'K': ['AAA', 'AAG'], 'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
                   '*': ['TAA', 'TAG', 'TGA']}
    from collections import OrderedDict
    maxmin_dict = OrderedDict()
    #maxmin_dict = {}
    #avg_dict = OrderedDict

    for i in range(len(protein)):
        x = protein[i]
        y = codon_table[x]

        #y = list of codons that code for the amino acid referenced by the amino acid at position protein[i]
        y = codon_table[protein[i]]
        #lowest possible frequency
        z = 0
        #highest possible frequency
        r = 1000
        #p = 0
        #count = 0
        for j in range(len(y)):
            if codon_dict[y[j]] > z:
                z = codon_dict[y[j]]
            if codon_dict[y[j]] < r:
                r = codon_dict[y[j]]
            #p+=codon_dict[y[j]]
            #count+=1

        #add key-value pair of max codon and frequency
        #print 'max: '+ str(z) +' min: '+str(r)
        maxmin_dict[protein[i]]=[r,z]
        #avg_dict[x] = float(p/count)
        #add key-value pair of min codon and frequency

    #print(avg_return(avg_dict))
    #avg_return(avg_dict)
    #print avg_dict
    return maxmin_dict
#seq1 = raw_input('protein: ')
#seq2 = raw_input('genome: ')
#print max_min_counter(seq1, seq2)

def avg_return(seq1,seq2):
    protein = protein_creator(seq1)

    from actual_codon_usage import actual_count

    #print('Enter genome file here:')
    codon_dict = actual_count(seq2)
    codon_table = {'I': ['ATT', 'ATC', 'ATA'], 'L': ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'],
                   'V': ['GTT', 'GTC', 'GTA', 'GTG'], 'F': ['TTT', 'TTC'], 'M': ['ATG'], 'C': ['TGT', 'TGC'],
                   'A': ['GCT', 'GCC', 'GCA', 'GCG'], 'G': ['GGT', 'GGC', 'GGA', 'GGG'],
                   'P': ['CCT', 'CCC', 'CCA', 'CCG'], 'T': ['ACT', 'ACC', 'ACA', 'ACG'],
                   'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], 'Y': ['TAT', 'TAC'], 'W': ['TGG'],
                   'Q': ['CAA', 'CAG'], 'N': ['AAT', 'AAC'], 'H': ['CAT', 'CAC'], 'E': ['GAA', 'GAG'],
                   'D': ['GAT', 'GAC'], 'K': ['AAA', 'AAG'], 'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
                   '*': ['TAA', 'TAG', 'TGA']}
    from collections import OrderedDict
    #maxmin_dict = OrderedDict()
    # maxmin_dict = {}
    avg_dict = OrderedDict()

    for i in range(len(protein)):
        x = protein[i]
        y = codon_table[x]

        # y = list of codons that code for the amino acid referenced by the amino acid at position protein[i]
        y = codon_table[protein[i]]
        # lowest possible frequency
        z = 0
        # highest possible frequency
        r = 1000
        p = 0
        count = 0
        for j in range(len(y)):
            #if codon_dict[y[j]] > z:
                #z = codon_dict[y[j]]
            #if codon_dict[y[j]] < r:
                #r = codon_dict[y[j]]
            p += codon_dict[y[j]]
            count += 1

        avg_dict[x] = float(p / count)
    return avg_dict
#seq1 = raw_input('protein: ')
#seq2 = raw_input('genome: ')
#print actual_counter(seq1, seq2)
'''protein = raw_input('Protein sequence file: ')
genome = raw_input('Genome file: ')
actual_dict = actual_counter(protein,genome)
min_max_dict = max_min_counter(protein,genome)
avg_dict = avg_return(protein, genome)
print actual_dict
print min_max_dict
print avg_dict'''



'''codon_table = {'I': ['ATT', 'ATC', 'ATA'], 'L': ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'],
               'V': ['GTT', 'GTC', 'GTA', 'GTG'], 'F': ['TTT', 'TTC'], 'M': ['ATG'], 'C': ['TGT', 'TGC'],
               'A': ['GCT', 'GCC', 'GCA', 'GCG'], 'G': ['GGT', 'GGC', 'GGA', 'GGG'],
               'P': ['CCT', 'CCC', 'CCA', 'CCG'], 'T': ['ACT', 'ACC', 'ACA', 'ACG'],
               'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], 'Y': ['TAT', 'TAC'], 'W': ['TGG'],
               'Q': ['CAA', 'CAG'], 'N': ['AAT', 'AAC'], 'H': ['CAT', 'CAC'], 'E': ['GAA', 'GAG'],
               'D': ['GAT', 'GAC'], 'K': ['AAA', 'AAG'], 'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
               '*': ['TAA', 'TAG', 'TGA']}'''

