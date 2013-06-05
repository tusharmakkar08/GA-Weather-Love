from pyevolve import G1DList
from pyevolve import GSimpleGA
import sys

def perfect_weather(chromosome):
	""" Fitness Function for the program
		Parameter: chromosome
		Type: One dimensional list
		Returns: Score of the function
		Type: Float """
	sun = chromosome[0]
	no_rain = float(100)/(chromosome[1]+1)
	no_wind = float(100)/(chromosome[2]+1)
	score = (sun + no_rain +no_wind)/300
	return score

def main():
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
    main() 
