seq = raw_input("enter a file: ")
f = open(seq).readlines()
def gene_edit(f):
    count = 0
    linecount = 0
    for i in range(len(f)):
        if f[i][0] == '>':
            for j in range(len(f[i])):

                linecount+=1
            #break
        else:
            continue
    return f