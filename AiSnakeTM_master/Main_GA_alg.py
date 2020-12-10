import numpy as np
import sys
from pygame.locals  import *
import pygame
import matplotlib.pylab as plt 
from random import random 
from modules import constants as const
from modules import food
from modules import snake_object
from modules import naiveAlgorithm as NA
from modules import genetic_algorithm as GA
from modules import graphics

 


def calc_next_head_position(head_position, direction):
	x, y = direction 
	next_head_position = (((head_position[0]+(x*const.GRID)) % const.WIDTH), (head_position[1] + (y*const.GRID)) % const.HEIGHT )
	return next_head_position

def deltax_deltay(head_position, food_position):
	delta_x = (food_position[0] - head_position[0]) / const.WIDTH
	delta_y = (food_position[1] - head_position[1]) / const.HEIGHT

	return delta_x, delta_y


def generate_inputs(snake, food_position):
	#MOVES_LIST = [UP, DOWN, LEFT, RIGHT]

	generated_input = []
	
	for a, b in const.MOVES_LIST:
		if calc_next_head_position(snake.positions[0], (a, b)) in snake.positions:
			generated_input.append(0)
		else:
			generated_input.append(1)
	
	delta_x, delta_y = deltax_deltay(snake.positions[0], food_position)
	
	generated_input.append(delta_x)
	generated_input.append(delta_y)
	#print('GENERATED INPUT = {}'.format(generated_input))
	return generated_input

def get_output(inputs, neuralNet):
	output = neuralNet.forward_pass(inputs)
	#print('OUTPUT LAYER PRE-SOFTMAX = {}'.format(output))
	processed_output = neuralNet.process_output(output)

	return processed_output

def softmax(x):
		return (np.exp(x) / sum(np.exp(x)))

def get_brain(NeuralNet):
	brain = [[], [], []]

	brain[0] = NeuralNet.layer1.weights
	brain[1] = NeuralNet.layer2.weights
	brain[2] = NeuralNet.layer3.weights

	brain = np.asarray(brain, dtype=np.float32)
	return brain

def generate_food_list(population_size):
	food_list = []
	for i in range(population_size):
		food_list.append(food.Food())
	return food_list

def generate_snake_list(population_size):
	snake_list =[]
	for i in range(population_size):
		snake_list.append(snake_object.Snake('genetic_alg.xml'))
	return snake_list


def train(nb_generations):

	nb_input_nodes = 6
	nb_layer1_nodes = 6
	nb_layer2_nodes = 6
	
	nb_output_nodes = 4

	population_size = 10

	performance = []
	
	for current_generation in range(nb_generations):
		
		if current_generation == 0:

			#print('generation {}'.format(current_generation))

			#Initialization
			population = GA.GeneticPopulation(population_size, nb_input_nodes, nb_layer1_nodes, nb_layer2_nodes, nb_output_nodes)
			population_genome = population.generate_population()

			snake_list = generate_snake_list(population_size)
			food_list = generate_food_list(population_size)

		 	#fitness assignement 
			score_list = fitness(snake_list, food_list, population_genome)
			#print(score_list)
			performance.append(score_list)

		 	#selection
			parents_index = selection(score_list)
			
			mother = population_genome[parents_index[0]]
			father = population_genome[parents_index[1]]
			print('best: {} {}'.format(parents_index[0], parents_index[1]))

			
		 	#crossover
			population = GA.ChildrenGeneration(mother, father, population_size, nb_layer1_nodes, nb_layer2_nodes, nb_output_nodes)
			population_genome = population.generate_population()

		else:
			#print('generation {}'.format(current_generation))

			snake_list = generate_snake_list(population_size)
			food_list = generate_food_list(population_size)

		 	#fitness assignement 
			score_list = fitness(snake_list, food_list, population_genome)
			print(score_list)
			performance.append(score_list)

		 	#selection
			parents_index = selection(score_list)
			
			mother = population_genome[parents_index[0]]
			father = population_genome[parents_index[1]]

			
		 	#crossover
			population = GA.ChildrenGeneration(mother, father, population_size, nb_layer1_nodes, nb_layer2_nodes, nb_output_nodes)
			population_genome = population.generate_population()


	return performance


				

def fitness(snake, food, population_genome):
	
	score_list = np.array([])
	#fpsClock = pygame.time.Clock()
	#fps = const.FPS

	for i in range(len(snake)):
		while snake[i].state == 'alive':
				
			inputs = generate_inputs(snake[i], food[i].position)
			output = get_output(inputs, population_genome[i])

			#graphics.initiateGraphics()
				
			snake[i].move()

			food[i].isEaten(snake[i], food[i])
			snake[i].chooseDirection(output)

			#graphics.updateGraphics(snake[i], food[i], fpsClock, fps)
			
		
		score_list = np.append(score_list, snake[i].score)

	return score_list


def selection(score_list):
	return np.argpartition(score_list, -4)[-4:]



def crossover(dad_Array, mum_Array, n):
	new_generation = np.zeros((population_size, 3))
	
	#keep a copy of mother and father genes
	new_generation.append(dad_Array)
	new_generation.append(mum_Array)

	for i in range(n-2): 
		alpha = random()
		beta  = 1 - alpha

		mum_genes = np.dot(mum_Array, beta)
		dad_genes = np.dot(dad_Array, alpha)
		kid = dad_genes.__add__(mum_genes)
		new_generation.append(kid)
		print('alpha = {} beta = {}'.format(alpha, beta))
		
		
	return new_generation 

if __name__ == "__main__":
	performance = train(6)
	








			


