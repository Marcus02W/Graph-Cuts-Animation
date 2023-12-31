from manim import *

class GraphTheoryScene(Scene):
    def construct(self):

        # white background
        self.camera.background_color = WHITE


        # === animation 1: nodes & edges === #

        # Defining the graph structure
        vertices = [1, 2]
        edges = [(1,2)]

        # Creating an empty graph
        g = Graph(
            vertices=vertices,
            edges=[],
            layout="circular", layout_scale=3, labels=False,
            vertex_config={v: {"fill_color": GRAY, "radius": 0.3} for v in vertices},
            edge_config={(e[0], e[1]): {"stroke_color": BLACK} for e in edges}
        )

        # Adding vertices to the graph
        self.add_foreground_mobject(g)
        self.play(Create(g), run_time=3)

        # Creating arrow for vertex
        arrow_1 = Arrow(
            start=g.vertices[2].get_center()+(1.1, 2.2, 0),
            end=g.vertices[2].get_center()+(0.1, 0.2, 0),
            color=GOLD,
            stroke_width=10
        )

        text_vertices = Tex("Knoten", color=GRAY)
        text_vertices.next_to(arrow_1.start, RIGHT, buff=0.2)

        self.play(Create(arrow_1))
        self.play(Write(text_vertices))


        

        # Waiting before adding edges
        self.wait(4)

        # Adding edges to the graph
        edge_lines = [Line(g.vertices[e[0]].get_center(), g.vertices[e[1]].get_center(), color=BLACK) for e in edges]
        g_edges = VGroup(*edge_lines)
        self.play(Create(g_edges), run_time=2)

        # Creating arrow for edge
        arrow_2 = Arrow(
            start=g.vertices[2].get_center()+(g.vertices[1].get_center()-g.vertices[2].get_center())/2+(2,-2,0),
            end=g.vertices[2].get_center()+(g.vertices[1].get_center()-g.vertices[2].get_center())/2,
            color=GOLD,
            stroke_width=10
        )

        text_edges = Tex("Kante", color=GRAY)
        text_edges.next_to(arrow_2.start, RIGHT, buff=0.2)

        text_weight = Tex("0.75", color=GRAY)
        text_weight.next_to(g_edges, UP, buff = 0.2)

        self.play(Create(arrow_2))
        self.play(Write(text_edges))
        self.wait(2)
        self.play(Write(text_weight))

        # removing graph from the scene
        self.wait(2)
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
            vertex_config={v: {"fill_color": GRAY, "radius": 0.3} for v in vertices},
            edge_config={(e[0], e[1]): {"stroke_color": BLACK} for e in edges}
        )

        g2 = Graph(
            vertices=vertices,
            edges=edges,
            layout="circular", layout_scale=3, labels=False,
            vertex_config={v: {"fill_color": GRAY, "radius": 0.3} for v in vertices},
            edge_config={(e[0], e[1]): {"stroke_color": BLACK} for e in edges}
        )

        g3 = Graph(
            vertices=vertices,
            edges=edges,
            layout="spiral", layout_scale=3, labels=False,
            vertex_config={v: {"fill_color": GRAY, "radius": 0.3} for v in vertices},
            edge_config={(e[0], e[1]): {"stroke_color": BLACK} for e in edges}
        )

        g4 = Graph(
            vertices=vertices,
            edges=edges,
            layout=graph_pos_layout, layout_scale=3, labels=False,
            vertex_config={v: {"fill_color": GRAY, "radius": 0.3} for v in vertices},
            edge_config={(e[0], e[1]): {"stroke_color": BLACK} for e in edges}
        )

        self.play(ScaleInPlace(g1, 0.6))
        self.play(g1.animate.shift((-3.5, 2.25, 0)))
        self.play(ScaleInPlace(g2, 0.6))
        self.play(g2.animate.shift((3.5, 1.8, 0)))
        self.play(ScaleInPlace(g3, 0.6))
        self.play(g3.animate.shift((-3.5, -2.25, 0)))
        self.play(ScaleInPlace(g4, 0.6))
        self.play(g4.animate.shift((3.5, -2.25, 0)))

        self.wait(5)

        self.play(FadeOut(g1,g2,g3))

        self.play(g4.animate.shift((-3.5, 2.25, 0)))

        self.play(ScaleInPlace(g4, 1))

        self.wait(2)
        self.play(FadeOut(g4))




        # === animation 3: Rectangular structure & subgraphs === #

        # Define the graph
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 2), (1, 3), (1, 4), (1, 6), (2, 3),
                 (2, 4), (2, 5), (3, 4), (3, 5),
                 (3, 6), (3, 8), (4, 5), (4, 6), (4, 7), (5, 6), (5, 8), (5, 7), (6, 7), (6, 8), (7,8)]
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
            edges=edges,
            layout=graph_pos_layout, layout_scale=3, labels=False,
            vertex_config={v: {"fill_color": GRAY, "radius": 0.3} for v in vertices},
            edge_config={(e[0], e[1]): {"stroke_color": BLACK} for e in edges}
        )

        
        self.play(Create(g), run_time=10)
        self.wait(10)
        
        # Vertices and edges to change color
        vertices_to_change = [6, 7, 8]
        edges_to_change = [(6, 7), (6, 8), (7, 8)]

        self.play(
            *[g.vertices[v].animate.set_fill_color(ORANGE) for v in vertices_to_change],
            *[ApplyMethod(g.edges[e].set_color, ORANGE) for e in edges_to_change],
            run_time=4
        )

        self.wait(10)




        # === animation 4: Components in connected and in particular in disconnected graphs === #
        comp_vertices = list(set(vertices) - set(vertices_to_change))
        comp_edges = list(set(edges) - set(edges_to_change))

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
            vertex_config={v: {"fill_color": GRAY, "radius": 0.3} for v in vertices},
            edge_config={(e[0], e[1]): {"stroke_color": BLACK} for e in edges}
        )

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
            *[g_2_comps.vertices[v].animate.set_fill_color(BLUE) for v in vertices_to_change_2],
            *[ApplyMethod(g_2_comps.edges[e].set_color, BLUE) for e in edges_to_change_2],
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

        self.wait(7)

        self.play(FadeOut(g))




        