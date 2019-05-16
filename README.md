# lineage
Models the number of generations required to have common ancestor to all living population.

Set population size and number of generations in evolve.py and run the main method. Returns a list of lists where the first member of each list is a child of the current generation, and the subsequent list is all the original ancestors they relate to. A few iterations will demonstrate that of the original generation, each ancestor will either sire every member of the current population, or none of them. 

TODO: Improve data structure: the first number is technically redundant, though convenient for visualizing the lists. 
TODO: Add statistics for how many members of the ancestral generation have barren lineages
TODO: Reduce assumptions of model (currently equal population sizes of 50/50 male/female)
TODO: Make more realistic heuristics for finding partners (based on genetic similarity, as well as chance) 
