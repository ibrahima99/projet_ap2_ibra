#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`Individual1` module

:author:Arnaud Kaderi, Elhadj Ibrahima BAH, Aboubakar Siriki DIAKITE


:date: 2019, october
:last revision: 2019, october

"""
from random import*
from Probleme1 import*

class Individual_Interface():
    
    def __init__(self, size):
        self.__size= size
        self.__genome = []
        self.__fitness = 0
    def copy(self):
        """
        build a copy of self, the genome is a copy of self’s genome
        rtype: an Individual object
        :return: a new Individual which is a « clone » of self
        """
        
        individual_copy = Individual_Interface(self.__size)
        individual_copy.set_value(self.get_value())
        return individual_copy
        
    def cross_with(self,other):
        """
        perform a 1 point crossover between self and other, two new built individuals are returned
        :param other: (an individual)- the individual to croww with
        :rtype: 2_uple of individuals
        :return: the two new individuals built by 1 point crossover operation
        """
        

        position = randint(0,self.get_size()-1)
        new_genome_1 = self.copy()
        new_genome_2 = other.copy()
        alea_1 = new_genome_1.get_value()
        alea_2 = new_genome_2.get_value()
        for i in range(position):
            alea_1[i] ,alea_2[i] = alea_2[i], alea_1[i]
            new_genome_1.set_value(alea_1)
            new_genome_2.set_value(alea_2)
            #self.__genome[i], other.__genome[i] = other.__genome, self.__genome
##            new_genome_2[i].set_value(self.__genome[i])
##            new_genome_1[i]= other.__genome[i]
            
##        for i in range(position,self.get_size()):
##            new_genome_1.append(self.__genome[i])
##            new_genome_2.append(other.__genome[i])
        return (new_genome_1, new_genome_2)
        
    def evaluate(self, problem):
        """
        set the fitness score with the fitness computed by problem for self
        :param problem: problem(a Problem object) - the problem
        """
        pass 
    def get_score(self):
        """
        :rtype: number
        :return: the fitness score of self
        """
        return self.__fitness
    def get_size(self):
        """
        :rtype: number
        :return: the size of self's genome
        """
        
        return self.__size
    def get_value(self):
        """
        :return: the genome of self
        """
        return self.__genome
    def init_value(self):
        """
        randomly initialize the genome value of self
        """
        for i in range(self.get_size()):
            gene = (randint(0,100)%2)
            if gene==1:
                self.__fitness +=1     
            self.__genome.append(gene)
    def mutate(self, probability):
        """
        apply mutation operation to self : each element of the geome sequence is randomly changed with given probabiliy
        :param probability: (float) - the probability of mutate for every gene
        :UC: probability in [0,1[
        :side effect: self's genome is modified
        """
        assert 0< probability <1
        new_alea = self.get_value()
        for i in range(self.get_size()):
            if random() > probability:
                new_alea[i] = new_alea[i] ^ 1
        self.set_value(new_alea)
    def set_score(self,new_score):
        """
        change the fitness score of self
        :param new_score: (number) - the new fitness 
        """
        self.__fitness = new_score
    def set_value(self,new_value):
        """
    change the genome value of self
    :param new_score: (sequence) - the new genome 
        """
        self.__genome = new_value
    def calculate_N(self):
        """
        convert the genome symbol into a decimal base
        :return: an integer in base 10
        """
        integer = 0
        for i in range(self.get_size()):
            integer = integer + self.__genome[i]*2**(self.get_size()-(i+1))
        return integer
            
            
        
    
        
    