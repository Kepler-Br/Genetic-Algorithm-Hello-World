import random
import GeneticAlgorithm


class FitnessScaling:
    # c - [1, 5]
    # @staticmethod
    # def sigma_truncation(pop, F, c):
    #     fitnesses = map(pop, key=lambda x: x.fitness)
    #     sigma = stdev(fitnessesArray)
    #     fitnessAvarage = mean(fitmessea)
    #     result = F + (fitnessAvarage + c * sigma)
    #     return result

    # k is around 1.
    # Ex: k = 1.005
    @staticmethod
    def power_law(F, k):
        return pow(F, k)

    @staticmethod
    def linear(F, a, b):
        return F * a + b

    @staticmethod
    def none(F):
        return


class Crossover:
    @staticmethod
    def masked(father, mother):
        assert (len(father.gene) == len(mother.gene)), "Parent's gene should be same length"
        gene_len = len(father.gene)
        mask = random.choices([0, 1], k=gene_len)
        child = GeneticAlgorithm.Chromosome()
        for i in range(gene_len):
            if mask[i] == 0:
                allele = father.gene[i]
            else:
                allele = mother.gene[i]
            child.gene.append(allele)
        return child

    @staticmethod
    def one_point(father, mother):
        assert(len(father.gene) == len(mother.gene)), "Parent's gene should be same length"
        gene_len = len(father.gene)
        child = GeneticAlgorithm.Chromosome()
        slice_place = random.randint(0, gene_len)
        child.gene.extend(father.gene[0:slice_place])
        child.gene.extend(mother.gene[slice_place:])
        return child


class Selection:
    @staticmethod
    def roulette(pop, count):
        weights = []
        fitness_sum = sum([x.fitness for x in pop])
        for member in pop:
            weights.append(member.fitness / fitness_sum)
        parent_pool = random.choices(pop, weights=weights, k=count)
        return parent_pool

    @staticmethod
    def tournament(pop, count):
        parent_pool = []
        for _ in range(count):
            pool = random.choices(pop, k=2)
            winner = max(pool, key=lambda x: x.fitness)
            parent_pool.append(winner)
        return parent_pool

    @staticmethod
    def rank(pop, count):
        sort = sorted(pop, key=lambda x: x.fitness)
        ranks = range(1, len(pop) + 1)
        return random.choices(sort, weights=ranks, k=count)


class GeneticOperators:
    @staticmethod
    def mutate(target, phenotype):
        gene_len = len(target.gene)
        result = GeneticAlgorithm.Chromosome()
        result.gene = target.gene
        index = random.randint(0, gene_len - 1)
        new_allele, alternative_allele = random.sample(phenotype, 2)
        if new_allele == result.gene[index]:
            result.gene[index] = alternative_allele
        else:
            result.gene[index] = new_allele
        result.fitness = GeneticAlgorithm.calc_fitness(result)
        return result

    @staticmethod
    def randomize_gene(target, gene_len, phenotype):
        target.gene = random.choices(phenotype, k=gene_len)
