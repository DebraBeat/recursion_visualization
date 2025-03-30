from manim import *


class Stack(Scene):
    def construct(self):
        stack = Group()

        for i in range(5):
            rect = Rectangle(width=1, height=0.33)
            rect.set_stroke(ORANGE)
            text = Text("Test", color=ORANGE).scale(0.33)
            text.move_to(rect.get_center())
            ele = Group(rect, text)
            self.push(stack, ele)

        for i in range(5):
            self.pop(stack)

    def push(self, stack, text):
        rect = Rectangle(width=1, height=0.33)
        rect.set_stroke(BLUE)
        text = Text(text, color=WHITE).scale(0.30)
        text.move_to(rect.get_center())
        ele = Group(rect, text)

        if len(stack) == 0:
            ele.move_to(ORIGIN + RIGHT * 6.0)
        else:
            ele.move_to(stack.get_top() + (UP * 0.33 / 2))

        stack.add(ele)
        self.play(Create(rect), Write(text))

    def pop(self, stack):
        if len(stack) > 0:
            element = stack[-1]
            self.play(FadeOut(element))
            stack.remove(element)

        # for i in range(5):
        #     rect = Rectangle(width=1, height=0.33)
        #     rect.set_stroke(ORANGE)
        #     text = Text("Test", color=ORANGE).scale(0.33)
        #     text.move_to(rect.get_center())
        #     ele = Group(rect, text)
        #     push(ele)
        #
        # for i in range(5):
        #     pop()

# class Driver(Scene):
#
#     def construct(self):
#         stack = Group()
#         mobStack = Stack()
#
#         for i in range(5):
#             rect = Rectangle(width=1, height=0.33)
#             rect.set_stroke(ORANGE)
#             text = Text("Test", color=ORANGE).scale(0.33)
#             text.move_to(rect.get_center())
#             ele = Group(rect, text)
#             mobStack.push(stack, ele)
#
#         for i in range(5):
#             mobStack.pop(stack)
