from manim import *
import networkx as nx

# Create a new graph
G = nx.Graph()

# Add nodes and edges for a 10x10 grid, including diagonal connections
y = 10
x = 10
for i in range(x):
    for j in range(y):
        # Add node
        G.add_node((i, j))

        # Add edges to neighboring nodes (including diagonals)
        if i > 0:
            G.add_edge((i, j), (i - 1, j))  # Edge to the left
            if j > 0:
                G.add_edge((i, j), (i - 1, j - 1))  # Diagonal left-top
            if j < 9:
                G.add_edge((i, j), (i - 1, j + 1))  # Diagonal left-bottom
        if j > 0:
            G.add_edge((i, j), (i, j - 1))  # Edge to the top
        if i < 9:
            G.add_edge((i, j), (i + 1, j))  # Edge to the right
            if j > 0:
                G.add_edge((i, j), (i + 1, j - 1))  # Diagonal right-top
            if j < 9:
                G.add_edge((i, j), (i + 1, j + 1))  # Diagonal right-bottom
        if j < 9:
            G.add_edge((i, j), (i, j + 1))  # Edge to the bottom

# Define positions for the nodes in the graph
pos = {(i, j): (i, j) for i in range(10) for j in range(10)}

# Define nodes for Moon and Earth
moon_nodes = [(7,8), (6,7), (7,7), (8,7), (7,6)]
earth_nodes = [(5,7), (4,7), (3,6), (4,6), (5,6), (6,6), (2,5), (3,5), (4,5), (5,5), (6,5), (7,5), 
               (2,4), (3,4), (4,4), (5,4), (6,4), (7,4), (3,3), (4,3), (5,3), (6,3), (4,2), (5,2)]

# Set colors for each node
node_colors = []
for node in G.nodes():
    if node in moon_nodes:
        node_colors.append('#bdb900')  # Color for Moon
    elif node in earth_nodes:
        node_colors.append('#318ab3')  # Color for Earth
    else:
        node_colors.append('black')  # Default color

class GraphScene(Scene):
    def construct(self):

        text_intro = Tex("Graph Cuts motivation").scale(1.4)
        text_intro.move_to((0, 0.5, 0))
        text_intro2 = Tex("The graph theoretical perspective")
        text_intro2.move_to((0, -0.5, 0))

        self.play(Write(text_intro))
        self.play(Write(text_intro2))
        self.wait(4)
        self.play(FadeOut(text_intro, text_intro2))

        text_connected = Tex("Subgraphs and components")
        text_connected2 = Tex("in a connected graph")
        text_connected.move_to((0, 0.5, 0))
        text_connected2.move_to((0, -0.5, 0))
        self.play(Write(text_connected), Write(text_connected2))
        self.wait(3)
        self.play(FadeOut(text_connected, text_connected2))
        # Convertion of 2D coordinates into 3D for manim
        pos_3d = {node: (x, y, 0) for node, (x, y) in pos.items()}

        # Colour definition
        node_colors = {node: ('#bdb900' if node in moon_nodes else 
                              '#318ab3' if node in earth_nodes else 
                              '#68228B') for node in G.nodes()}

        # Node config
        vertex_config = {
            node: {"radius": 0.2, "color": node_colors[node]}
            for node in G.nodes()
        }
        
        # Edge config
        edge_config = {
            edge: {"stroke_color": "#666666"}
            for edge in G.edges()
        }
        # Manim graph building from networkx graph
        m_graph = Graph(list(G.nodes), list(G.edges), layout=pos_3d, layout_scale=1, labels=False, 
                        vertex_config=vertex_config, edge_config=edge_config)


        # centering
        m_graph.move_to(ORIGIN)
        m_graph.scale(0.7)

        
        self.play(Create(m_graph), run_time=5)

        self.wait(5)

        self.play(
            *[m_graph.vertices[v].animate.set_fill_color("#318ab3") for v in m_graph.vertices],
            *[ApplyMethod(m_graph.edges[e].set_color, "#318ab3") for e in m_graph.edges],
            run_time=3
        )
        self.wait(2)

        self.play(FadeOut(m_graph))
        m_graph = Graph(list(G.nodes), list(G.edges), layout=pos_3d, layout_scale=1, labels=False, 
                        vertex_config=vertex_config, edge_config=edge_config)
        m_graph.move_to(ORIGIN)
        m_graph.scale(0.7)
        self.play(FadeIn(m_graph))

        self.wait(2)

        self.play(
            *[m_graph.vertices[v].animate.set_fill_color("#bdb900") for v in m_graph.vertices],
            *[ApplyMethod(m_graph.edges[e].set_color, "#bdb900") for e in m_graph.edges],
            run_time=3
        )

        self.wait(2)

        self.play(FadeOut(m_graph))
        m_graph = Graph(list(G.nodes), list(G.edges), layout=pos_3d, layout_scale=1, labels=False, 
                        vertex_config=vertex_config, edge_config=edge_config)
        m_graph.move_to(ORIGIN)
        m_graph.scale(0.7)
        self.play(FadeIn(m_graph))

        self.wait(2)

        self.play(
            *[m_graph.vertices[v].animate.set_fill_color("#68228B") for v in m_graph.vertices],
            *[ApplyMethod(m_graph.edges[e].set_color, "#68228B") for e in m_graph.edges],
            run_time=3
        )

        self.wait(2)

        self.play(FadeOut(m_graph))

        self.wait(2)


        # subgraphs and components of disconnected graph (desired cuts)
        text_disconnected = Tex("Subgraphs and components")
        text_disconnected2 = Tex("in a disconnected graph")
        text_disconnected.move_to((0, 0.5, 0))
        text_disconnected2.move_to((0, -0.5, 0))
        self.play(Write(text_disconnected), Write(text_disconnected2))
        self.wait(3)
        self.play(FadeOut(text_disconnected, text_disconnected2))

        space_nodes = list(set(G.nodes()) - (set(earth_nodes).union(set(moon_nodes))))
        blue_edges = [(u, v) for u, v in G.edges() if u in earth_nodes and v in earth_nodes]
        yellow_edges = [(u, v) for u, v in G.edges() if u in moon_nodes and v in moon_nodes]
        purple_edges = [(u, v) for u, v in G.edges() if u in space_nodes and v in space_nodes]

        edge_config2 = {
            edge: {"stroke_color": "#666666"} for edge in G.edges()
        }

        edge_config2.update({b_edge: {"stroke_color": '#318ab3'} for b_edge in blue_edges})
        edge_config2.update({y_edge: {"stroke_color": '#bdb900'} for y_edge in yellow_edges})
        edge_config2.update({p_edge: {"stroke_color": '#68228B'} for p_edge in purple_edges})
        edge_config2.update({i_edge: {"stroke_color": BLACK} for i_edge in G.edges() if i_edge not in blue_edges and i_edge not in purple_edges and i_edge not in yellow_edges})

        disconnected_graph = Graph(list(G.nodes), list(G.edges), layout=pos_3d, layout_scale=1, labels=False, 
                        vertex_config=vertex_config, edge_config=edge_config2)
        
        disconnected_graph.move_to(ORIGIN)
        disconnected_graph.scale(0.7)
        self.play(FadeIn(disconnected_graph))

        self.wait(9)

        self.play(FadeOut(disconnected_graph))
