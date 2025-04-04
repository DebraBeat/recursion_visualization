def dfs(adj, vertex, seen):
    seen.add(vertex)

    for neighbor in adj[vertex]:
        if neighbor not in seen:
            dfs(adj, neighbor, seen)