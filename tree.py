from manim import *


class Tree(Scene):
    def add_root(self, text):
        outline = Circle(radius=0.4, color=GREEN)
        vertex_text = Text(text, font_size=18).move_to(outline.get_center())
        vertex = Group(outline, vertex_text)
        vertex.shift(UP * 3.0)

        self.play(FadeIn(vertex))

        return outline.get_center()