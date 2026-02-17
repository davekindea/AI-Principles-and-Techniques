"""
Shared search algorithms: BFS, DFS, UCS, A*, Minimax.
Each question uses the appropriate algorithm with its own graph data.
"""

from shared.search_algorithms import (
    breadth_first_search,
    depth_first_search,
    UniformCostSearch,
    AStarSearch,
    MiniMaxSearch,
)

__all__ = [
    "breadth_first_search",
    "depth_first_search",
    "UniformCostSearch",
    "AStarSearch",
    "MiniMaxSearch",
]
