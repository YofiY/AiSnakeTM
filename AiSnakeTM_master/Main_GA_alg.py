import numpy as np
import sys
from pygame.locals  import *
import pygame
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


def generate_input(snake, food_position):
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


def let_generation_play(generation, snake, food_position, population_size,):
	scores = []

	for i in range(len(generation)):	
		while snake.state != 'dead':
			graphics.initiateGraphics()

			inputs = generate_input(snake, food_position)
				
			output = generation[i].forward_pass(inputs)
			processed_output = generation[i].process_output(output[i])
			
			snake.chooseDirection(processed_output)
			snake.move()
			
			#for each iteration  we check if the snake and the food collided
			food.isEaten(snake,food)
			graphics.updateGraphics(snake, food, fpsClock, fps)

		scores.append(snake.length)
	return scores






if __name__ == '__main__':

	fpsClock = pygame.time.Clock()
	fps = const.FPS

	graphics.initiateGraphics()

	#initiate the objects
	snake = snake_object.Snake('Naive1.2-ng')
	food = food.Food() 

	#The number of trials is taken as command line arguments 
	#max_trials = int(sys.argv[1])

	#set out the neural structure 1 input, 2 hidden, 1 output layer
	nb_input_nodes = 6
	nb_layer1_nodes = 10
	nb_layer2_nodes = 10
	
	nb_output_nodes = 4

	population_size = 10

	#Main Loop

	population = GA.GeneticPopulation(population_size, nb_input_nodes, nb_layer1_nodes, nb_layer2_nodes, nb_output_nodes,)
	generation = population.generate_population(population_size)
	
	parent_score = let_generation_play(generation, snake, food.position, population_size)

	print('Parent_score = {}'.format(parent_score))
		
	#for each iteration  we check if the snake and the food collided
	food.isEaten(snake,food)

	#print('{} trials completed'.format(max_trials))
	sys.exit()
