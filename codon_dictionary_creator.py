with open('codon frequencies.txt', 'r') as document:
    answer = {}
    for line in document:
        line = line.split()
        if not line:  # empty line?
            continue
        answer[line[0]] = line[1:]
#list string to float
#def change_val(answer):
for key,val in answer.items():
    answer[key] = float(val[0])
        #return answer[key]
            #sub = float(sub[0])

#print answer
#print change_val(answer)
print answer