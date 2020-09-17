import numpy as np
import matplotlib.pyplot as plt

class NodeLayer():
	def __init__(self, nb_nodes, nb_inputs):
		self.nb_nodes = nb_nodes
		self.nb_inputs = nb_inputs
		self.weights = np.random.uniform(low = -1, high = 1, size=(nb_inputs, nb_nodes))


class NeuralNet():
	def __init__(self, l1, l2, l3):
		self.layer1 = l1
		self.layer2 = l2
		self.layer3 = l3

	def sigmoid(self, x):
		return 1 / (1+np.exp(-x))

	def forward_pass(self, inputs):
		#Sum of dot product of each layer
		#Apply activation function to the layer sums
		
		z_layer_1 = np.dot(inputs, self.layer1.weights) + self.layer1.bias
		output_layer_1 = self.sigmoid(z_layer_1) #activation(1)

		z_layer_2 = np.dot(output_layer_1, self.layer2.weights) + self.layer2.bias
		output_layer_2 = self.sigmoid(z_layer_2) #activation(2)

		z_layer_3 = np.dot(output_layer_2, self.layer3.weights) + self.layer3.bias #z4
		output_layer_3 = self.sigmoid(z_layer_3) #y_Hat
		
		return output_layer_1, output_layer_2, output_layer_3

if __name__ = "__main__":

	nb_input_nodes = 4
	nb_layer1_node =
	nb_layer2_node =
	nb_output_node =

