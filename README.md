GA-Weather-Love
================

Genetic Algorithm for finding weather preference of a person using Pyevolve .

Requirements :
-------------
	
* Pyevolve 
* Python

Project Details :
----------------

Individuals are the weather descriptions, and weather preference is measured by your fitness function.

* trialGAcode.py :

		
This is the trial code with extreemely simple Fitness Function . Here we have assumed that we like sunny days and hate both rainy and windy days . 
		
SAMPLE OUTPUT FOR TRIAL CODE:
-----------------------------
		
<pre>
Gen. 0 (0.00%): Max/Min/Avg Fitness(Raw) [0.23(0.68)/0.18(0.01)/0.19(0.19)]
Gen. 10 (10.00%): Max/Min/Avg Fitness(Raw) [1.17(0.99)/0.00(0.34)/1.16(0.98)]
Gen. 20 (20.00%): Max/Min/Avg Fitness(Raw) [1.17(0.99)/0.00(0.34)/1.16(0.98)]
Gen. 30 (30.00%): Max/Min/Avg Fitness(Raw) [1.15(0.99)/0.00(0.34)/1.09(0.95)]
Gen. 40 (40.00%): Max/Min/Avg Fitness(Raw) [1.17(0.99)/0.00(0.34)/1.16(0.98)]
Gen. 50 (50.00%): Max/Min/Avg Fitness(Raw) [1.17(0.99)/0.00(0.34)/1.16(0.98)]
Gen. 60 (60.00%): Max/Min/Avg Fitness(Raw) [1.16(0.99)/0.00(0.34)/1.14(0.97)]
Gen. 70 (70.00%): Max/Min/Avg Fitness(Raw) [1.16(0.99)/0.00(0.34)/1.14(0.97)]
Gen. 80 (80.00%): Max/Min/Avg Fitness(Raw) [1.17(0.99)/0.00(0.34)/1.16(0.98)]
Gen. 90 (90.00%): Max/Min/Avg Fitness(Raw) [1.17(0.99)/0.00(0.34)/1.16(0.98)]
Gen. 100 (100.00%): Max/Min/Avg Fitness(Raw) [1.15(0.99)/0.00(0.34)/1.09(0.95)]
Total time elapsed: 0.175 seconds.
- GenomeBase
	Score:			 0.986667
	Fitness:		 1.145006

	Params:		 {'rangemax': 100, 'rangemin': 0}

	Slot [Evaluator] (Count: 1)
		Name: perfect_weather - Weight: 0.50
		Doc:  Fitness Function for the program
		Parameter: chromosome
		Type: One dimensional list
		Returns: Score of the function
		Type: Float 
	Slot [Initializator] (Count: 1)
		Name: G1DListInitializatorInteger - Weight: 0.50
		Doc:  Integer initialization function of G1DList

   This initializator accepts the *rangemin* and *rangemax* genome parameters.

   
	Slot [Mutator] (Count: 1)
		Name: G1DListMutatorSwap - Weight: 0.50
		Doc:  The mutator of G1DList, Swap Mutator
   
   .. note:: this mutator is :term:`Data Type Independent`

   
	Slot [Crossover] (Count: 1)
		Name: G1DListCrossoverSinglePoint - Weight: 0.50
		Doc:  The crossover of G1DList, Single Point

   .. warning:: You can't use this crossover method for lists with just one element.

   

- G1DList
	List size:	 3
	List:		 [96, 0, 0]


</pre>
