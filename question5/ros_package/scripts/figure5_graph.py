"""
Figure 5 (relaxed) state space for Traveling Ethiopia.
Graph and Cartesian coordinates for ROS path planner.
"""

# Cartesian coordinates (x, y, z) in meters. Addis Ababa at origin.
STATE_COORDINATES = {
    "Addis Ababa": (0, 0, 0.5),
    "Debre Birhan": (0, 10, 0.5),
    "Ambo": (8, 0, 0.5),
    "Adama": (0, -8, 0.5),
    "Nekemte": (16, 0, 0.5),
    "Wolkite": (8, -6, 0.5),
    "Jimma": (16, -6, 0.5),
    "Butajira": (8, -12, 0.5),
    "Batu": (4, -12, 0.5),
    "Shashemene": (4, -18, 0.5),
    "Hawassa": (4, -24, 0.5),
    "Dilla": (4, -30, 0.5),
    "Bule Hora": (4, -36, 0.5),
    "Yabello": (4, -42, 0.5),
    "Moyale": (4, -48, 0.5),
    "Assella": (-4, -8, 0.5),
    "Dodolla": (0, -18, 0.5),
    "Woldia": (0, 20, 0.5),
    "Debre Sina": (0, 15, 0.5),
    "Kemise": (0, 25, 0.5),
    "Dessie": (0, 30, 0.5),
    "Worabe": (4, -14, 0.5),
    "Hossana": (6, -10, 0.5),
    "Wolaita Sodo": (2, -20, 0.5),
    "Matahara": (-4, -12, 0.5),
    "Debre Markos": (8, 12, 0.5),
    "Finote Selam": (8, 18, 0.5),
    "Bahir Dar": (8, 28, 0.5),
    "Gondar": (8, 38, 0.5),
    "Lalibela": (0, 38, 0.5),
    "Sekota": (-4, 38, 0.5),
    "Mekelle": (-8, 38, 0.5),
    "Arba Minch": (-2, -24, 0.5),
    "Bale": (-8, -18, 0.5),
    "Goba": (-12, -14, 0.5),
    "Babile": (-16, -10, 0.5),
    "Harar": (-20, -8, 0.5),
    "Dire Dawa": (-18, -12, 0.5),
}

# Undirected graph (adjacency list) for Figure 5 relaxed state space
FIGURE5_GRAPH = {
    "Addis Ababa": ["Debre Birhan", "Ambo", "Adama"],
    "Debre Birhan": ["Addis Ababa", "Debre Sina"],
    "Ambo": ["Addis Ababa", "Nekemte", "Wolkite"],
    "Adama": ["Addis Ababa", "Assella", "Matahara", "Batu"],
    "Nekemte": ["Ambo", "Jimma"],
    "Wolkite": ["Ambo", "Jimma", "Hossana", "Butajira"],
    "Jimma": ["Nekemte", "Wolkite"],
    "Butajira": ["Wolkite", "Worabe", "Batu"],
    "Batu": ["Butajira", "Shashemene", "Adama"],
    "Shashemene": ["Wolaita Sodo", "Hawassa", "Batu", "Dodolla"],
    "Hawassa": ["Dilla", "Shashemene"],
    "Dilla": ["Bule Hora", "Hawassa"],
    "Bule Hora": ["Yabello", "Dilla"],
    "Yabello": ["Moyale", "Bule Hora"],
    "Moyale": ["Yabello"],
    "Assella": ["Adama", "Dodolla"],
    "Dodolla": ["Shashemene", "Assella", "Bale"],
    "Woldia": ["Dessie", "Lalibela"],
    "Debre Sina": ["Debre Markos", "Kemise", "Debre Birhan"],
    "Kemise": ["Dessie", "Debre Sina"],
    "Dessie": ["Woldia", "Kemise"],
    "Worabe": ["Butajira", "Hossana", "Wolaita Sodo"],
    "Hossana": ["Wolkite", "Worabe", "Wolaita Sodo"],
    "Wolaita Sodo": ["Worabe", "Hossana", "Shashemene", "Arba Minch"],
    "Matahara": ["Adama"],
    "Debre Markos": ["Finote Selam", "Debre Sina"],
    "Finote Selam": ["Bahir Dar", "Debre Markos"],
    "Bahir Dar": ["Finote Selam", "Gondar"],
    "Gondar": ["Bahir Dar"],
    "Lalibela": ["Woldia", "Sekota"],
    "Sekota": ["Mekelle", "Lalibela"],
    "Mekelle": ["Sekota"],
    "Arba Minch": ["Wolaita Sodo"],
    "Bale": ["Dodolla", "Goba"],
    "Goba": ["Bale", "Babile"],
    "Babile": ["Goba", "Harar"],
    "Harar": ["Babile", "Dire Dawa"],
    "Dire Dawa": ["Harar"],
}


def get_graph_undirected():
    """Return graph with symmetric edges (undirected)."""
    g = {}
    for u, neighbors in FIGURE5_GRAPH.items():
        g.setdefault(u, []).extend(neighbors)
        for v in neighbors:
            g.setdefault(v, [])
            if u not in g[v]:
                g[v].append(u)
    return g
