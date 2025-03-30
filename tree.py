from manim import *


class Tree(Scene):
    def add_root(self, text):
        vertex_outline = Circle(radius=0.4, color=GREEN)
        vertex_text = Text(text, font_size=18).move_to(vertex_outline.get_center())
        vertex = Group(vertex_outline, vertex_text)

        vertex.shift(UP * 3.0)

        self.play(Create(vertex_outline), Write(vertex_text))

        return vertex

    def remove_vertex(self, vertex):
        self.play(FadeOut(vertex))

    def add_left_child(self, text, parent):
        vertex_outline = Circle(radius=0.4, color=GREEN)
        vertex_text = Text(text, font_size=18).move_to(vertex_outline.get_center())
        parent_coor = parent[0].get_center()
        left_child = Group(vertex_outline, vertex_text)

        left_child.move_to(parent_coor)
        left_child.shift((DOWN + LEFT) * 1.1)

        edge = Line(vertex_outline.get_center(), parent_coor, color=LIGHT_BROWN).scale(0.5)

        self.play(Create(left_child[0]), Create(edge), Write(left_child[1]))

        return left_child

    def add_right_child(self, text, parent):
        vertex_outline = Circle(radius=0.4, color=GREEN)
        vertex_text = Text(text, font_size=18).move_to(vertex_outline.get_center())
        parent_coor = parent[0].get_center()
        left_child = Group(vertex_outline, vertex_text)

        left_child.move_to(parent_coor)
        left_child.shift((DOWN + RIGHT) * 1.1)

        edge = Line(vertex_outline.get_center(), parent_coor, color=LIGHT_BROWN).scale(0.5)

        self.play(Create(left_child[0]), Create(edge), Write(left_child[1]))

        return left_child
