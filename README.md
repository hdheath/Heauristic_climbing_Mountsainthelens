# Heuristic Pathfinding for Mount St. Helens

This repository contains implementations of heuristic-based pathfinding algorithms to tackle the classic problem of climbing Mount St. Helens using A* search variants in an artificial intelligence class.

## Algorithms

### AStarExp
The `AStarExp` module uses an exponential heuristic that accounts for the elevation change. It amplifies the cost exponentially when climbing and uses a reduction factor based on the Chebyshev distance when descending.

### AStarDiv
The `AStarDiv` module simplifies the heuristic to a Chebyshev distance, factoring in the difference in height between the current point and the goal, scaled by the cost so far (`alt`).

### AStarMSH
The `AStarMSH` module provides a more dynamic heuristic by modifying the `heuristic` method to penalize elevation changes using the mathematical constant `e`. It aims to optimize the path based on both distance and elevation change, with an additional scaling factor of `1.15`.

## 2 types of AStar 

AStarMSH Heuristic (Bi directional)
heuristicGoingUp: Uses a modified Chebyshev distance for elevation and applies an exponential penalty if the goal is at a higher elevation than the current point.
heuristicGoingDown: Applies a penalty when descending and scales the penalty based on the Chebyshev distance and the difference in elevation.
This snippet implies the implementation of a bi-directional A* search where two priority queues are managed, and paths are built from both the start and the end points until they meet.

AStarMSH Heuristic (Undirectional)
The heuristic method in the second code snippet simplifies the evaluation and does not distinguish between going up or down. It applies a penalty based on the elevation difference using the constant e and the Chebyshev distance.
The second snippet appears to be a unidirectional A* search as it does not implement the bi-directional logic seen in the first code snippet.
The heuristic in this version also includes a scaling factor of 1.15 when calculating the comparator for the neighbors.

Summary of Differences
Bi-directional vs. Unidirectional Search: The first snippet introduces a bi-directional search approach, whereas the second snippet is a traditional unidirectional A* search.
Heuristic Complexity: The first snippet uses two separate heuristic functions depending on whether the algorithm is currently evaluating paths leading away from the start or toward it. The second snippet uses a single heuristic function regardless of direction.
Scaling Factor: Only the second snippet includes an additional scaling factor of 1.15

## Usage

Each module can be used as a plug-and-play component for any system that requires heuristic pathfinding capabilities over a two-dimensional terrain with varying elevation, such as geographic information systems (GIS), games, or simulation environments.

To use an algorithm module:

1. Instantiate the module.
2. Call the `createPath` method with the map object.
3. The `createPath` method returns the computed path from the start to the goal.

Example:

```python
map_ = YourMapClass()  # Your map initialization
astar = AStarExp()  # Replace with AStarDiv or AStarMSH as needed
path = astar.createPath(map_)
```

## Map Representation 
The map is assumed to be represented by a class providing the following methods:

getCost(x, y): Returns the cost of moving to the specified tile.
getNeighbors(x, y): Returns a list of neighboring tiles to the specified tile.
getStartPoint(): Returns the starting point of the map.
getEndPoint(): Returns the goal/end point of the map.

## Dependencies
The implementations require the PriorityQueue class from the queue module and the math module for mathematical functions.

## Author 
Harrison Heath 
