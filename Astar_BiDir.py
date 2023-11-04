# Attempt at Bi-directional Search
#class AStarMSH(AIModule):
  
  def heuristicGoingUp(self, v, v_height, end, end_height):
    chebychev = max(abs(end.x - v.x), abs(end.y - v.y))
    if end_height > v_height :
      return (math.e) * (end_height - v_height) 
    if end_height < v_height :
      return math.pow(math.e,(end_height - v_height)/chebychev) * (chebychev)
    if end_height == v_height :
      return chebychev

  def heuristicGoingDown(self, w, w_height, start, start_height):
    chebychev = max(abs(start.x - w.x), abs(start.y - w.y))
    if start_height > w_height :
      return ((math.e) * ( w_height - start_height)) 
    if start_height < w_height :
      return math.pow(math.e,(w_height - start_height)/chebychev) * (chebychev) 
    if start_height == w_height :
      return chebychev
  
  def createPath(self, map_):
    q_start = PriorityQueue()
    q_end = PriorityQueue()
    cost_start = {}
    cost_end = {}
    prev_start = {}
    prev_end = {}
    explored_start = {}
    explored_end = {}
    
    for i in range(map_.width):
      for j in range(map_.length):
        cost_start[(i,j)] = math.inf
        cost_end[(i,j)] = math.inf
        prev_start[(i,j)] = None
        prev_end[(i,j)] = None
        explored_start[(i,j)] = False
        explored_end[(i,j)] = False
    
    start = map_.getStartPoint()
    end = map_.getEndPoint() 
    
    start.comparator = 0
    cost_start[(start.x, start.y)] = 0
    q_start.put(map_.getStartPoint())
    
    end.comparator = 0
    cost_end[(end.x, end.y)] = 0
    q_end.put(map_.getEndPoint())
    
    while q_start.qsize() > 0 and q_end.qsize() > 0:
      if (q_start.qsize()) > (q_end.qsize()):
        w = q_end.get()
        explored_end[(w.x, w.y)] = True
        if (w.x , w.y) in explored_start:
          break
        neighbors = map_.getNeighbors(w)
        for neighbor in neighbors:
          alt = cost_end[(w.x, w.y)] + map_.getCost(w, neighbor)
          if alt < cost_end[(neighbor.x, neighbor.y)]:
            cost_end[(neighbor.x, neighbor.y)] = alt
            start_height = map_.getTile(start.x, start.y)
            w_height = map_.getTile(w.x, w.y)
            neighbor.comparator = alt + self.heuristicGoingDown(w, w_height, start, start_height)
            prev_end[(neighbor.x, neighbor.y)] = w
          q_end.put(neighbor)
      else:
        v = q_start.get()
        explored_start[(v.x, v.y)] = True
        if (v.x , v.y) in explored_end:
          break
        neighbors2 = map_.getNeighbors(v)
        for neighbor2 in neighbors2:
          alt2 = cost_start[(v.x, v.y)] + map_.getCost(v, neighbor2)
          if alt2 < cost_start[(neighbor2.x, neighbor2.y)]:
            cost_start[(neighbor2.x, neighbor2.y)] = alt2
            end_height = map_.getTile(end.x, end.y)
            v_height = map_.getTile(v.x, v.y)
            neighbor.comparator2 = alt2 + self.heuristicGoingUp(v, v_height, end, end_height)
            prev_start[(neighbor2.x, neighbor2.y)] = v
          q_start.put(neighbor2)

    # Find and return path
    path = []
    path2 = []
    
    while v != map_.getStartPoint():
      path.append(v)
      v = prev_start[(v.x,v.y)]

    path.append(map_.getStartPoint())
    
    while w != map_.getEndPoint():
      path2.append(w)
      w = prev_end[(w.x,w.y)]

    path2.append(map_.getEndPoint())
    path.reverse()
    final_path = path + path2

    return final_path
