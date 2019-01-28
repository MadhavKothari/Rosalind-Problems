# python template code for exercise ID REVC (Complementing a Strand of DNA)
# your code *must* define a function called run to work

def run(ss) :
	comp = ''
	for bp in ss[::-1]:
		if bp == 'A':
			comp += 'T'
		if bp == 'T':
			comp += 'A'
		if bp == 'G':
			comp += 'C'
		if bp == 'C':
			comp += 'G'
	print (comp)

  # compute and print with the print() function the reverse complement of the
  #DNA sequence ss
	pass
