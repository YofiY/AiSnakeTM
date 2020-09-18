import numpy as np
import matplotlib.pyplot as plt

class NodeLayer:
	def __init__(self, nb_nodes, nb_inputs):
		self.nb_nodes = nb_nodes
		self.nb_inputs = nb_inputs
		self.weights = np.random.uniform(low = -1, high = 1, size=(nb_inputs, nb_nodes))
		self.bias = np.random.normal(-1.0, 1.0, size=(1, nb_nodes))
		print('\n {} \n'.format(self.weights))

class NeuralNetwork():
	def __init__(self, l1, l2, l3):
		self.layer1 = l1
		self.layer2 = l2
		self.layer3 = l3

	def sigmoid(self, x):
		return 1 / (1+np.exp(-x))
	
	def tanh(self, x):
		return np.tanh(x)
	
	def forward_pass(self, inputs):
		#Sum of dot product of each layer
		#Apply activation function to the layer sums
		
		z_layer_1 = np.dot(inputs, self.layer1.weights) + self.layer1.bias
		output_layer_1 = self.sigmoid(z_layer_1) 

		z_layer_2 = np.dot(output_layer_1, self.layer2.weights) + self.layer2.bias
		output_layer_2 = self.sigmoid(z_layer_2) 

		z_layer_3 = np.dot(output_layer_2, self.layer3.weights) + self.layer3.bias #z4
		output_layer_3 = self.tanh(z_layer_3) 
		
		return output_layer_3

	def process_output(self, output):
		possible_decisions = [(0,-1), (0,1), (1,0), (-1,0)] # [NORTH, SOUTH, EAST, WEST]
		for i in range(len(output)):
			if output[i] == max(output):
				return possible_decisions[i]

class GeneticPopulation:
	

	def __init__(self, population_size, nb_input_nodes, nb_layer1_nodes, nb_layer2_nodes, nb_output_nodes):
		self.population_size = population_size #nb of individual per generation
		self.nb_input_nodes = nb_input_nodes
		self.nb_layer1_nodes = nb_layer1_nodes
		self.nb_layer2_nodes = nb_layer2_nodes
		self.nb_output_nodes = nb_output_nodes
	
	def generate_population(self, population_size):
		generation = [] #referencing all brains of the generation
		
		for i in range(population_size): 
			layer1 = NodeLayer(self.nb_layer1_nodes, self.nb_input_nodes)
			layer2 = NodeLayer(self.nb_layer2_nodes, self.nb_layer1_nodes)
			layer3 = NodeLayer(self.nb_output_nodes, self.nb_layer2_nodes)
			
			generation.append(NeuralNetwork(layer1, layer2, layer3))

		
		
		return generation
	
	def evaluate_fitness(self, score_list, generation):
		parent_genes =[]
		while len(parent_genes) != 2:
			for i in range(len(score_list)):
				if score_list[i] == max(score_list):
					parent_genes.append(generation[i])
					score_list[i].remove(score_list[i])



		

	def cross_over(self):
		pass
	
	def mutate(self):
		pass






















	"""nb_input_nodes = 5
	
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

