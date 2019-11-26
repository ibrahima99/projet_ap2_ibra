#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`algorithme_génétique_` module

:author:Arnaud Kaderi, Elhadj Ibrahima BAH, Aboubakar Siriki DIAKITE


:date: 2019, october
:last revision: 2019, october

"""

from Probleme1 import* 

class AlgoGen():
    
    def __init__(self, problem, population_size, crossover_rate, mutation_probability):
        """
        build an genetic algorithm to solve problem using a population of size population_size and a probability of muation of mutation_probability
        :param problem: (a Problem object) - the problem to solve
        :param population_size: (int) - the size of the population (must be even)
        :param mutation_probability: (float) - the mutation probability
        :UC: population_size must be even and mutation_probability must be 0<= and <1
        """
        self.__problem = problem
        self.__population_size = population_size
        self.__crossover_rate = crossover_rate
        self.__mutation_probability = mutation_probability
        self.__the_population = []
        self.__crossover_rate = crossover_rate
    def get_population_size(self):
        return self.__population_size
    def init_population(self):
        """
        construction of a population according to size set as a parameter
        :rtype: (int)
        :return: the average of the individuals according to the problem
        """
        for i in range(self.get_population_size()):
            self.__the_population.append(self.__problem.create_individual())
    def public_information(self):
        """
        """
        
        assert self.__the_population != [], "il n'y a pas de population"
        next_gen_1, next_gen_2, next_gen, meilleurs  = [], [], [], []
        self.__problem.sort_population(self.__the_population)
        for i in range(self.__crossover_rate):
            next_gen_1, next_gen_2, next_gen, meilleurs  = [], [], [], []
            for i in range(len(self.__the_population)-1):
                next_gen_1.append(self.__problem.tournament(self.__the_population[i],self.__the_population[i+1]))
                croisements = self.__the_population[i].cross_with(self.__the_population[i+1])
                next_gen_2.append(self.__problem.tournament(croisements[0],croisements[1]))
            next_gen = next_gen_1 + next_gen_2
            for i in range(len(next_gen)):
                next_gen[i].mutate(self.__mutation_probability)
            meilleurs = [self.__the_population[i] for i in range(5)]
            self.__the_population = list()
            next_gen_1 = list()
            next_gen_2 = list()
            
            self.__the_population = meilleurs + [next_gen[i] for i in range(len(next_gen)-5)]
            meilleurs = list()
            next_gen = list()
            #print(next_gen_1)
            
        self.__problem.sort_population(self.__the_population)   
        return self.__problem.best_individual(self.__the_population)
        
        
            
            
            
##            print(i+1, "Génerations")
##            self.__problem.sort_population(self.__the_population)
##            print(self.__problem.best_individual(self.__the_population))
##            print("la moyenne de la Géneration est : ",self.__problem.average_population(self.__the_population))
            
            
        
        
        
    def affiche_population(self):
        assert self.__the_population != [], "il n'y a pas de population"
        for e in self.__the_population:
            print(e.get_value())
    
  