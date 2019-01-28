# python template code for exercise ID HAMM (Counting Point Mutations)
# your code *must* define a function called run to work

def run(s,t) :
	count = 0
	for bp1,bp2 in zip(s,t):
		if bp1 != bp2:
			count += 1
	print (count)
  # count the number of base positions that do not have the same nucleotide
  # across DNA sequences s and t
  # print out the number of differing positions with the print function
