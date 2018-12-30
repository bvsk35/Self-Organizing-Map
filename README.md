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

Ability of SOM to visualize high-dimensional data by creating low-dimensional has been used here. There are two fundamentally different ways of visualizing a self-organizing feature map. In one method of visualization, the feature map is viewed as an elastic net, with the synaptic-weight vectors treated as pointers for the respective neurons, which are directed into the input space. This method of visualization is particularly useful for displaying the topological-ordering property of the SOM algorithm (as illustrated by the results of the computer simulation experiments presented in Section 9.5 Ch 9 of S.Haykin textbook). 
In the second method of visualization, class labels are assigned to neurons in a two-dimensional lattice (representing the output layer of the network), depending on how each test pattern (not seen before) excites a particular neuron in the self-organized network. As a result of this second stage of stimulation, the neurons in the two-dimensional lattice are partitioned into a number of coherent regions, coherent in the sense that each grouping of neurons represents a distinct set of contiguous symbols or labels (Ritter, 2003).This method assumes that the right conditions have been followed for the development of a well-ordered feature map in the first place.

1 - In colour palette problem 3D RGB data has been used to train a neural network and create map in which particular area responds most to one set of inputs. And that input is placed on that neuron and this is repeated on all inputs to generate the entire map. If the number of neurons are more than the inputs then in map there can be some neurons which are not associated to any input. We find which input fires the neuron the most and it is placed over there. This is know as contextual map. Contextual maps come under second method of visualizations. 

2 - In MNIST dataset problem 784D data in similar fashion as above has been mapped to 2D map (i.e. contextual map). And colour label has been given to each digit label which helps in plotting.

Results for colour paletter and MNIST dataset has been posted. SOM and PCA helps in dimensional reduction which can be further used to develop a classifier using algorithms like K-Means, Deep Layer Nerual Networks etc. 

For further information refer: the code for Color Palette, S.Haykin "Neural Networks and Learning Machines" textbook and https://en.wikipedia.org/wiki/Self-organizing_map. 
