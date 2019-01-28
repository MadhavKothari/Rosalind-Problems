# python template code for exercise ID RNA (Transcribing DNA into RNA)
# your code *must* define a function called run to work

def run(t) :
	mrna = ''
	for bp in t:
		if bp == 'T':
			mrna += 'U'
		else:
			mrna += bp
	print (mrna)
  # print out the DNA sequence in t replacing all Ts with Us
