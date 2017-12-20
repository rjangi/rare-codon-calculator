#A = 'AGUUGUCA-'
#B = 'AG-UGUUAA'
#A = 'ddddddd'
#B = 'eeeeeee'
#X = 'AGUU'
#Y = 'AG--'
seq1 = raw_input('Enter sequence 1 ')
seq2 = raw_input('Enter sequence 2 ')
C = open(seq1).read()
P = open(seq2).read()


def window(A,B,size):
    #print len(A) - size
    output = []
    for i in range((len(A)-size)+1):
        temp_A = []
        temp_B = []
        for j in range(size):
            temp_A += A[i+j]
            temp_B += B[i+j]
            #print temp_A
        #if temp_A == temp_B:
            #output+='1'
        #else:
            #output+='0'
        count = 0
        for z in range(len(temp_A)):
            if temp_A[z] != temp_B[z]:
                count += 1
            else:
                #count+= 0
                pass
        #print count
        if count > 1:
            output+='0'
        else:
            output+='1'
        #print temp_A
        #print temp_B
    results = map(int, output)
    return results

#x = window(A,B,3)
#print x
vec = window(C,P,30)
filename = raw_input('Enter a file name: ')
f=open(filename,'w')
for i in range(len(vec)):
    f.write(str(i+1)+ ' '+ str(vec[i]) + '\n')
