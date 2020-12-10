import numpy as np
import matplotlib.pyplot as plt
import random

class NodeLayer:
	def __init__(self, nb_nodes, nb_inputs):
		self.nb_nodes = nb_nodes
		self.nb_inputs = nb_inputs
		self.weights = np.random.uniform(low = -1, high = 1, size=(nb_inputs, nb_nodes))
		self.bias = np.random.normal(-1.0, 1.0, size=(1, nb_nodes))
		#print('\n {} \n'.format(self.weights))

class NeuralNetwork:
	def __init__(self, layer1, layer2, layer3):
		self.layer1 = layer1
		self.layer2 = layer2
		self.layer3 = layer3
	
	def sigmoid(self, x):
		return 1 / (1+np.exp(-x))
	
	def tanh(self, x):
		return np.tanh(x)
	
	def softmax(self,x):
		return (np.exp(x) / sum(np.exp(x)))
	
	def forward_pass(self, inputs):
		#Sum of dot product of each layer
		#Apply activation function to the layer sums
		
		z_layer_1 = np.dot(inputs, self.layer1.weights) + self.layer1.bias
		output_layer_1 = self.sigmoid(z_layer_1) 

		z_layer_2 = np.dot(output_layer_1, self.layer2.weights) + self.layer2.bias
		output_layer_2 = self.sigmoid(z_layer_2) 

		z_layer_3 = np.dot(output_layer_2, self.layer3.weights) + self.layer3.bias #z4
		output_layer_3 = self.sigmoid(z_layer_3) 
		
		return output_layer_3

	def process_output(self, output):
		possible_decisions = [(0,-1), (0,1), (1,0), (-1,0)] # [NORTH, SOUTH, EAST, WEST]
		softmaxed_output = self.softmax(output[0])
		softmaxed_output = softmaxed_output.tolist()
		decision = np.random.choice([0, 1, 2, 3], p=softmaxed_output)
		
		return possible_decisions[decision]

class GeneticPopulation:
	def __init__(self, population_size, nb_input_nodes, nb_layer1_nodes, nb_layer2_nodes, nb_output_nodes):
		self.population_size = population_size #nb of individual per generation
		self.nb_input_nodes  = nb_input_nodes
		self.nb_layer1_nodes = nb_layer1_nodes
		self.nb_layer2_nodes = nb_layer2_nodes
		self.nb_output_nodes = nb_output_nodes
		#self.genome = generate_population
	
	def generate_population(self):
		population_genome = [] #referencing all brains of the generation
		
		for i in range(self.population_size): 
			#random generation of brains consited of 1 input, 2 hidden and 1 output layer
			layer1 = NodeLayer(self.nb_layer1_nodes, self.nb_input_nodes)
			layer2 = NodeLayer(self.nb_layer2_nodes, self.nb_layer1_nodes)
			layer3 = NodeLayer(self.nb_output_nodes, self.nb_layer2_nodes)
			
			population_genome.append(NeuralNetwork(layer1, layer2, layer3))
		self.genome = population_genome
		return population_genome


class ChildrenNodeLayer:
	def __init__(self, weights, nb_nodes):
		self.weights = weights
		self.bias = np.random.normal(-1.0, 1.0, size=(1, nb_nodes))




class ChildrenGeneration:
	def __init__(self, mother, father, population_size, nb_layer1_nodes, nb_layer2_nodes, nb_output_nodes):
		self.mother = mother
		self.father = father
		self.population_size = population_size
		
		self.nb_layer1_nodes = nb_layer1_nodes
		self.nb_layer2_nodes = nb_layer2_nodes
		self.nb_output_nodes = nb_output_nodes
		
	def crossover(self, dad_layer, mother_layer, alpha): #takes mum and dad layer as input and returns list of child layer
		beta  = 1 - alpha
		weighted_mother_layer = np.dot(mother_layer, beta)
		weighted_father_layer = np.dot(dad_layer, alpha)
		kid = weighted_father_layer.__add__(weighted_mother_layer)

		return kid

		
	def generate_population(self):
		population_genome = []

		population_genome.append(self.mother)
		population_genome.append(self.father)

		for i in range(self.population_size - 2 ):
			alpha = random.random()

			layer1_weights = self.crossover(self.mother.layer1.weights, self.father.layer1.weights, alpha)
			layer2_weights = self.crossover(self.mother.layer2.weights, self.father.layer2.weights, alpha)
			layer3_weights = self.crossover(self.mother.layer3.weights, self.father.layer3.weights, alpha)

			layer1 = ChildrenNodeLayer(layer1_weights, self.nb_layer1_nodes)
			layer2 = ChildrenNodeLayer(layer2_weights, self.nb_layer2_nodes)
			layer3 = ChildrenNodeLayer(layer3_weights, self.nb_output_nodes)

			population_genome.append(NeuralNetwork(layer1, layer2, layer3))

		return population_genome
				




#https://towardsdatascience.com/artificial-neural-networks-optimization-using-genetic-algorithm-with-python-1fe8ed17733e
'''
def mat_to_vector(mat_pop_weights):
     pop_weights_vector = []
    
     for sol_idx in range(mat_pop_weights.shape[0]):
         curr_vector = []
         
         for layer_idx in range(mat_pop_weights.shape[1]):
             
             vector_weights = numpy.reshape(mat_pop_weights[sol_idx, layer_idx], newshape=(mat_pop_weights[sol_idx, layer_idx].size))
             curr_vector.extend(vector_weights)
         
         pop_weights_vector.append(curr_vector)
    
     return numpy.array(pop_weights_vector)



'''

















"""
	nb_input_nodes = 5
	
	nb_layer1_nodes = 5
	nb_layer2_nodes = 5
	
	nb_output_nodes = 3

	layer1 = NodeLayer(nb_layer1_node, nb_input_nodes)
	layer2 = NodeLayer(nb_layer2_node, nb_layer1_nodes)
	layer3 = NodeLayer(nb_output_node, nb_layer2_nodes)

	neural_network = NeuralNetwork(layer1, layer2, layer3)
	input_vector = [1.5, 3.0, 4.0, -1.0, -1.5]
	
	print('OUTPUT = {}'.format(neural_network.forward_pass(input_vector)))


"""

