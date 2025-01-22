
import itertools

def count_edge_crossings(graph, pos):
    def edges_cross(p1, p2, q1, q2):
        """Check if edges (p1, p2) and (q1, q2) cross using vector math."""
        def ccw(a, b, c):
            # Check counter-clockwise orientation
            return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])
        
        return (ccw(p1, q1, q2) != ccw(p2, q1, q2)) and (ccw(p1, p2, q1) != ccw(p1, p2, q2))

    edges = list(graph.edges())
    crossing_count = 0

    # Check all pairs of edges
    for (u1, v1), (u2, v2) in itertools.combinations(edges, 2):
        if len({u1, v1, u2, v2}) == 4:  # Ignore edges that share nodes
            if edges_cross(pos[u1], pos[v1], pos[u2], pos[v2]):
                crossing_count += 1

    return crossing_count