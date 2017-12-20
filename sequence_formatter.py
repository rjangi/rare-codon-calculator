seq = raw_input("enter a file: ")
f = open(seq).readlines()
def mrna_seq(codon_list):
    total_sequence = ''.join(codon_list)
    return total_sequence