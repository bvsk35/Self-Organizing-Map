# This file Loads the Training Images and Labels
# Loads Test Images and Labels
# Generate/Initialize Weight Matrix using Xavier Initialisation

# Import required functions
import gzip
import numpy

# Functions
# def load_training_images(filename):
#     with gzip.open(filename) as f:
#         a = numpy.frombuffer(f.read(), dtype=numpy.uint8, offset=16).reshape(-1, 784)
#         return a

# def load_training_labels(filename):
#     with gzip.open(filename) as f:
#         a = numpy.frombuffer(f.read(), dtype=numpy.uint8, offset=8)
#         return a

# def load_test_images(filename):
#     with gzip.open(filename) as f:
#         a = numpy.frombuffer(f.read(), dtype=numpy.uint8, offset=16).reshape(-1, 784)
#         return a

# def load_test_labels(filename):
#     with gzip.open(filename) as f:
#         a = numpy.frombuffer(f.read(), dtype=numpy.uint8, offset=8)
#         return a

# Function for loading images and labels can be clubed into one function
def load_images(filename):
    with gzip.open(filename) as f:
        a = numpy.frombuffer(f.read(), dtype=numpy.uint8, offset=16).reshape(-1, 784)
        return a

def load_labels(filename):
    with gzip.open(filename) as f:
        a = numpy.frombuffer(f.read(), dtype=numpy.uint8, offset=8)
        return a

def InitialWeights():
    W_Layer_2 = numpy.random.normal(0, 0.050507, size=(40, 785))
    W_Layer_3 = numpy.random.normal(0, 0.44721, size=(10, 41))
    return W_Layer_2, W_Layer_3
