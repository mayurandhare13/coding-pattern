This is how we can implement this algorithm:
time complexity O(V+E)

## Initialization
- We will store the graph in Adjacency Lists, which means each parent vertex will have a list containing all of its children. <br>
- We will do this using a HashMap where the ‘key’ will be the parent vertex number and the value will be a List containing children vertices. <br>
- To find the sources, we will keep a HashMap to count the in-degrees i.e., count of incoming edges of each vertex. Any vertex with ‘0’ in-degree will be a source.

## Build the graph and find in-degrees of all vertices
We will build the graph from the input and populate the in-degrees HashMap.

## Find all sources
All vertices with ‘0’ in-degrees will be our sources and we will store them in a Queue.

## Sort
For each source, do the following things:
  - Add it to the sorted list.
  - Get all of its children from the graph.
  - Decrement the in-degree of each child by 1.
  - If a child’s in-degree becomes ‘0’, add it to the sources Queue.
  - Repeat step 1, until the source Queue is empty.