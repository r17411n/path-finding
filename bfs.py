"""Breadth First Search Algorithm"
class BreadthFirstSearch(object):

  def __init__(self, start, finish, rooms):
    self.start = start
    self.finish = finish
    self.rooms = json.load(rooms)
    self.visited = list[]
    
  def bfs_calc(self):
    #find old mover from 2020 and paste the algorithm i made then here
    pass

  def populate_map(self):
    #need to think on how to crawl through the world and save current room as key and adjacent rooms as values in a list
    pass

  def blocked_path(self, room_num: int): -> bool
    if room_num is 0:
      return True
    else:
      return False

  def save_calculated_path(self, path, target_name)
    calculated_paths = dict()
    calculated_paths += (f"target_name", [path])
    
