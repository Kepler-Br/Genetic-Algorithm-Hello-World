import random
from GeneticOperators import Selection, Crossover, FitnessScaling, GeneticOperators
from functools import reduce


class Chromosome:
    def __init__(self):
        self.gene = []
        self.fitness = 0.0


def calc_fitness(chromosome):
    fitness = 0
    for allele in chromosome.gene:
        fitness += allele
    return fitness


# Probability of true.
# probability is on [0, 1]
def decision(probability):
    return random.random() <= probability


class GeneticAlgorithm(object):
    def __init__(self):
        self.pop = []
        self.parentPool = []
        self.generation = 0
        self.popSize = 100
        self.geneLen = 100
        self.mutationChance = 0.1
        self.eliteCount = 2
        self.phenotype = [0, 1]
        self.selection = Selection.tournament
        self.crossover = Crossover.masked
        self.fitnessScaling = FitnessScaling.none

    def loop(self, target_fitness, target_generation=5000):
        self.generate_pop()
        while self.generation < target_generation:
            elite = self.get_best(self.eliteCount)
            self.do_selection()
            self.do_crossover()
            self.do_mutation()
            self.pop.extend(elite)
            self.print_info()
            self.generation += 1
            if self.best_fitness() >= target_fitness:
                break

    def do_crossover(self):
        self.pop = []
        for _ in range(self.popSize):
            parents = random.sample(self.parentPool, 2)
            child = self.crossover(parents[0], parents[1])
            child.fitness = calc_fitness(child)
            self.pop.append(child)

    def do_selection(self):
        self.parentPool = self.selection(self.pop, self.popSize)

    def do_mutation(self):
        for i in range(len(self.pop)):
            if decision(self.mutationChance):
                mutated = GeneticOperators.mutate(self.pop[i], self.phenotype)
                self.pop.append(mutated)

    def get_best(self, count=1):
        return sorted(self.pop, key=lambda x: x.fitness, reverse=True)[0:count]

    def generate_pop(self):
        self.pop = []
        for _ in range(self.popSize):
            member = Chromosome()
            GeneticOperators.randomize_gene(member, self.geneLen, self.phenotype)
            self.pop.append(member)
        self.recalculate_fitness()

    def recalculate_fitness(self):
        for member in range(len(self.pop)):
            self.pop[member].fitness = calc_fitness(self.pop[member])

    def average_fitness(self):
        sum_val = reduce(lambda x, y: x + y.fitness, self.pop, 0.0)
        quantity = len(self.pop)
        return sum_val / quantity

    def best_fitness(self):
        best = max(self.pop, key=lambda x: x.fitness)
        return best.fitness

    def worst_fitness(self):
        worst = min(self.pop, key=lambda x: x.fitness)
        return worst.fitness

    def print_info(self):
        best = self.best_fitness()
        avg = self.average_fitness()
        print(f"Generation: {self.generation}, Average fitness: {avg}, Best: {best}, Pop count: {len(self.pop)}")
