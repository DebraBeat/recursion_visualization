from manim import *


class Tree(Scene):
    def add_root(self, text):
        vertex_outline = Circle(radius=0.4, color=GREEN)
        vertex_text = Text(text, font_size=18).move_to(vertex_outline.get_center())
        vertex = Group(vertex_outline, vertex_text)

        vertex.shift(UP * 3.0)

        self.play(Create(vertex_outline), Write(vertex_text))

        return vertex

    def remove_root(self, root):
        self.play(FadeOut(root))

    def add_left_child(self, text, parent):
        vertex_outline = Circle(radius=0.4, color=GREEN)
        vertex_text = Text(text, font_size=18).move_to(vertex_outline.get_center())
        parent_coor = parent[0].get_center()
        left_child = Group(vertex_outline, vertex_text)

        left_child.move_to(parent_coor)
        left_child.shift((DOWN + LEFT) * 1.1)

        edge = Line(vertex_outline.get_center(), parent_coor, color=LIGHT_BROWN).scale(0.5)

        self.play(Create(left_child[0]), Write(left_child[1]), Create(edge))

        left_child.add(edge)

        return left_child

    def add_right_child(self, text, parent):
        vertex_outline = Circle(radius=0.4, color=GREEN)
        vertex_text = Text(text, font_size=18).move_to(vertex_outline.get_center())
        parent_coor = parent[0].get_center()
        right_child = Group(vertex_outline, vertex_text)

        right_child.move_to(parent_coor)
        right_child.shift((DOWN + RIGHT) * 1.1)

        edge = Line(vertex_outline.get_center(), parent_coor, color=LIGHT_BROWN).scale(0.5)

        self.play(Create(right_child[0]), Write(right_child[1]), Create(edge))

        right_child.add(edge)

        return right_child

    def replace_text(self, new_text, vertex):
        new_vertex_outline = vertex[0]
        new_vertex_edge = vertex[2]
        new_vertex_text = Text(new_text, font_size=18).move_to(new_vertex_outline.get_center())
        new_vertex = Group(new_vertex_outline, new_vertex_text, new_vertex_edge)

        self.remove(vertex)
        self.remove(vertex[1])
        self.add(new_vertex[0], new_vertex[2])
        self.play(FadeIn(new_vertex[1]))

        return new_vertex

    def remove_child(self, vertex):
        self.play(FadeOut(vertex))