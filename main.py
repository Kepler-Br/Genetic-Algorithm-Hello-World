import random
from statistics import stdev
from operator import attrgetter
from functools import reduce

# Probability of true. 
#probability is on [0, 1]
def decision(probability):
    return random.random() <= probability

def calcFitness(chromosome):
    fitness = 0
    for allele in chromosome.gene:
        fitness += allele
    return fitness

class Chromosome:
    def __init__(self):
        self.gene = []
        self.fitness = 0.0
class FitnessScaling:
    # c - [1, 5]
    @staticmethod
    def sigmaTruncation(pop, F, c):
        fitnesses = map(pop, key=lambda x: x.fitness)
        sigma = stdev(fitnessesArray)
        fitnessAvarage = mean(fitmessea)
        result = F + (fitnessAvarage+c*sigma)
        return result

    # k is around 1.
    #Ex: k = 1.005
    @staticmethod
    def powerLaw(F, k):
        return pow(F, k)

    @staticmethod
    def linear(F, a, b):
        return F*a+b

    @staticmethod
    def none(F):
        return

class Crossover:
    @staticmethod
    def masked(father, mother):
        if len(father.gene) != len(mother.gene):
            raise "Parent's gene should be same length"
        geneLen = len(father.gene)
        mask = random.choices([0, 1], k=geneLen)
        child = Chromosome()
        for i in range(geneLen):
            if mask[i] == 0:
                allele = father.gene[i]
            else:
                allele = mother.gene[i]
            child.gene.append(allele)
        return child
    
    def onePoint(father, mother):
        if len(father.gene) != len(mother.gene):
            raise "Parent's gene should be same length"
        geneLen = len(father.gene)
        child = Chromosome()
        slicePlace = random.randint(0, geneLen)
        child.gene.extend(father.gene[0:slicePlace])
        child.gene.extend(mother.gene[slicePlace:])
        return child

class Selection:
    @staticmethod
    def roulette(pop, count):
        weights = []
        fitnessSumm = sum([x.fitness for x in pop])
        for member in pop:
            weights.append(member.fitness/fitnessSumm)
        parentPool = random.choices(pop, weights=weights, k=count)
        return parentPool

    @staticmethod
    def tournament(pop, count):
        parentPool = []
        for _ in range(count):
            pool = random.choices(pop, k=2)
            winner = max(pool, key=lambda x:x.fitness)
            parentPool.append(winner)
        return parentPool

    def rank(pop, count):
       sort = sorted(pop, key=lambda x: x.fitness)
       ranks = range(1, len(pop)+1)
       return random.choices(sort, weights=ranks, k=count)

class GeneticOperators:
    @staticmethod
    def mutate(target, phenotype):
        geneLen = len(target.gene)
        result = Chromosome()
        result.gene = target.gene
        index = random.randint(0, geneLen-1)
        newAllele, alternativeAllele = random.sample(phenotype, 2)
        if newAllele == result.gene[index]:
            result.gene[index] = alternativeAllele
        else:
            result.gene[index] = newAllele
        result.fitness = calcFitness(result)
        return result
    
    @staticmethod
    def randomizeGene(target, geneLen, phenotype):
        target.gene = random.choices(phenotype, k=geneLen)

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
        #self.selection = Selection.rank
        self.crossover = Crossover.masked
        self.fitnessScaling = FitnessScaling.none
    
    def loop(self, targetFitness, targetGeneration = 5000):
        self.generatePop()
        while self.generation < targetGeneration:
            elite = self.getBest(self.eliteCount)
            self.doSelection()
            self.doCrossover()
            self.doMutation()
            self.pop.extend(elite)
            self.printInfo()
            self.generation += 1
            if self.bestFitness() >= targetFitness:
                break
        
    def doCrossover(self):
        self.pop = []
        for _ in range(self.popSize):
            parents = random.sample(self.parentPool, 2)
            child = self.crossover(parents[0], parents[1])
            child.fitness = calcFitness(child)
            self.pop.append(child)
    
    def doSelection(self):
        self.parentPool = self.selection(self.pop, self.popSize)

    def doMutation(self):
        for i in range(len(self.pop)):
            if decision(self.mutationChance):
                mutated = GeneticOperators.mutate(self.pop[i], self.phenotype)
                self.pop.append(mutated)

    def getBest(self, count = 1):
        return sorted(self.pop, key=lambda x: x.fitness, reverse=True)[0:count]

    def generatePop(self):
        self.pop = []
        for _ in range(self.popSize):
            member = Chromosome()
            GeneticOperators.randomizeGene(member, self.geneLen, self.phenotype)
            self.pop.append(member)
        self.recalculateFitness()

    def recalculateFitness(self):
        for member in range(len(self.pop)):
            self.pop[member].fitness = calcFitness(self.pop[member])

    def avarageFitness(self):
        summ =  reduce(lambda x, y: x+y.fitness, self.pop, 0.0)
        quantity = len(self.pop)
        return summ/quantity

    def bestFitness(self):
        best = max(self.pop, key=lambda x: x.fitness)
        return best.fitness

    def printInfo(self):
        best = self.bestFitness()
        avg = self.avarageFitness()
        print("gen: {}, avg: {}, best: {}, pop: {}".format(self.generation, avg, best, len(self.pop)))


GA = GeneticAlgorithm()
GA.generatePop()
GA.printInfo()
targetFitness = max(GA.phenotype)*GA.geneLen
GA.loop(targetFitness)
best = GA.getBest()[0]
print(best.gene)
print(min(best.gene))
print(list(map(lambda x: x.fitness, GA.pop)))
