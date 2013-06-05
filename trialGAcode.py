from pyevolve import G1DList
from pyevolve import GSimpleGA
import sys
def perfect_weather(chromosome):
	sun = chromosome[0]
	no_rain = float(100)/(chromosome[1]+1)
	no_wind = float(100)/(chromosome[2]+1)
	score = (sun + no_rain +no_wind)/300
	return score
def main():
	genome = G1DList.G1DList(3)
	genome.setParams(rangemin= 0, rangemax=100)
	genome.evaluator.set(perfect_weather)
	ga = GSimpleGA.GSimpleGA(genome)
	ga.evolve(freq_stats=10)
	print ga.bestIndividual()
if __name__ == "__main__":
    main() 
