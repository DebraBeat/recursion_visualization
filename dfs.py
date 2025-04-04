from manim import *
from stack import Stack


class DFS(Scene):
    """
    Class for DFS visualization
    """
    def construct(self):
        """
        construct method needed for manim. It is equivalent to "main".
        :return: None
        """

        # Relevant variables
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        edges_backwards = [(e[1], e[0]) for e in edges]
        edges = edges + edges_backwards

        adj = {i: [] for i in vertices}
        for e in edges:
            adj[e[0]].append(e[1])

        v = Graph(vertices, [])
        g = Graph(vertices, edges, layout="circular")

        stack = Group()
        stack_text = Text('Stack', color=BLUE)
        stack_outline = Rectangle(width=1.2, height=3.4, color=BLUE).shift(ORIGIN + RIGHT * 6.0 + UP * 0.3)
        stack_text.move_to(ORIGIN + RIGHT * 6.0)
        stack_text.shift(UP * 3.0)

        listing = Code( # code listing of fibonacci sequence
            "dfs-listing.py",
            formatter_style="emacs",
            background="window",
            language="python",
            background_config={"stroke_color": WHITE},
            paragraph_config={"font": "Noto Sans Mono"},
        ).scale(0.5).shift(LEFT * 4.5 + UP)

        # Intro text blocks
        intro_text = Text("Recursion Visualization: Depth First Search",
                    font_size=20).shift(UP * 2.5)
        self.play(Write(intro_text))
        self.wait(2)

        text = Text("Depth First Search (DFS for short) is an algorithm for "
                    "traversing vertices in a graph.", font_size=20)
        self.play(Write(text))
        self.wait(4)

        self.play(FadeOut(intro_text, text))

        text = Text("Graphs consist of vertices and edges. Vertices can be "
                    "thought of as a collection of dots."
                    , font_size=20).shift(UP * 2.5)
        self.play(Write(text))
        self.wait(4)

        self.play(Create(v))
        self.play(FadeOut(text))

        text = Text("Edges can be thought of as the lines connecting various "
                    "vertices to each other.", font_size=20).shift(UP * 2.5)
        self.play(Write(text))

        # Graph creation
        self.remove(v)
        self.play(Create(g))
        annotation_group = Group()
        for vertex in vertices:
            annotation = Text(f"{vertex}", font_size=16)
            annotation_group.add(annotation)
            annotation.next_to(g.vertices[vertex], (DOWN * 0.4) + (RIGHT * 0.2))  # Position annotation near the vertex
            self.play(Write(annotation))

        self.wait(4)
        self.play(FadeOut(text))

        text = Text("DFS is a way to traverse these vertices. Given a vertex "
                    "\nand it's edges, it travels the first edge it encounters, "
                    "\ntravels the first edge on the second vertex, and so on."
                    , font_size=20).shift(UP * 3.0)

        self.play(Write(text))
        self.wait(4)
        self.play(FadeOut(text))

        text = Text("DFS is used in Garbage Collection. Using the mark and sweep\n"
                    "method, each cell in memory is a vertex, and each pointer\n"
                    "to other cells is an edge. All vertices are thought of as\n"
                    "garbage except for the starting cell. The edges from the start\n"
                    "are traversed and marked as non-garbage. The collector then\n"
                    "deallocates all non-marked cells.", font_size=20).shift(UP * 3.0)

        self.play(Write(text))
        self.wait(8)
        self.play(FadeOut(text))

        text = Text("Let's display a listing of the DFS code for reference.",
                    font_size=20).shift(UP * 3.0)
        self.play(Write(text))
        self.play(Create(listing))
        self.wait(8)
        self.play(FadeOut(text))

        text = Text("DFS is implemented with a call stack. Let's visualize the stack\n"
                    "and traverse the given graph.", font_size=20).shift(UP * 2.5)

        # Stack creation
        self.play(Write(text))
        self.play(FadeIn(stack_text, stack_outline))
        self.wait(4)
        self.play(FadeOut(text))

        def dfs(g, adj, vertex, seen):
            """
            dfs traversal in manim

            :param g: manim representation of graph
            :param adj: adjacency list representation of a graph
            :param vertex: vertex to run dfs on
            :param seen: set of all seen vertices
            :return: None
            """
            g.vertices[vertex].set_fill(GREEN)
            self.wait(0.5)
            seen.add(vertex)

            for neighbor in adj[vertex]:
                edge = (vertex, neighbor)
                edge_backwards = (neighbor, vertex)

                if neighbor not in seen and edge in g.edges:
                    g.edges[edge].animate.set_stroke(BLUE)
                    g.edges[edge_backwards].set_stroke(BLUE)
                    self.wait(2)
                    Stack.push(self, stack, str(neighbor))
                    dfs(g, adj, neighbor, seen)

            g.vertices[vertex].set_fill(BLUE)
            self.wait(0.5)
            Stack.pop(self, stack)

        # Perform DFS
        Stack.push(self, stack, '1')
        dfs(g, adj, 1, {1})
        Stack.pop(self, stack)
        self.play(FadeOut(stack_text, stack_outline, listing))
        self.wait(4)

        text = Text("All visited vertices and edges have been marked. \n"
                    "Redundant edges have not been marked, because the "
                    "vertices have already been visited.", font_size=20).shift(UP * 2.5)
        self.play(Write(text))
        self.wait(4)
        self.play(FadeOut(text, g, annotation_group))

        # Added this section relating everything to PLC for posterity.
        concept_group = Group()  # group for concepts
        list_header = (Text("List of Programming Language Concepts used:", font_size=24)
                       .move_to(UP * 2.5))
        concept_group.add(list_header)

        concept1 = (Text("- Recursive functions: DFS is "
                         "recursive. A fundamental subject in PLC", font_size=20)
                    .move_to(UP * 1.5))
        concept_group.add(concept1)

        concept2 = (Text("- DFS is used to mark non-garbage memory in the "
                         " mark-and-sweep method of garbage collection.", font_size=20)
                    .move_to(UP * 1.0))
        concept_group.add(concept2)

        concept3 = (Text("- Dynamic Heap Allocation and Dynamic chains: "
                         "Memory on the heap must be allocated with "
                         "call stack pushes\n and deallocated with "
                         "call stack pops. This also creates dynamic chains.", font_size=20)
                    .move_to(UP * 0.5))
        concept_group.add(concept3)

        for i in range(len(concept_group)):
            self.play(Write(concept_group[i]))
            self.wait(3)

        self.play(FadeOut(list_header, concept_group))
        self.wait(3)
