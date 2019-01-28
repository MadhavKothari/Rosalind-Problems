# python template code for exercise ID GC (Computing GC Content)
# your code *must* define a function called run to work

def run(fasta_str) :
	ma = 0
	ID = ''
	file = fasta_str.split('\n')
	file.remove(file[-1])
	for line in file:
        	count = 0
        	if line[0] == '>':
                	temp_ID = line.lstrip('>')
        	else:
                	for bp in line:
                        	if bp == 'G' or bp == 'C':
                                	count += 1
               		GC = (count/len(line))
                	if ma < GC:
                        	ma = GC 
	                       	ID = temp_ID 
	ma =  ma * 100.00
	print(ID, ma, sep = '\n') 

  # calculate the %GC content of each DNA sequence in the fasta records of fasta_str
  # fasta_str is a single string with each line separated by a newline character
  # retain the sequence name and gc content of the sequence with the highest %gc
  # print out the sequence name with the print function on its ownline
  # then print out the %GC of the sequence with the print function on the next line


