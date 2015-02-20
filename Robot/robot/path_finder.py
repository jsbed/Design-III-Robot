from queue import PriorityQueue


class PathFinder():
    def __init__(self):
        self._frontier = PriorityQueue()
        self._came_from = {}
        self._cost_so_far = {}
        self._path = []

    def heuristic(self, a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def reconstruct_path(self, came_from, start, goal):
        current = goal
        self._path = [current]
        while current != start:
            current = came_from[current]
            self._path.append(current)
        return self._path

    def a_star_search(self, grid, start, goal):
        self._frontier.put(start, 0)
        self._came_from[start] = None
        self._cost_so_far[start] = 0

        while not self._frontier.empty():
            current = self._frontier.get()

            if current == goal:
                break

            for next_node in grid.neighbors(current):
                new_cost = self._cost_so_far[current] + 1
                if next_node not in self._cost_so_far or new_cost \
                        < self._cost_so_far[next_node]:
                    self._cost_so_far[next_node] = new_cost
                    priority = new_cost + self.heuristic(goal, next_node)
                    self._frontier.put(next_node, priority)
                    self._came_from[next_node] = current

        return self.reconstruct_path(self._came_from, start, goal)
