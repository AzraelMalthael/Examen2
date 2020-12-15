# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:53:19 2020
@author: Windows Vista
"""

import random
import numpy
import numpy as np
from deap import algorithms
from deap import base, creator, tools

import pandas as pd
dato=pd.read_csv("datos2.csv")

aux=np.array(dato)

num_lug = 4
distancia =aux
print (aux)
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)
toolbox = base.Toolbox()

toolbox.register("indices", random.sample, range(num_lug),  num_lug)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def EVALUATE(individual):
    summation = 0
    start = individual[0]
    for i in range(1, len(individual)):
        end = individual[i]
        summation =summation+distancia[start][end],
        start = end
    return summation

toolbox.register("evaluate", EVALUATE)

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.01)
toolbox.register("select", tools.selTournament, tournsize=2)

def main():
    random.seed(169)

    pop = toolbox.population(n=300)

    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    
    algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=40, stats=stats, 
                        halloffame=hof)
    
    return pop, stats, hof

if __name__ == "__main__":
    main()
