
seq = raw_input("enter a file: ")
f = open(seq).readlines()
#print codon_table_creator(f)
print len(f)

'''i = 1
f = open('file')
for line in f.readlines():
    if i % 2 == 0 :
        print line
    i += 1'''
codon_table = {'I':['ATT', 'ATC', 'ATA'],'L':['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'],'V':['GTT', 'GTC', 'GTA', 'GTG'], 'F':['TTT', 'TTC'],'M':['ATG'],'C':['TGT', 'TGC'], 'A':['GCT', 'GCC', 'GCA', 'GCG'],'G':['GGT', 'GGC', 'GGA', 'GGG'], 'P':['CCT', 'CCC', 'CCA', 'CCG'], 'T':['ACT', 'ACC', 'ACA', 'ACG'], 'S':['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], 'Y':['TAT', 'TAC'], 'W':['TGG'], 'Q':['CAA', 'CAG'], 'N':['AAT', 'AAC'], 'H':['CAT', 'CAC'], 'E':['GAA', 'GAG'], 'D':['GAT', 'GAC'], 'K':['AAA', 'AAG'], 'R':['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], '*':['TAA', 'TAG', 'TGA']}