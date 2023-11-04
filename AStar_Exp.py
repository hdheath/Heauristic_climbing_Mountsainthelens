class AStarExp(AIModule):

  def heuristic(self, v, v_height, end, end_height):
    
    chebychev = max(abs(end.x - v.x), abs(end.y - v.y), abs(end_height-v_height))
		
    if end_height > v_height :
      return (math.e) * (end_height - v_height) 
		
    if end_height < v_height :
      return math.pow(math.e,(end_height - v_height)/chebychev) * (chebychev) 
		
    if end_height == v_height :
      return 0
	
  def createPath(self, map_):
    
    q = PriorityQueue()
    cost = {}
    prev = {}
    explored = {}
		# Dictionary initialization
    for i in range(map_.width):
      for j in range(map_.length):
        cost[(i,j)] = math.inf
        prev[(i,j)] = None
        explored[(i,j)] = False
    current_point = deepcopy(map_.start)
    # set a variable equal to the end goal location
    end = map_.getEndPoint() 
    current_point.comparator = 0
    cost[(current_point.x, current_point.y)] = 0
		# Add start node to the queue
    q.put(current_point)
		# Search loop
    while q.qsize() > 0:
			# Get new point from PQ
      v = q.get()
      explored[(v.x,v.y)] = True
			# Check if popping off goal
      if v == map_.getEndPoint():
        break
			# Evaluate neighbors
      neighbors = map_.getNeighbors(v)
      for neighbor in neighbors:
        alt = map_.getCost(v, neighbor) + cost[(v.x,v.y)]
        if alt < cost[(neighbor.x,neighbor.y)]:
          cost[(neighbor.x,neighbor.y)] = alt 
          end_height = map_.getTile(end.x,end.y)
          v_height = map_.getTile(v.x,v.y)
          neighbor.comparator = alt + self.heuristic(v, v_height, end, end_height)
          prev[(neighbor.x,neighbor.y)] = v
        q.put(neighbor)
		
    # Find and return path
    path = []
    while v != map_.getStartPoint():
      path.append(v)
      v = prev[(v.x,v.y)]
    path.append(map_.getStartPoint())
    path.reverse()
    return path
