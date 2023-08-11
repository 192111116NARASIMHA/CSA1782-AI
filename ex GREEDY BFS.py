from queue import PriorityQueue

def greedy_best_first_search(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start))  # Using a priority queue with heuristic value as priority
    
    while not pq.empty():
        cost, current_node = pq.get()
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        print("Visiting node:", current_node)
        
        if current_node == goal:
            print("Goal reached!")
            return
        
        for neighbor, heuristic_value in graph[current_node]:
            if neighbor not in visited:
                pq.put((heuristic_value, neighbor))
    
    print("Goal not reachable.")

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 10), ('C', 5)],
    'B': [('D', 7)],
    'C': [('D', 15), ('E', 10)],
    'D': [('E', 3)],
    'E': []
}

start_node = 'A'
goal_node = 'E'

greedy_best_first_search(graph, start_node, goal_node)
