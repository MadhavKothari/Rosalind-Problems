# python template code for exercise ID FIB (Rabbits and Recurrence Relations)
# your code *must* define a function called run to work

def run(n,k) :
	pairs = [1,1]
	i = 2
	while i < n:
		pairs.append(pairs[i-1]+pairs[i-2]*k)
		i += 1
	print (pairs[n-1])
  # print out the number of rabbit pairs that exist after n months if each
  # pair of living rabbits producs a litter of k rabbit pairs
