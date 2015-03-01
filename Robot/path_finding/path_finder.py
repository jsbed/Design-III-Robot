from queue import PriorityQueue
from collections.__main__ import Point


class PathFinder():
    def __init__(self):
        self._frontier = PriorityQueue()
        self._came_from = {}
        self._path = []

    def reconstruct_path(self, came_from, start, goal):
        current = goal
        self._path = [current]
        while current != start:
            current = came_from[current]
            self._path.append(current)
        return self._path

    def get_next_node(self, current, goal):
        (x1, y1) = current
        (x2, y2) = goal
        next_node = current
        if (x2 - x1 > 0):
            if (y2 - y1 > 0):
                next_node = Point(x1+1, y1+1)
            elif (y2 - y1 < 0):
                next_node = Point(x1+1, y1-1)
            else:
                next_node = Point(x1+1, y1)
        elif (x2 - x1 < 0):
            if (y2 - y1 > 0):
                next_node = Point(x1-1, y1+1)
            elif (y2 - y1 < 0):
                next_node = Point(x1-1, y1-1)
            else:
                next_node = Point(x1-1, y1)
        else:
            if (y2 - y1 > 0):
                next_node = Point(x1, y1+1)
            elif (y2 - y1 < 0):
                next_node = Point(x1, y1-1)
            else:
                next_node = Point(x1, y1)
        return next_node

    def find_path(self, start, goal):
        self._frontier.put(start, 0)
        self._came_from[start] = None

        while not self._frontier.empty():
            current = self._frontier.get()

            if (current == goal):
                break

            next_node = self.get_next_node(current, goal)
            self._frontier.put(next_node, 0)
            self._came_from[next_node] = current

        return self.reconstruct_path(self._came_from, start, goal)
