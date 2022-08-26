# Evolutionary-Sorting
An evolutionary algorithm tries to sort an array

The AI attempts to generate a network to sort a specific array in only n swaps
It generates 5 genes (sets of network pairings), runs the network, and assigns a score based on the number of inversions (higher score = fewer inversions)
Then it takes the best two to reproduce and generate 5 more AIs:
It does a crossover at a random position of the genes, then each piece in the gene has a chance to mutate (be replaced by a new random pairing)
Then it continues with the hope that it finds the network to sort the specific array
