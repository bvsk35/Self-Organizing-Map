# Self-Organizing-Map
Keywords: SOM, Color-Palette, MNIST Dataset

### Gist
This repo contains implementation of Self Organizing Map (SOM) also know as Kohonen map or network. A self-organizing map (SOM) 
self-organizing feature map (SOFM) is a type of artificial neural network (ANN) that is trained using unsupervised learning to produce 
a low-dimensional (typically two-dimensional), discretized representation of the input space of the training samples, called a map, 
and is therefore a method to do dimensionality reduction. Self-organizing maps differ from other artificial neural networks as 
they apply competitive learning as opposed to error-correction learning (such as backpropagation with gradient descent), 
and in the sense that they use a neighborhood function to preserve the topological properties of the input space. This 
makes SOMs useful for visualization by creating low-dimensional views of high-dimensional data, akin to multidimensional scaling.

Ability of SOM to visualize high-dimensional data by creating low-dimensional has been used here.
1 - In colour palette problem 3D RGB data has been used to train a neural network and create map in which particular area responds most to one set of input. And that input is placed on that neuron. 

2 - In MNIST dataset problem 784D data in similar fashion as above has been mapped to 2D map. And colour label has been given to each digit label which helps in plotting. 

Results for colour paletter and MNIST dataset has been posted. SOM and PCA helps in dimensional reduction which can be further used to develop a classifier using algorithms like K-Means, Nerual Networks etc. 

For further information refer: https://en.wikipedia.org/wiki/Self-organizing_map and the code for Color Palette. 
