import numpy as np

class DBSCAN:
  
  def __init__(self, epsilon, min_points):
    self.epsilon = epsilon
    self.min_points = min_points
    self.visited = set ()
  
  def fit (self, data):
    self.data = data 
    self.clusters = []
    for point in self.data:
      if point not in self.visited:
        self.visited. add (point)
        neighbors = self.range_query (point)
        
        if len (neighbors) < self.min_points:
          continue
    
        cluster = self.expand_cluster (point, neighbors)
        self.clusters.append(cluster)
    return self.clusters
  
  def range_query (self, point):
    neighbors = []
    for q in self.data:
      if np.linalg.norm(point - q) <= self.epsilon:
        neighbors.append(q)
    return neighbors
  
  def expand_cluster (self, point, neighbors):
    cluster = [point]
    
    for neighbor in neighbors:
      
      if neighbor not in self.visited:
        self.visited.add(neighbor)
        new_neighbors = self.range_query(neighbor)
        
        if len(new_neighbors) >= self.min_points: 
          neighbors.extend(new_neighbors)
        
      if neighbor not in [p for c in self.clusters for p in c]:
        cluster.append(neighbor)
    
    return cluster