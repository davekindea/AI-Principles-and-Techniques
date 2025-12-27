"""
Heuristic values for A* search based on the provided path data
Heuristic represents estimated cost from each node to goal (Moyale)
"""

# Heuristic values (h) from Figure 3
# These are the exact heuristic values provided for each city to goal (Moyale)

HEURISTIC_TO_MOYALE = {
    # Exact values from Figure 3
    "Addis Ababa": 26,
    "Adama": 23,
    "Adigrat": 62,
    "Adwa": 65,
    "Alamata": 53,
    "Ambo": 31,
    "Arba Minch": 13,
    "Asmara": 68,
    "Asmera": 68,  # Alternative spelling
    "Assasa": 18,
    "Assella": 18,  # Alternative spelling
    "Assosa": 51,
    "Awash": 27,
    "Azezo": 55,
    "Babile": 37,
    "Bahir Dar": 48,
    "Batu": 19,
    "Bedelle": 40,
    "Bonga": 33,
    "Bongo": 33,  # Alternative spelling
    "Butajira": 21,
    "Chiro": 31,
    "Dawro": 23,
    "Debarke": 60,
    "Dembidollo": 49,
    "Dembi Dollo": 49,  # Alternative spelling
    "Dilla": 12,
    "Dire Dawa": 31,
    "Dodolla": 19,
    "Dollo": 18,
    "Debre Birhan": 31,
    "Debre Markos": 39,
    "Debre Tabor": 52,
    "Dessie": 44,
    "Fanti Rasu": 49,
    "Finote Selam": 42,
    "Gambella": 51,
    "Gobi Rasu": 32,
    "Gabi Rasu": 32,  # Alternative spelling
    "Goba": 40,
    "Gode": 35,
    "Gondar": 56,
    "Gore": 46,
    "Harar": 35,
    "Hawassa": 15,
    "Hossana": 21,
    "Injibara": 44,
    "Jigjiga": 40,
    "Jijiga": 40,  # Alternative spelling
    "Jimma": 33,
    "Liben": 11,
    "Maji": 28,
    "Mekelle": 58,
    "Metekel": 59,
    "Metema": 62,
    "Moyale": 0,
    "Nairobi": 22,
    "Nekemete": 39,
    "Nekemte": 39,  # Alternative spelling
    "Robe": 22,
    "Samara": 42,
    "Sekota": 59,
    "Shire": 67,
    "Shashemene": 16,
    "Sof Oumer": 45,
    "Tepi": 41,
    "Werder": 46,
    "Woldia": 50,
    "Wolaita Sodo": 17,
    "Wolkite": 25,
    "Worabe": 22,
    "Yabello": 6,
    "Yirgalem": 13,
    
    # Additional cities that might be in the graph but not in the heuristic table
    # Use reasonable defaults based on proximity
    "Bule Hora": 9,  # Between Dilla (12) and Yabello (6)
    "Konso": 3,  # Close to Yabello (6)
    "Matahara": 24,  # Between Adama (23) and Awash (27)
    "Kemise": 38,  # Between Dessie (44) and Debre Sina
    "Debre Sina": 35,  # Between Debre Birhan (31) and Kemise
    "Lalibela": 48,  # Between Woldia (50) and Sekota (59)
    "Axum": 64,  # Close to Adwa (65)
    "Humera": 63,  # Close to Metema (62)
    "Dega Habur": 38,  # Between Jigjiga (40) and Kebri Dehar
    "Kebri Dehar": 36,  # Between Dega Habur and Gode (35)
    "Mizan Teferi": 42,  # Close to Tepi (41)
    "Basketo": 16,  # Close to Arba Minch (13)
    "Bench Maji": 29,  # Close to Maji (28)
    "Juba": 50,  # External connection
    "Mokadisho": 0,  # External connection
    "Kilbet Rasu": 50,  # Close to Fanti Rasu (49)
}

def create_heuristic_function():
    """
    Create a heuristic function that returns estimated cost to goal (Moyale)
    """
    def heuristic(node, goal):
        """Return heuristic value from node to goal"""
        if node == goal:
            return 0
        
        # For goal = Moyale, use the stored heuristic values
        if goal == "Moyale":
            return HEURISTIC_TO_MOYALE.get(node, 50)  # Default to 50 if not found
        
        # For other goals, use a simple approximation
        # In practice, you'd have heuristic tables for each goal
        return 30  # Default heuristic
    
    return heuristic

