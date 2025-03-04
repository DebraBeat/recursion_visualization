from manim import *


class Stack(Scene):
    def construct(self):
        stack = Group()

        def push(element):
            if len(stack) == 0:
                element.move_to(ORIGIN + RIGHT * 6.0)
            else:
                element.move_to(stack.get_top() + (UP * 0.33 / 2))

            stack.add(element)
            self.play(FadeIn(element))

        def pop():
            if len(stack) > 0:
                element = stack[-1]
                self.play(FadeOut(element))
                stack.remove(element)

        for i in range(5):
            rect = Rectangle(width=1, height=0.33)
            rect.set_stroke(ORANGE)
            text = Text("Test", color=ORANGE).scale(0.33)
            text.move_to(rect.get_center())
            ele = Group(rect, text)
            push(ele)

        for i in range(5):
            pop()
