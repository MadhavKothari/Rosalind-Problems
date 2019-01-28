def run(string):

    def mat_dna(file):
        import numpy as np
        seq = ''
        list_seq = []
        lines = file.split('\n')
        for l in lines:
            if '>' in l:
                if seq != '':
                    list_seq.append(list(seq))
                    seq = ''
            else:
                seq += l.strip()
        list_seq.append(list(seq))
        mat_seq = np.matrix(list_seq)
        return mat_seq

    def analize(mat_seq):
        row,clm = np.shape(mat_seq)
        count = np.zeros((4,clm),dtype = np.int)
        for i in range(clm):
            for j in mat_seq[:,i]:
                if j == 'A':
                    count[0,i] += 1
                if j == 'C':
                    count[1,i] += 1
                if j == 'G':
                    count[2,i] += 1
                if j == 'T':
                    count[3,i] += 1
        return count

    def cons(count):
        con = ''
        row,clm = np.shape(count)
        for i in range(clm):
            val = np.argmax(count[:,i])
            if val == 0:
                con += 'A'
            if val == 1:
                con += 'C'
            if val == 2:
                con += 'G'
            if val == 3:
                con += 'T'
        return con

    def print_cons(con,count):
        print(con)
        print('A: ',*count[0,:])
        print('C: ',*count[1,:])
        print('G: ',*count[2,:])
        print('T: ',*count[3,:])

    x = mat_dna(string)
    m = analize(x)
    c = cons(m)
    print_cons(c,m)
