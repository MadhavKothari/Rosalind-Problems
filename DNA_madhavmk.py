# python template code for exercise ID DNA (Counting DNA Nucleotides)
# your code *must* define a function called run to work

def run(s) :
	ca = 0
	cc = 0
	cg = 0 
	ct = 0
	for bp in s:
		if bp == 'A':
			ca += 1
		if bp == 'C':
			cc += 1
		if bp == 'G':
			cg += 1
		if bp == 'T':
			ct += 1
	print (ca, cc, cg, ct)
  # use the print() function to print out counts of A, C, G, and T in s on one
  # line separated by spaces

