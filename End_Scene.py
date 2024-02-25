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

        text_intro = Tex("Advancements built upon the normalized cuts algorithm").scale(1)
        text_intro.move_to((0, 0, 0))

        self.play(Write(text_intro))
        self.wait(3)
        self.play(FadeOut(text_intro))

        text_intro2 = Tex("Semisupervised normalized cuts").scale(1)
        text_intro2.move_to((0, 0, 0))

        self.play(Write(text_intro2))
        self.wait(3)
        self.play(FadeOut(text_intro2))

        # KConvertion of 2D coordinates into 3D for manim
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

        ### defining labels of must-link connections (examples) ###
        must_link_moon = [((6,7), (7,7)), ((7,7), (8,7))]
        must_link_earth = [((3,4), (4,4)), ((4,4), (5,4)), ((5,4),(6,4)), ((6,4), (6,5))]
        must_link_space = [((1,7), (1,8)), ((1,8), (2,8)), ((2,8), (2,7)), ((2,7), (2,6)), ((2,6), (2,5)), ((7,0), (7,1)), ((7,1), (7,2)), ((7,2), (7,3)), ((7,3), (8,3)), ((8,3), (8,4)), ((8,4), (8,5))]

        moon_link_nodes = [(6,7), (7,7), (8,7)]
        earth_link_nodes = [(3,4),(4,4),(5,4),(6,4),(6,5)]
        space_link_nodes = [(1,7), (1,8), (2,8), (2,7), (2,6), (2,5), (7,0), (7,1), (7,2), (7,3), (8,3), (8,4), (8,5)]
        
        # Edge config
        edge_config = {
            edge: {"stroke_color": "#666666"}
            for edge in G.edges()
        }

        # first graph without the updated colours of the constraints
        m_graph = Graph(list(G.nodes), list(G.edges), layout=pos_3d, layout_scale=1, labels=False, 
                        vertex_config=vertex_config, edge_config=edge_config)


        # centering
        m_graph.move_to(ORIGIN)
        m_graph.scale(0.7)

        self.play(Create(m_graph), run_time=5)
        self.wait(3)

        # updating colours in config for constraint visualization
        edge_config.update({moon_edge: {"stroke_color": 'orange'} for moon_edge in must_link_moon})
        vertex_config.update({moon_link_node: {"color": 'orange', "radius": 0.2} for moon_link_node in moon_link_nodes})
        edge_config.update({earth_edge: {"stroke_color": 'white'} for earth_edge in must_link_earth})
        vertex_config.update({earth_link_node: {"color": 'white', "radius": 0.2} for earth_link_node in earth_link_nodes})
        edge_config.update({space_edge: {"stroke_color": '#80091B'} for space_edge in must_link_space})
        vertex_config.update({space_link_node: {"color": '#80091B', "radius": 0.2} for space_link_node in space_link_nodes})

        # this new graph new represents the constraints with different colours (uses the updated config)
        m_graph2 = Graph(list(G.nodes), list(G.edges), layout=pos_3d, layout_scale=1, labels=False, 
                        vertex_config=vertex_config, edge_config=edge_config)
        m_graph2.move_to(ORIGIN)
        m_graph2.scale(0.7)
        self.add(m_graph2)
        self.wait(5)

        # self.play(
        #     #*[m_graph.vertices[v].animate.set_fill_color("orange") for v in m_graph.vertices],
        #     *[ApplyMethod(edge_config.update({y_edge: {"stroke_color": 'orange'} for y_edge in must_link_moon}))],
        #     run_time=3
        # )

        self.play(FadeOut(m_graph))

        self.wait(2)
