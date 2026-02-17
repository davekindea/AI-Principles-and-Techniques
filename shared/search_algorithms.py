"""
Unified search algorithms: BFS, DFS, UCS, A*, and Minimax.
- Graph (adjacency list): used by BFS, DFS, Minimax.
- Graph with costs: used by UCS and A*.
"""

from collections import deque
import heapq


# ---------------------------------------------------------------------------
# BFS - Breadth-First Search (uninformed)
# ---------------------------------------------------------------------------

def breadth_first_search(graph, initial_state, goal_state):
    """
    Breadth-First Search on an adjacency-list graph.

    Args:
        graph: dict {node: [neighbors]}
        initial_state: start node
        goal_state: target node

    Returns:
        tuple: (path, nodes_explored) or (None, nodes_explored)
    """
    if initial_state == goal_state:
        return [initial_state], [initial_state]
    queue = deque([(initial_state, [initial_state])])
    visited = {initial_state}
    nodes_explored = [initial_state]
    while queue:
        node, path = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor == goal_state:
                return path + [neighbor], nodes_explored + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                nodes_explored.append(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None, nodes_explored


# ---------------------------------------------------------------------------
# DFS - Depth-First Search (uninformed)
# ---------------------------------------------------------------------------

def depth_first_search(graph, initial_state, goal_state):
    """
    Depth-First Search on an adjacency-list graph.

    Args:
        graph: dict {node: [neighbors]}
        initial_state: start node
        goal_state: target node

    Returns:
        tuple: (path, nodes_explored) or (None, nodes_explored)
    """
    if initial_state == goal_state:
        return [initial_state], [initial_state]
    stack = [(initial_state, [initial_state])]
    visited = {initial_state}
    nodes_explored = [initial_state]
    while stack:
        node, path = stack.pop()
        for neighbor in graph.get(node, []):
            if neighbor == goal_state:
                return path + [neighbor], nodes_explored + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                nodes_explored.append(neighbor)
                stack.append((neighbor, path + [neighbor]))
    return None, nodes_explored


# ---------------------------------------------------------------------------
# UCS - Uniform Cost Search (informed by cost)
# ---------------------------------------------------------------------------

class UniformCostSearch:
    """
    Uniform Cost Search on a graph with edge costs.
    graph format: dict {node: [(neighbor, cost), ...]}
    """

    def __init__(self, graph):
        """
        Args:
            graph: object with .get_graph() -> {node: [(neighbor, cost), ...]}
                   or plain dict.
        """
        self.graph = graph.get_graph() if hasattr(graph, "get_graph") else graph

    def search(self, initial_state, goal_state):
        """
        Returns:
            tuple: (path, total_cost, nodes_explored) or (None, None, nodes_explored)
        """
        if initial_state == goal_state:
            return [initial_state], 0, [initial_state]
        # (cost, node, path)
        pq = [(0, initial_state, [initial_state])]
        visited = set()
        min_cost = {initial_state: 0}
        nodes_explored = []
        while pq:
            cost, node, path = heapq.heappop(pq)
            if node in visited:
                continue
            if node in min_cost and min_cost[node] < cost:
                continue
            visited.add(node)
            nodes_explored.append(node)
            if node == goal_state:
                return path, cost, nodes_explored
            for neighbor, edge_cost in self.graph.get(node, []):
                if neighbor in visited:
                    continue
                new_cost = cost + edge_cost
                if neighbor not in min_cost or new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))
        return None, None, nodes_explored


# ---------------------------------------------------------------------------
# A* - A* Search (informed by heuristic)
# ---------------------------------------------------------------------------

class AStarSearch:
    """
    A* Search on a graph with edge costs and heuristic.
    graph format: dict {node: [(neighbor, cost), ...]}
    heuristic_func(node, goal) -> h value (admissible).
    """

    def __init__(self, graph, heuristic_func=None):
        self.graph = graph.get_graph() if hasattr(graph, "get_graph") else graph
        self.heuristic = heuristic_func if heuristic_func is not None else (lambda n, g: 0)

    def search(self, initial_state, goal_state):
        """
        Returns:
            tuple: (path, total_cost, nodes_explored) or (None, None, nodes_explored)
        """
        if initial_state == goal_state:
            return [initial_state], 0, [initial_state]
        g_score = {initial_state: 0}
        h0 = self.heuristic(initial_state, goal_state)
        # (f, g, node, path) for tie-breaking we use g then node order via path
        pq = [(h0, 0, initial_state, [initial_state])]
        visited = set()
        nodes_explored = []
        came_from = {initial_state: None}
        while pq:
            f, g, node, path = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            nodes_explored.append(node)
            if node == goal_state:
                return path, g_score[goal_state], nodes_explored
            for neighbor, edge_cost in self.graph.get(node, []):
                if neighbor in visited:
                    continue
                tentative_g = g_score[node] + edge_cost
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = node
                    g_score[neighbor] = tentative_g
                    h = self.heuristic(neighbor, goal_state)
                    heapq.heappush(pq, (tentative_g + h, tentative_g, neighbor, path + [neighbor]))
        return None, None, nodes_explored


# ---------------------------------------------------------------------------
# Minimax - Adversarial search
# ---------------------------------------------------------------------------

class MiniMaxSearch:
    """
    MiniMax with alpha-beta pruning.
    graph: dict {node: [successors]}
    utility_func(node, is_maximizing_player) -> numeric value (e.g. at leaves).
    """

    def __init__(self, graph, utility_func, max_depth=5):
        self.graph = graph
        self.utility = utility_func
        self.max_depth = max_depth

    def minimax(self, node, depth, is_maximizing_player, alpha=float("-inf"), beta=float("inf")):
        """
        Returns:
            tuple: (value, path_from_this_node)
        """
        if depth == 0 or node not in self.graph or len(self.graph[node]) == 0:
            u = self.utility(node, is_maximizing_player)
            return u, [node]
        neighbors = self.graph[node]
        if is_maximizing_player:
            max_val = float("-inf")
            best_path = [node]
            for neighbor in neighbors:
                val, path = self.minimax(neighbor, depth - 1, False, alpha, beta)
                if val > max_val:
                    max_val = val
                    best_path = [node] + path
                alpha = max(alpha, val)
                if beta <= alpha:
                    break
            return max_val, best_path
        else:
            min_val = float("inf")
            best_path = [node]
            for neighbor in neighbors:
                val, path = self.minimax(neighbor, depth - 1, True, alpha, beta)
                if val < min_val:
                    min_val = val
                    best_path = [node] + path
                beta = min(beta, val)
                if beta <= alpha:
                    break
            return min_val, best_path

    def search(self, initial_state):
        """Returns (best_value, best_path) for the maximizing agent."""
        return self.minimax(initial_state, self.max_depth, True)
