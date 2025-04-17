from manim import *

class Credits(Scene):
    def construct(self):
        roll_text = Text("Visualization created by Debra Ritter\n"
                     "For CSC4330 - Programming Language Concepts\n"
                         "April 2025.\n\n"
                         "Github: https://github.com/DebraBeat/recursion_visualization/",
                         font_size=24)

        self.play(Write(roll_text))
        self.wait(5)
        self.play(FadeOut(roll_text))
        self.wait(1)