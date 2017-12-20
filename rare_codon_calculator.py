def calc_avg(codon_list):
   #sum_freq = sum(codon_dict.itervalues())
   sum_freq = sum(codon_list)
   avg_freq = float(sum_freq/len(codon_list))
   avg_freq = round(avg_freq, 1)
   return avg_freq

def calc_minmax_avg(min_max_list):
    #min_max = min_max_dict.values()
    #list(map(sum, min_max))
    #min_sum = sum([pair[0] for pair in min_max])
    #max_sum = sum([pair[1] for pair in min_max])
    min_sum = sum((i[0]) for i in min_max_list)
    max_sum = sum((i[1]) for i in min_max_list)
    min_avg = round(float(min_sum/len(min_max_list)),1)
    max_avg = round(float(max_sum / len(min_max_list)),1)
    min_max_avg = [min_avg,max_avg]
    return min_max_avg

def calc_percent(actual_val, min_max_val, avg_val):
    #print actual_val, min_max_val, avg_val
    max_percent = ((actual_val-avg_val)/(min_max_val[1]-avg_val))* 100
    if max_percent >= 0:
        #print '%Max is: '
        return max_percent
    else:
        min_percent = (((avg_val - actual_val) / (avg_val - min_max_val[0])) * 100)
        #print '%Min is: '
        return -1*min_percent

from max_min_codon_usage import actual_counter, max_min_counter, avg_return

#actual_dict = actual_counter()
#min_max_dict = max_min_counter()
#avg_dict = avg_return()



'''actual_dict = {'ATG': 26.2, 'AAG': 12.7, 'TCG' : 8.5, 'AGG' : 2.2, 'ACC' : 21.7}
min_max_dict = {'M': [26.2, 26.2], 'K': [ 12.7,35.4], 'S' : [8.5, 15.0], 'R' : [2.2,19.8], 'T' : [9.7,21.7]}
avg_dict = {'M': 26.2, 'K': 24.1, 'S' : 10.6, 'R' : 9.2, 'T' : 13.2}

actual_val = calc_avg(actual_dict.values())
min_max_val = calc_minmax_avg(min_max_dict.values())
avg_val = calc_avg(avg_dict.values())

print calc_percent(actual_val, min_max_val, avg_val)'''