import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Neural network class
class SimpleNeuralNetwork:
    def __init__(self):
        # Initialize weights with random values
        np.random.seed(1)
        self.weights1 = np.random.rand(3, 4)  # Input layer to hidden layer
        self.weights2 = np.random.rand(4, 1)  # Hidden layer to output layer

    # Feedforward function to predict output
    def feedforward(self, inputs):
        self.layer1 = sigmoid(np.dot(inputs, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))
        return self.output

    # Backpropagation function to train the network
    def backpropagation(self, inputs, target, learning_rate):
        output_error = target - self.output
        d_output = output_error * sigmoid_derivative(self.output)

        layer1_error = d_output.dot(self.weights2.T)
        d_layer1 = layer1_error * sigmoid_derivative(self.layer1)

        # Update weights
        self.weights2 += self.layer1.T.dot(d_output) * learning_rate
        self.weights1 += inputs.T.dot(d_layer1) * learning_rate

    # Training function
    def train(self, inputs, targets, iterations, learning_rate):
        for i in range(iterations):
            self.feedforward(inputs)
            self.backpropagation(inputs, targets, learning_rate)

# Example usage
nn = SimpleNeuralNetwork()
X = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])  # Training features
y = np.array([[0], [1]])  # Target output
nn.train(X, y, iterations=10000, learning_rate=0.1)

# Testing
test_input = np.array([0.4, 0.5, 0.6])
prediction = nn.feedforward(test_input)
print("Predicted output:", prediction) 
