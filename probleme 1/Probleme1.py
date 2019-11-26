#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`Probleme1` module

:author:Arnaud Kaderi, Elhadj Ibrahima BAH, Aboubakar Siriki DIAKITE


:date: 2019, october
:last revision: 2019, october

"""
from random import*
from Individual1 import*
from math import*


class Problem_interface():
    
    def __init__(self, x_min, x_max):
        self.__x_min = x_min
        self.__x_max = x_max
        pass
    def get_x_min(self):
        return self.__x_min
    def get_x_max(self):
        return self.__x_max
    def best_individual(self,population):
        """
        return the best fitted individual from population. Depending on the problem, it can correspond to the individual with the highest or the lowest fitness value.
        :param population: list(Individual) the list of individuals to sort.
        :rtype: an Individuals to sort.
        :return: the best fitted individual of population.
        """
        
        return population[-1].get_value()
        
    def create_individual(self):
        """
        create a randomly generated indidivual for this problem.
        :rtype: an Individual object.
        :return: a randomly generated individual for this problem.
        """
        individual = Individual_Interface(12)
        individual.init_value()
        return individual
    def evaluate_fitness(self,individual):
        """
        compute the fitness of individual for this problem.
        :param individual: (an Individual object) - the individual to consider.
        :rtype: int 
        :return: the fitness of individual for this problem
        """
        X=0
        X = self.get_x_min()+ individual.calculate_N() *(self.get_x_max() - self.get_x_min())/(2**12)
        return (X**2)*sin(X)*cos(X)

    def sort_population(self,population):
        """
        sort population from best fitted to worst fitted individuals. Depending on the problem, it can correspond to ascending or descending order with respect to the fitness function.
        :param population: (list(Individual)) - the list of individuals to sort.
        side effecrt: population is modified by this method.
        """
        population.sort(key = lambda individual: individual.get_value())
        
        
    def tournament(self,first,second):
        """
        perform a tounament between two individuals, the winner is the most fitted one, it is returned.
        :param first: (an Individual object) - an individual.
        :param second: (an Individual object) - an individual.
        rtype: Individual object
        :return: the winner of the tournament
        """
        if self.evaluate_fitness(first) > self.evaluate_fitness(second):
            return first
        else:
            return second
    def average_population(self,population):
        """
        calculate the average population for the generation concerned
        :param population: 
        :rtype: (int)(list(Individual)) - the list of individuals
        :return: the average of the individuals according to the problem
        """
        add = 0
        average = 0
        for e in population:
            for gene in e:
                add += gene
        average = add/len(population)
        return average
                
