import matplotlib.pyplot as plt
import sys
import os

# Ensure we can import figure5_states
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from figure5_states import get_state_coordinates, get_graph
except ImportError:
    print("Error: Could not import figure5_states. Make sure it is in the same directory.")
    sys.exit(1)

def visualize(path_nodes=None):
    coords = get_state_coordinates()
    graph = get_graph()
    
    # Extract coordinates
    x_vals = []
    y_vals = []
    names = []
    
    for city, (x, y, z) in coords.items():
        x_vals.append(x)
        y_vals.append(y)
        names.append(city)
    
    plt.figure(figsize=(12, 10))
    
    # Draw edges first (so they are behind nodes)
    added_edges = set()
    for city, neighbors in graph.items():
        if city not in coords:
            continue
        x1, y1 = coords[city][0], coords[city][1]
        
        for neighbor in neighbors:
            if neighbor in coords:
                # Avoid drawing duplicates
                edge = tuple(sorted((city, neighbor)))
                if edge in added_edges:
                    continue
                added_edges.add(edge)
                
                x2, y2 = coords[neighbor][0], coords[neighbor][1]
                plt.plot([x1, x2], [y1, y2], 'gray', linestyle='-', alpha=0.5, linewidth=1)
    
    
    # Draw path if provided
    if path_nodes and len(path_nodes) > 1:
        print(f"Highlighting path: {' -> '.join(path_nodes)}")
        path_coords = []
        for city in path_nodes:
            if city in coords:
                path_coords.append(coords[city])
            else:
                print(f"Warning: City '{city}' not found in coordinates")
        
        if len(path_coords) > 1:
            px, py = zip(*[(p[0], p[1]) for p in path_coords])
            plt.plot(px, py, 'r-', linewidth=3, alpha=0.7, label='Planned Path')
            
            # Add arrows
            for i in range(len(path_coords) - 1):
                p1 = path_coords[i]
                p2 = path_coords[i+1]
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                plt.arrow(p1[0], p1[1], dx*0.6, dy*0.6, head_width=2, head_length=2, fc='red', ec='red', zorder=10)

    # Highlight Start (Addis Ababa) and Goal (Moyale) or from path
    start_node = path_nodes[0] if path_nodes else "Addis Ababa"
    goal_node = path_nodes[-1] if path_nodes else "Moyale"

    if start_node in coords:
        xa, ya = coords[start_node][0], coords[start_node][1]
        plt.scatter([xa], [ya], c='green', s=150, label='Start', zorder=6)
    
    if goal_node in coords:
        xm, ym = coords[goal_node][0], coords[goal_node][1]
        plt.scatter([xm], [ym], c='red', s=150, label='Goal', zorder=6)
    
    # Annotate names
    for i, txt in enumerate(names):
        plt.annotate(txt, (x_vals[i], y_vals[i]), xytext=(0, 5), textcoords='offset points', ha='center', fontsize=9)
    
    plt.title(f"Robot Path Visualization ({' -> '.join(path_nodes) if len(path_nodes) < 5 else '...'})", fontsize=14)
    plt.xlabel("X (meters)")
    plt.ylabel("Y (meters)")
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend()
    plt.axis('equal')
    
    output_file = "robot_path_visualization.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Path visualization saved to {output_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Visualize Gazebo World and Robot Path")
    parser.add_argument("--path", nargs="+", help="List of cities in the path")
    args = parser.parse_args()
    
    visualize(args.path)
