from manim import *

class GraphTheoryScene(Scene):
    def construct(self):

        # === animation 1: nodes & edges === #

        # Defining the graph structure
        vertices = [1, 2]
        edges = [(1,2)]

        # Creating an empty graph
        g = Graph(
            vertices=vertices,
            edges=[],
            layout="circular", layout_scale=3, labels=False,
            vertex_config={v: {"fill_color": BLUE, "radius": 0.3} for v in vertices},
            edge_config={(e[0], e[1]): {"stroke_color": WHITE} for e in edges}
        )

        # Adding vertices to the graph
        self.add_foreground_mobject(g)
        self.play(Create(g), run_time=3)

        # Creating arrow for vertex
        arrow_1 = Line(
            start=g.vertices[2].get_center()+(1.1, 2.2, 0),
            end=g.vertices[2].get_center()+(0.3, 0.8, 0),
            color=GOLD,
            stroke_width=10
        )

        text_vertices = Tex("Node", color=GOLD)
        text_vertices.next_to(arrow_1.start, RIGHT, buff=0.2)

        self.play(Create(arrow_1))
        self.play(Write(text_vertices))


        

        # Waiting before adding edges
        #self.wait(1)

        # Adding edges to the graph
        edge_lines = [Line(g.vertices[e[0]].get_center(), g.vertices[e[1]].get_center(), color=WHITE) for e in edges]
        g_edges = VGroup(*edge_lines)
        self.play(Create(g_edges), run_time=2)

        # Creating arrow for edge
        arrow_2 = Line(
            start=g.vertices[2].get_center()+(g.vertices[1].get_center()-g.vertices[2].get_center())/2+(2,-2,0),
            end=g.vertices[2].get_center()+(g.vertices[1].get_center()-g.vertices[2].get_center())/2+(0.2, -0.3, 0),
            color=GOLD,
            stroke_width=10
        )

        text_edges = Tex("Edge", color=GOLD)
        text_edges.next_to(arrow_2.start, RIGHT, buff=0.2)

        text_weight = Tex("0.75", color=WHITE)
        text_weight.next_to(g_edges, UP, buff = 0.2)

        self.play(Create(arrow_2))
        self.play(Write(text_edges))
        self.wait(2)
        self.play(Write(text_weight))

        # removing graph from the scene
        self.wait(4)
        self.play(FadeOut(arrow_1), FadeOut(text_vertices))
        self.play(FadeOut(arrow_2), FadeOut(text_edges))
        self.play(FadeOut(g), FadeOut(g_edges), FadeOut(text_weight))



        # === animation 2: different forms of graphs & relevance for graph cuts === #

        # Define the graph
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        graph_pos_layout = {    
            1: (-3, -1, 0),
            2: (-3, 1, 0),
            3: (-1, -1, 0),
            4: (-1, 1, 0),
            5: (1, -1, 0),
            6: (1, 1, 0),
            7: (3, -1, 0),
            8: (3, 1, 0)}
        
        g1 = Graph(
            vertices=vertices,
            edges=edges,
            layout="planar", layout_scale=3, labels=False,
            vertex_config={v: {"fill_color": BLUE, "radius": 0.3} for v in vertices},
            edge_config={(e[0], e[1]): {"stroke_color": WHITE} for e in edges}
        )

        g2 = Graph(
            vertices=vertices,
            edges=edges,
            layout="circular", layout_scale=3, labels=False,
            vertex_config={v: {"fill_color": BLUE, "radius": 0.3} for v in vertices},
            edge_config={(e[0], e[1]): {"stroke_color": WHITE} for e in edges}
        )

        g3 = Graph(
            vertices=vertices,
            edges=edges,
            layout="spiral", layout_scale=3, labels=False,
            vertex_config={v: {"fill_color": BLUE, "radius": 0.3} for v in vertices},
            edge_config={(e[0], e[1]): {"stroke_color": WHITE} for e in edges}
        )

        edges_rectangle = [(1, 2), (1, 3), (1, 4), (1, 6), (2, 3),
                 (2, 4), (2, 5), (3, 4), (3, 5),
                 (3, 6), (3, 8), (4, 5), (4, 6), (4, 7), (5, 6), (5, 8), (5, 7), (6, 7), (6, 8), (7,8)]
        
        g4 = Graph(
            vertices=vertices,
            edges=edges_rectangle,
            layout=graph_pos_layout, layout_scale=3, labels=False,
            vertex_config={v: {"fill_color": BLUE, "radius": 0.3} for v in vertices},
            edge_config={(e[0], e[1]): {"stroke_color": WHITE} for e in edges}
        )

        self.play(ScaleInPlace(g1, 0.6))
        self.play(g1.animate.move_to((-3.8, 2.25, 0)))
        self.play(ScaleInPlace(g2, 0.6))
        self.play(g2.animate.move_to((3.6, 1.4, 0)))
        self.play(ScaleInPlace(g3, 0.6))
        self.play(g3.animate.move_to((-4.2, -2, 0)))
        self.play(ScaleInPlace(g4, 0.6))
        self.play(g4.animate.move_to((3.5, -2.25, 0)))

        self.wait(5)

        self.play(FadeOut(g1,g2,g3))

        self.play(g4.animate.shift((-3.5, 2.25, 0)))

        self.play(ScaleInPlace(g4, 1))

        self.wait(2)
        self.play(FadeOut(g4))




        # === animation 3: Rectangular structure & subgraphs === #

        # Define the graph
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        
        graph_pos_layout = {    
            1: (-3, -1, 0),
            2: (-3, 1, 0),
            3: (-1, -1, 0),
            4: (-1, 1, 0),
            5: (1, -1, 0),
            6: (1, 1, 0),
            7: (3, -1, 0),
            8: (3, 1, 0)}
        
        # Creating the graph
        g = Graph(
            vertices=vertices,
            edges=edges_rectangle,
            layout=graph_pos_layout, layout_scale=3, labels=False,
            vertex_config={v: {"fill_color": BLUE, "radius": 0.3} for v in vertices},
            edge_config={(e[0], e[1]): {"stroke_color": WHITE} for e in edges}
        )

        
        self.play(Create(g), run_time=10)
        self.wait(10)
        
        # Vertices and edges to change color
        vertices_to_change = [6, 7, 8]
        edges_to_change = [(6, 7), (6, 8), (7, 8)]

        text_subgraph = Tex("Subgraph", color=WHITE)
        text_subgraph.move_to((0, 2.5, 0))
        self.play(Write(text_subgraph))
        self.play(g.animate.move_to((0, -1, 0)))
        self.wait(3)
        text_subgraph2 = Text("G(V^, E^) is subgraph of G(V, E) if:", color=WHITE).scale(0.4)
        text_part_2 = Text(" 1)V^ ⊆ V").scale(0.4)
        text_part_3 = Text("2) E^ ⊆ E").scale(0.4)
        text_part_4 = Text("3) for each e in E^ its nodes are in V^").scale(0.4)
        
        text_subgraph2.move_to((0, 1.8, 0))
        text_part_2.move_to((0, 1.3, 0))
        text_part_3.move_to((0, 1.0, 0))
        text_part_4.move_to((0, 0.7, 0))

        self.play(Write(text_subgraph2))
        self.wait(2)
        self.play(Write(text_part_2))
        self.wait(1)
        self.play(Write(text_part_3))
        self.wait(1)
        self.play(Write(text_part_4))
        self.wait(3)

        self.play(
            *[g.vertices[v].animate.set_fill_color(ORANGE) for v in vertices_to_change],
            *[ApplyMethod(g.edges[e].set_color, ORANGE) for e in edges_to_change],
            run_time=4
        )

        self.wait(6)
        self.play(FadeOut(text_subgraph, text_subgraph2, text_part_2, text_part_3, text_part_4))

        # text about connectivity
        text_connectivity = Tex("Connected nodes", color=WHITE)
        text_connectivity.move_to((0, 2.5, 0))
        self.play(Write(text_connectivity))
        self.wait(1)
        text_connectivity2 = Text("In undirected graphs: Two nodes are connected, if there is a path from one node to the other", color=WHITE, should_center=True).scale(0.4)
        text_connectivity2.move_to((0, 1.8, 0))

        text_connectivity3 = Text("=> all nodes are connected to one another in our graph").scale(0.4)
        text_connectivity4 = Text("=> connected graph yields exactly one component").scale(0.4)
        text_connectivity3.move_to((0, 1.3, 0))
        text_connectivity4.move_to((0, 1.0, 0))

        self.play(Write(text_connectivity2))
        self.wait(2)
        self.play(Write(text_connectivity3))
        self.wait(1)
        self.play(Write(text_connectivity4))
        self.wait(6)
        self.play(FadeOut(text_connectivity, text_connectivity2, text_connectivity3, text_connectivity4))


        

        self.wait(2)




        # === animation 4: Components in connected and in particular in disconnected graphs === #
        comp_vertices = list(set(vertices) - set(vertices_to_change))
        comp_edges = list(set(edges_rectangle) - set(edges_to_change))

        # text about components
        text_components = Tex("Components in connected graphs", color=WHITE)
        text_components.move_to((0, 2.5, 0))
        self.play(Write(text_components))
        self.wait(1)
        text_components2 = Text("1) All nodes v ∈ V, which are connected to some v^ ∈ V^", color=WHITE).scale(0.4)
        text_components2.move_to((0, 1.8, 0))

        text_components3 = Text("2) All edges in E whose nodes are connected to some node v^ ∈ V^").scale(0.4)
        text_components3.move_to((0, 1.4, 0))

        self.play(Write(text_components2))
        self.wait(1)
        self.play(Write(text_components3))
        self.wait(3)

        self.play(
            *[g.vertices[v].animate.set_fill_color(GREEN) for v in comp_vertices],
            *[ApplyMethod(g.edges[e].set_color, GREEN) for e in comp_edges],
            run_time=4
        )

        self.wait(4)

        self.play(
            *[g.vertices[v].animate.set_fill_color(GREEN) for v in vertices_to_change],
            *[ApplyMethod(g.edges[e].set_color, GREEN) for e in edges_to_change],
            run_time=4
        )

        self.wait(7)
        self.play(FadeOut(text_components, text_components2, text_components3))
        self.play(FadeOut(g))


        ## components in disconnected graph ##

        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 2), (1, 3), (1, 4), (2, 3),
                 (2, 4), (3, 4), (5, 6), (5, 8), (5, 7), (6, 7), (6, 8), (7,8)]
        
        graph_pos_layout = {    
            1: (-3, -1, 0),
            2: (-3, 1, 0),
            3: (-1, -1, 0),
            4: (-1, 1, 0),
            5: (1, -1, 0),
            6: (1, 1, 0),
            7: (3, -1, 0),
            8: (3, 1, 0)}
        
        # Creating the graph
        g_2_comps = Graph(
            vertices=vertices,
            edges=edges,
            layout=graph_pos_layout, layout_scale=3, labels=False,
            vertex_config={v: {"fill_color": BLUE, "radius": 0.3} for v in vertices},
            edge_config={(e[0], e[1]): {"stroke_color": WHITE} for e in edges}
        )

        g_2_comps.move_to((0, -1, 0))

        # text about components
        text_components = Tex("Components in disconnected graphs", color=WHITE)
        text_components.move_to((0, 2.5, 0))
        self.play(Write(text_components))
        self.wait(1)
        text_components2 = Text("1) All nodes v ∈ V, which are connected to some v^ ∈ V^", color=WHITE).scale(0.4)
        text_components2.move_to((0, 1.8, 0))

        text_components3 = Text("2) All edges in E whose nodes are connected to some node v^ ∈ V^").scale(0.4)
        text_components3.move_to((0, 1.4, 0))

        self.play(Write(text_components2))
        self.wait(1)
        self.play(Write(text_components3))

        self.wait(1)

        self.play(Create(g_2_comps), run_time = 2)
        self.wait(2)

        # same subgraph as before
        vertices_to_change = [6, 7, 8]
        edges_to_change = [(6, 7), (6, 8), (7, 8)]

        self.play(
            *[g_2_comps.vertices[v].animate.set_fill_color(ORANGE) for v in vertices_to_change],
            *[ApplyMethod(g_2_comps.edges[e].set_color, ORANGE) for e in edges_to_change],
            run_time=2
        )

        vertices_to_change_2 = [1, 2]
        edges_to_change_2 = [(1, 2)]

        self.play(
            *[g_2_comps.vertices[v].animate.set_fill_color(YELLOW) for v in vertices_to_change_2],
            *[ApplyMethod(g_2_comps.edges[e].set_color, YELLOW) for e in edges_to_change_2],
            run_time=2
        )


        # highlighting the seperated components
        comp_vertices = [1, 2, 3, 4]
        comp_edges = [(1, 2), (1, 3), (1, 4), (2, 3),
                 (2, 4), (3, 4)]
        
        comp_vertices_2 = [5, 6, 7, 8]
        comp_edges_2 = [(5, 6), (5, 8), (5, 7), (6, 7), (6, 8), (7,8)]

        self.play(
            *[g_2_comps.vertices[v].animate.set_fill_color(PURPLE) for v in comp_vertices],
            *[ApplyMethod(g_2_comps.edges[e].set_color, PURPLE) for e in comp_edges],
            run_time=4
        )

        self.wait(4)

        self.play(
            *[g_2_comps.vertices[v].animate.set_fill_color(GREEN) for v in comp_vertices_2],
            *[ApplyMethod(g_2_comps.edges[e].set_color, GREEN) for e in comp_edges_2],
            run_time=4
        )

        self.wait(5)
        self.play(FadeOut(text_components, text_components2, text_components3))
        self.play(FadeOut(g_2_comps))




        