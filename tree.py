from manim import *


class Tree(Scene):
    """
    This module defines the tree class, which allows you to create representations
    of trees in manim.
    """
    def add_root(self, text):
        """
        Create a root vertex. This has NO EDGES since it has no parent.
        :param text: the text to go in the center of the vertex
        :return none
        """
        vertex_outline = Circle(radius=0.4, color=GREEN)
        vertex_text = Text(text, font_size=18).move_to(vertex_outline.get_center())
        vertex = Group(vertex_outline, vertex_text)

        vertex.shift(UP * 3.0)

        self.play(Create(vertex_outline), Write(vertex_text))

        return vertex

    def remove_root(self, root):
        """
        Remove the root vertex from the screen.
        :param root: the root (a group of mobjects)
        :return none
        """
        self.play(FadeOut(root))

    def add_left_child(self, text, parent, i):
        """

        :param text: the text to be added in the center of the vertex
        :param parent:
        :param i: hacky integer which controls spacing on tree levels. This is
        so two vertices don't intersect or overlap
        :return: none
        """
        vertex_outline = Circle(radius=0.4, color=GREEN)
        vertex_text = Text(text, font_size=18).move_to(vertex_outline.get_center())
        parent_coor = parent[0].get_center()
        left_child = Group(vertex_outline, vertex_text)

        left_child.move_to(parent_coor)
        left_child.shift(DOWN + (LEFT * 0.9 / i))

        edge = Line(vertex_outline.get_center(), parent_coor, color=LIGHT_BROWN).scale(0.5)

        self.play(Create(left_child[0]), Write(left_child[1]), Create(edge))

        left_child.add(edge)

        return left_child

    def add_right_child(self, text, parent, i):
        """
        :param text: the text to be added in the center of the vertex
        :param parent:
        :param i: hacky integer which controls spacing on tree levels. This is
        so two vertices don't intersect or overlap
        :return: none
        """
        vertex_outline = Circle(radius=0.4, color=GREEN)
        vertex_text = Text(text, font_size=18).move_to(vertex_outline.get_center())
        parent_coor = parent[0].get_center()
        right_child = Group(vertex_outline, vertex_text)

        right_child.move_to(parent_coor)
        right_child.shift(DOWN + (RIGHT * 0.9 / i))

        edge = Line(vertex_outline.get_center(), parent_coor, color=LIGHT_BROWN).scale(0.5)

        self.play(Create(right_child[0]), Write(right_child[1]), Create(edge))

        right_child.add(edge)

        return right_child

    def replace_text(self, new_text, vertex):
        """
        This is a method to replace the text inside the vertex.
        :param new_text: The text to be visible and replace the old text.
        :param vertex: The vertex whose text will be replaced
        :return: none
        """
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
        """
        Remove a given vertex
        :param vertex: The vertex to be removed.
        :return: None
        """
        self.play(FadeOut(vertex))