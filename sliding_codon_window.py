#size = raw_input('Enter a window size')
'''def window(iterable, size):
    i = iter(iterable)
    win = {}
    for e in range(0, size):
        win.update(next(i))
    yield win
    for e in i:
        win = win[1:] + [e]
        yield win
    #return dict(win)'''


def actual_return(actual):
    actual_freq = actual.values()
    #minmax_freq = minmax.values()
    #avg_freq = avg.values()
    return actual_freq

def minmax_return(minmax):
    #actual_freq = actual.values()
    minmax_freq = minmax.values()
    #avg_freq = avg.values()
    return minmax_freq


def avg_return(avg):
    #actual_freq = actual.values()
    #minmax_freq = minmax.values()
    avg_freq = avg.values()
    return avg_freq

from collections import OrderedDict
def window(actual,minmax,avg, size,seq1):
    #print actual.values(), minmax.values(), avg.values()
    from codon_usage import mrna_seq
    from max_min_codon_usage import protein_list

    protein = protein_list(seq1)
    #print protein
    from rare_codon_calculator import calc_avg, calc_minmax_avg, calc_percent
    output = []
    #print actual
    #actual = actual_return(actual)
    actualx = mrna_seq(seq1)
    #minmax = minmax_return(minmax)
    #avg = avg_return(avg)
    #print len(minmax), len(actual), len(avg)
    for i in range(len(actualx)-size):
        temp_actual = []
        temp_minmax = []
        temp_avg = []
        for j in range(size):
            #print j
            #print actual[i+j]
            temp_actual += [actual[actualx[i+j]]]
            #print i,j
            #print minmax[i+j]
            temp_minmax += [minmax[protein[i+j]]]
            temp_avg += [avg[protein[i+j]]]
        #print temp_actual, temp_minmax, temp_avg
        x = calc_avg(temp_actual)
        #print x
        y = calc_minmax_avg(temp_minmax)
        #print y
        z = calc_avg(temp_avg)
        #print z
        percent = calc_percent(x,y,z)
        output += [percent]
    #print len(output)
    return output
    #return temp_actual


def single_window(actual, seq1):

    from codon_usage import mrna_seq
    from max_min_codon_usage import protein_list

    #protein = protein_list(seq1)

    #from rare_codon_calculator import calc_avg, calc_minmax_avg, calc_percent
    output = []

    actualx = mrna_seq(seq1)

    for i in range(len(actualx)):
        #temp_actual = []
        #temp_minmax = []
        #temp_avg = []
        #for j in range(size):

        output += [actual[actualx[i]]]

            #temp_minmax += [minmax[protein[i+j]]]
            #temp_avg += [avg[protein[i+j]]]

        #x = calc_avg(temp_actual)

        #y = calc_minmax_avg(temp_minmax)

        #z = calc_avg(temp_avg)

        #percent = calc_percent(x,y,z)

    return output
from max_min_codon_usage import actual_counter
seq1 = raw_input('protein file: ')
genome = raw_input('genome file: ')
actual = actual_counter(seq1,genome)
#print actual
x = single_window(actual, seq1)
#print x
filename = raw_input('Enter a file name: ')
f=open(filename,'w')
for i in range(len(x)):
    f.write(str(i+1)+ ' '+ str(x[i]) + '\n')
    #f.write(str(i+1)+ ' '+ str(x[i]) + '\n')
    #f.write(str(i+1)+ ' '+ str(x[i]) + '\n')
#print len(x)

def codon_count(protein):
    lines = open(protein).readlines()[1:]
    characters = 0
    for line in lines:
        for i in range(len(line)):
            characters+=1
    codons = characters/3
    #print characters
    return codons


'''from max_min_codon_usage import actual_counter, max_min_counter, avg_return
protein = raw_input('Protein sequence file: ')
size_p = codon_count(protein)
genome = raw_input('Genome file: ')
actual_dict = actual_counter(protein,genome)
min_max_dict = max_min_counter(protein,genome)
avg_dict = avg_return(protein, genome)
#f = open(protein).readlines()


print window(actual_dict, min_max_dict, avg_dict, size_p, protein)'''
'''actual_dict = {'ATG': 26.2, 'AAG': 12.7, 'TCG' : 8.5, 'AGG' : 2.2, 'ACC' : 21.7}
min_max_dict = {'M': [26.2, 26.2], 'K': [ 12.7,35.4], 'S' : [8.5, 15.0], 'R' : [2.2,19.8], 'T' : [9.7,21.7]}
avg_dict = {'M': 26.2, 'K': 24.1, 'S' : 10.6, 'R' : 9.2, 'T' : 13.2}
protein = raw_input('enter protein: ')
print window(actual_dict, min_max_dict, avg_dict, 4, protein)'''




#y = window(actual_dict,3)

