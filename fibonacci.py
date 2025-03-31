from manim import *
import numpy as np
from stack import Stack
from tree import Tree

hashmap = {0: 1, 1: 1}


def fib(i: int) -> int:
    if i in hashmap:
        return hashmap[i]

    hashmap[i] = fib(i - 1) + fib(i - 2)

    return hashmap[i]


class FibonacciRegular(Scene):
    def construct(self):
        colors = [BLUE, GOLD, GREEN, PINK, TEAL]
        color_index = 0
        scale_factor = 1
        group = Group()

        intro_text = Text("The Fibonacci sequence is a sequence of numbers named after "
                          "the mathematician\n \"Fibonacci\" (he only had one word for "
                          "his name).", font_size=20)
        intro_text.shift(UP * 2.0)

        definition_text = Text("The sequence is defined as follows:                         "
                               "\n\n Let the "
                               "first two elements each be equal to one.\n Every "
                               "element afterwards is the sum of the previous "
                               "two.\n In other words F_0 = 1, F_1 = 1, F_n = "
                               "F_{n-1} + F_{n-2}", font_size=20)

        transition_text = Text("If we set make squares with the length of a side being"
                               "a fibonacci number we get the following:", font_size=20)

        self.play(Write(intro_text))
        self.wait(5)
        self.play(Write(definition_text))
        self.wait(5)
        self.play(FadeOut(intro_text))
        self.play(FadeOut(definition_text))

        self.play(Write(transition_text))
        self.wait(2)
        self.play(FadeOut(transition_text))

        for i in range(0, 10):
            curr_fib = np.sqrt(fib(i))
            # next_fib = np.sqrt(fib(i + 1))
            scale_factor = 1.0 / curr_fib
            # next_scale_factor = 1.0 / next_fib
            # next_rect = Rectangle(width=next_fib, height=next_fib).scale(next_scale_factor)

            rect = Rectangle(width=curr_fib, height=curr_fib).scale(scale_factor)
            rect.set_fill(colors[color_index], opacity=0.5)
            color_index = (color_index + 1) % len(colors)

            t = Text(f'{i}')
            b = Brace(rect)
            equals = Text('=')
            b_text = Text(f'{fib(i)}')
            f_text = Text(f'Fibonacci of {i}')
            f_text.shift(DOWN * 1.6)
            equals.shift(DOWN * 1.25)
            b_text.shift(DOWN * 1.25)
            t.shift(UP)

            self.play(FadeIn(t))
            self.play(group.animate.scale(scale_factor))
            self.play(Create(rect))
            self.play(FadeIn(b, f_text))
            self.play(FadeOut(f_text))
            self.play(FadeIn(equals))
            self.play(FadeOut(equals))
            self.play(FadeIn(b_text))
            self.wait(1)

            rect = Group(rect, t, b, b_text)
            group.add(rect)
            self.play(group.animate.shift(LEFT))


class FibonacciWithStack(Scene):
    def construct(self):
        stack = Group()
        cs = []  # call stack
        fib_idx = 4
        listing = Code(
            "example.py",
            formatter_style="emacs",
            background="window",
            language="python",
            background_config={"stroke_color": WHITE},
            paragraph_config={"font": "Noto Sans Mono"},
        ).scale(0.5).shift(LEFT * 4 + UP * 2.5)

        # Begin main part of program
        # In this program, we'll go through the fibonacci of four
        text = Text("The Fibonacci sequence can also be visualized with "
                           "Stacks and Trees.", font_size=20)
        text.shift(UP)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))

        stack_text = Text('Stack', color=BLUE)
        stack_outline = Rectangle(width=1.2, height=2.8, color=BLUE).shift(ORIGIN + RIGHT * 6.0 + UP)
        stack_text.move_to(ORIGIN + RIGHT * 6.0)
        stack_text.shift(UP * 3.0)
        self.play(FadeIn(stack_text, stack_outline))
        self.wait(2)

        text = Text("Each call of the Fibonacci Sequence can visualized "
                    "as\npushing an element onto the call stack.", font_size=20)
        self.play(Write(text))
        Stack.push(self, stack, f"fib({fib_idx})")
        self.wait(4)
        self.play(FadeOut(text))

        text = Text("Each call of the Fibonacci Sequence can also be visualized\n"
                    "as creating a node in a call tree.", font_size=20).shift(DOWN)
        self.play(Write(text))
        root = Tree.add_root(self, f'fib({fib_idx})')
        lc = Tree.add_left_child(self, f'fib({fib_idx - 1})', root)
        Stack.push(self, stack, f'fib({fib_idx - 1})')
        rc = Tree.add_right_child(self, f'fib({fib_idx - 2})', root)
        Stack.push(self, stack, f'fib({fib_idx - 2})')
        self.wait(4)
        self.play(FadeOut(text))

        text = Text("Since nodes and stack elements are the same, once we have\n"
                    "calculated them, we can remove them.\n"
                    "(Remember that fib(1) = 1)", font_size=20).shift(DOWN)
        self.play(Write(text))
        rrc = Tree.add_right_child(self, f'fib({fib_idx - 3})', rc)
        Stack.push(self, stack, f'fib({fib_idx - 3})')
        self.wait(3)
        rrc = Tree.replace_text(self, "1", rrc)
        Stack.change(self, stack, "1")
        # Stack.pop(self, stack)
        # Stack.push(self, stack, "1")
        Tree.remove_child(self, rrc)
        Stack.pop(self, stack)
        Stack.quick_pop(self, stack)
        Tree.remove_child(self, rc)
        Stack.pop(self, stack)
        Tree.remove_child(self, lc)
        Stack.pop(self, stack)
        Tree.remove_root(self, root)
        Stack.pop(self, stack)
        self.wait(3)
        self.play(FadeOut(text))

        text = Text("Let's load the code for the Fibonacci sequence and go\n"
                    "through the sequence for four.", font_size=20)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeIn(listing))
        self.play(FadeOut(text))