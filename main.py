from GeneticAlgorithm import GeneticAlgorithm


GA = GeneticAlgorithm()
# Generate population with default settings.
GA.generate_pop()

GA.geneLen = 50
# Set set of possible values for alleles.
GA.phenotype = list(range(0, 2))

# Set target fitness based on maximum possible.
targetFitness = max(GA.phenotype)*GA.geneLen
# Start genetic magic.
GA.loop(targetFitness)
print("Done!")

print(f"Best fitness: {GA.best_fitness()}")
print(f"Worst fitness: {GA.worst_fitness()}")
