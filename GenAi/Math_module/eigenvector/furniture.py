import networkx as nx
import random

# Create a directed graph
G = nx.DiGraph()

# Add nodes (shops)
shops = [f"Shop {chr(65 + i)}" for i in range(20)]  # 20 shops named A through T
G.add_nodes_from(shops)

# Add directed edges based on referrals (more complex relationships)
edges = []
for i in range(len(shops)):
    # Each shop will have 2-5 outgoing edges
    num_edges = random.randint(2, 5)
    for _ in range(num_edges):
        target = random.choice(shops)
        if target != shops[i]:  # Avoid self-loops
            edges.append((shops[i], target))

G.add_edges_from(edges)

# Calculate PageRank
pagerank_scores = nx.pagerank(G)

# Display PageRank results
print("PageRank Scores:")
for shop, score in sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{shop}: {score:.4f}")

# Find the shop with the highest PageRank score
top_shop = max(pagerank_scores, key=pagerank_scores.get)
print(f"\nShop with highest PageRank: {top_shop}")

# Find shortest paths to the top shop from other shops
print("\nShortest paths to contact the top shop (minimizing nodes):")
for shop in shops:
    if shop != top_shop:
        try:
            path = nx.shortest_path(G, source=shop, target=top_shop)
            print(f"Shortest path from {shop} to {top_shop}: {' -> '.join(path)} (Nodes covered: {len(path)})")
        except nx.NetworkXNoPath:
            print(f"No path from {shop} to {top_shop}")

# Visualize the network (optional, requires matplotlib)
try:
    import matplotlib.pyplot as plt
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, arrows=True)
    plt.title("Furniture Shop Network")
    plt.axis('off')
    plt.tight_layout()
    plt.show()
except ImportError:
    print("\nMatplotlib not installed. Skipping network visualization.")
