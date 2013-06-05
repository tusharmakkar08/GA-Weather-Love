from pyevolve import *
def perfect_weather(chromosome):
	""" Fitness Function for the program
		Parameter: chromosome
		Type: One dimensional list
		Returns: Score of the function
		Type: Float """
	if flag1==1:
		sun = chromosome[0]
	else:
		sun = float(100)/(chromosome[2]+1)
	if flag2==1:
		rain=chromosome[0]
	else:
		rain = float(100)/(chromosome[1]+1)
	if flag3==1:
		wind = chromosome[2]
	else:
		wind = float(100)/(chromosome[2]+1)
	score = (sun+rain+wind)/300
	return score

def main(flag1,flag2,flag3):
	genome = G1DList.G1DList(3)
	""" A One dimensional List is made which consists of 3 elements
		- Sun , Rain and Wind . Basically a Genome instance"""
	genome.setParams(rangemin= 0, rangemax=100)
	""" Setting Maximum Percentage of weather to 100 """
	genome.evaluator.set(perfect_weather)
	""" The evaluator function (objective function) """
	ga = GSimpleGA.GSimpleGA(genome)
	""" We are using GsimpleGA algorithm made by Goldberg """
	ga.evolve(freq_stats=10)
	""" Do the evolution, with stats dump
		frequency of 10 generations """
	print ga.bestIndividual()
	""" Printing the best Individual """
	
if __name__ == "__main__":
	print "Enter Your weather Love"
	print "-----------------------------------------------------------------"
	flag1=0
	flag2=0
	flag3=0
	"""
	Flag1 : Used for checking whether the weather you like is sunny 
	Flag2 : Used for checking whether the weather you like is rainy
	Flag3 : Used for checking whether the weather you like is windy 
	"""
	a=raw_input("Do you like sunny weather ?\n")
	if "y" in a or "Y" in a:
		flag1=1
	a=raw_input("Do you like rainy weather ?\n")
	if "y" in a or "Y" in a:
		flag2=1
	a=raw_input("Do you like windy weather ?\n")
	if "y" in a or "Y" in a:
		flag3=1
	main(flag1,flag2,flag3)
