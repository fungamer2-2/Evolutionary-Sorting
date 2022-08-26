# Evolutionary-Sorting
A genetic algorithm tries to sort an array

The AI attempts to generate a network to sort a specific array in only `n` swaps<br />
It generates 5 AIs for an initial population, each with randomly generated chromosomes (lists of network pairings of length `n`), runs the network, and assigns a fitness score based on the number of inversions (higher score = fewer inversions) <br />
Then it takes the best two to reproduce and create the next generation of AIs:<br />
It does a crossover at a random position of the chromosomes, then each gene in the chromosome has a chance to mutate (be replaced by a new random gene)<br />
Then it continues with the hope that it finds the network to sort the specific array<br /><br />
You can adjust the number of runs it does <br />
It runs for `TOTAL` generations, then it returns the output of best run so you can see how close it got to sorting
