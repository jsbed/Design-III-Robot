from queue import PriorityQueue
from Robot.path_finding.point import Point


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
                next_node = Point(x1 + 1, y1 + 1)
            elif (y2 - y1 < 0):
                next_node = Point(x1 + 1, y1 - 1)
            else:
                next_node = Point(x1 + 1, y1)
        elif (x2 - x1 < 0):
            if (y2 - y1 > 0):
                next_node = Point(x1 - 1, y1 + 1)
            elif (y2 - y1 < 0):
                next_node = Point(x1 - 1, y1 - 1)
            else:
                next_node = Point(x1 - 1, y1)
        else:
            if (y2 - y1 > 0):
                next_node = Point(x1, y1 + 1)
            elif (y2 - y1 < 0):
                next_node = Point(x1, y1 - 1)
            else:
                next_node = Point(x1, y1)
        return next_node

    def get_point_where_path_change_direction(self, path):
        if (int(len(path)) <= 2):
            return 0
        (x1, y1) = path[0]
        (x2, y2) = path[1]
        (x3, y3) = path[2]
        if ((x2 - x1 != x3 - x2) or (y2 - y1 != y3 - y2)):
            return path[1]
        else:
            return self.get_point_where_path_change_direction(path[1:])

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
