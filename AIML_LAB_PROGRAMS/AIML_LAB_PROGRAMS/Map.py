def is_safe(graph, color, node, col):
    for neighbor in graph[node]:
        if color[neighbor] == col:
            return False
    return True


def solve_map_coloring(graph, m, color, node, color_names):
    
    if node == len(graph):
        return True

    
    for col in range(m):
        if is_safe(graph, color, node, col):
            color[node] = col
            if solve_map_coloring(graph, m, color, node + 1, color_names):
                return True
            color[node] = -1  

    return False


def map_coloring(graph, m, color_names):
    color = [-1] * len(graph)

    if solve_map_coloring(graph, m, color, 0, color_names):
        return [color_names[c] for c in color]  # Convert color index to actual color names
    else:
        return "Solution does not exist."


if __name__ == "__main__":
    
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2]
    }

    
    m = 3

    
    color_names = ["Red", "Green", "Blue"]

    
    result = map_coloring(graph, m, color_names)
    print("Color assignment:", result)
