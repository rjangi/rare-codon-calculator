from max_min_codon_usage import actual_counter, max_min_counter, avg_return
from sliding_codon_window import window
# codon_count
#from rare_codon_calculator import calc_avg, calc_minmax_avg, calc_percent
protein = raw_input('Protein sequence file: ')
genome = raw_input('Genome file: ')
actual_dict = actual_counter(protein,genome)
min_max_dict = max_min_counter(protein,genome)
avg_dict = avg_return(protein, genome)
#protein_size = codon_count(protein)
output = window(actual_dict,min_max_dict,avg_dict,18, protein)
print output
'''for i in range(len(output)):
    if output[i]<0:
        print str(i+1)+ ' '+str(output[i])'''

'''filename = raw_input('Enter a file name: ')
f=open(filename,'w')
for i in range(len(output)):
    for j in range(3):
        f.write(str(i+1)+ ' '+ str(output[i]) + '\n')'''


