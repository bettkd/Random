#! /usr/bin/python

# Run with <python 8puzzle.py -i> to input your puzzle on the commandline
# Otherwise random puzzle is generated

from heapq import heappush, heappop
from random import shuffle
import time
import sys
 
class Solver:
  def __init__(self, initial_state=None):
    self.initial_state = State(initial_state)
    self.goal = range(1, 9)
 
  def _rebuildPath(self, end):
    path = [end]
    state = end.parent
    while state.parent:
      path.append(state)
      state = state.parent
    return path
 
  def solve(self):
    openset = PriorityQueue()
    openset.add(self.initial_state)
    closed = set()
    moves = 0
    print 'Trying to solve:'
    print openset.peek(), '\n\n'
    start = time.time()
    while openset:
      current = openset.poll()
      if current.values[:-1] == self.goal:
        end = time.time()
        print 'Solution found.'
        path = self._rebuildPath(current)
        for state in reversed(path):
          print state
          print
        print 'Finished in %d moves' % len(path)
        print 'Solution found in %2.f seconds' % float(end - start)
        break
      moves += 1
      for state in current.possible_moves(moves):
        if state not in closed:
          openset.add(state)
      closed.add(current)
    else:
      print 'Solution could not be found!'
 

class State:
  def __init__(self, values, moves=0, parent=None):
    self.values = values
    self.moves = moves
    self.parent = parent
    self.goal = range(1, 9)
  
  #Move Up, Right, Left or Down
  def possible_moves(self, moves):
    i = self.values.index(0)
    if i in [3, 4, 5, 6, 7, 8]:
      new_board = self.values[:]
      new_board[i], new_board[i - 3] = new_board[i - 3], new_board[i]
      yield State(new_board, moves, self)
    if i in [1, 2, 4, 5, 7, 8]:
      new_board = self.values[:]
      new_board[i], new_board[i - 1] = new_board[i - 1], new_board[i]
      yield State(new_board, moves, self)
    if i in [0, 1, 3, 4, 6, 7]:
      new_board = self.values[:]
      new_board[i], new_board[i + 1] = new_board[i + 1], new_board[i]
      yield State(new_board, moves, self)
    if i in [0, 1, 2, 3, 4, 5]:
      new_board = self.values[:]
      new_board[i], new_board[i + 3] = new_board[i + 3], new_board[i]
      yield State(new_board, moves, self)
 
  #A Star Search = Heuristic + Cost (Manhattan heuristic)
  def score(self):
    return self._h() + self._g()
 
  def _h(self):
    return sum([1 if self.values[i] != self.goal[i] else 0 for i in xrange(8)])
 
  def _g(self):
    return self.moves
 
  def __cmp__(self, other):
    return self.values == other.values
 
  def __eq__(self, other):
    return self.__cmp__(other)
 
  def __hash__(self):
    return hash(str(self.values))
 
  def __lt__(self, other):
    return self.score() < other.score()
 
  def __str__(self):
    return '\n'.join([str(self.values[:3]),
        str(self.values[3:6]),
        str(self.values[6:9])]).replace('[', '').replace(']', '').replace(',', '').replace('0', 'x')
 
class PriorityQueue:
  def __init__(self):
    self.pq = []
 
  def add(self, item):
    heappush(self.pq, item)
 
  def poll(self):
    return heappop(self.pq)
 
  def peek(self):
    return self.pq[0]
 
  def remove(self, item):
    value = self.pq.remove(item)
    heapify(self.pq)
    return value is not None
 
  def __len__(self):
    return len(self.pq)
 
# Option -i alows interactive input
def main(argv):
  if len(argv) == 1:
    puzzle = range(9)
    shuffle(puzzle)
  elif argv[1] == '-i':
    print 'Enter the puzzle sepatated by space:'
    str_arr = raw_input().split(' ') #will take in a string of numbers separated by a space
    puzzle = [int(num) for num in str_arr]
  
  #
  solver = Solver(puzzle)
  solver.solve()

if __name__ == '__main__':
  main(sys.argv)