from manim import *
import numpy as np
from stack import Stack # Custom stack class for easy stack visualization
from tree import Tree # Custom tree class for easy tree visualization

# Hashmap to used in fib method
hashmap = {0: 1, 1: 1}


def fib(i: int) -> int:
    """
    Basic optimized fibonacci code.
    :param i:
    :return:
    """
    if i in hashmap:
        return hashmap[i]

    hashmap[i] = fib(i - 1) + fib(i - 2)

    return hashmap[i]


class FibonacciRegular(Scene):
    def construct(self):
        colors = [BLUE, GOLD, GREEN, PINK, TEAL] # A list of colors to iterate
        color_index = 0
        group = Group() # Group for previous rectangles

        text = Text("Recursion Visualization: The Fibnonacci sequence.",
                    font_size=20).shift(UP * 2.0)
        self.play(Write(text))
        self.play(FadeOut(text))

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

        # Next two blocks of code are writing relevant information
        self.play(Write(intro_text))
        self.wait(5)
        self.play(Write(definition_text))
        self.wait(5)
        self.play(FadeOut(intro_text))
        self.play(FadeOut(definition_text))

        self.play(Write(transition_text))
        self.wait(2)
        self.play(FadeOut(transition_text))

        # Run the rectangle creation for the first eight fibonacci
        # sequence elements.
        for i in range(0, 8):
            curr_fib = fib(i)
            scale_factor = 1.0 / curr_fib

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

        self.play(FadeOut(group))
        self.wait(2)


class FibonacciWithStack(Scene):
    def construct(self):
        stack = Group() # The visualization of the call stack
        cs = []  # call stack
        fib_idx = 4 # We'll be doing a visualization of fib(4)
        listing = Code( # code listing of fibonacci sequence
            "example.py",
            formatter_style="emacs",
            background="window",
            language="python",
            background_config={"stroke_color": WHITE},
            paragraph_config={"font": "Noto Sans Mono"},
        ).scale(0.5)

        # Begin main part of program
        # In this program, we'll go through the fibonacci of four
        text = Text("The Fibonacci sequence can also be visualized with "
                           "Stacks and Trees.", font_size=20)
        text.shift(UP)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))

        # Initialize stack visualization
        stack_text = Text('Stack', color=BLUE)
        stack_outline = Rectangle(width=1.2, height=3.4, color=BLUE).shift(ORIGIN + RIGHT * 6.0 + UP * 0.3)
        stack_text.move_to(ORIGIN + RIGHT * 6.0)
        stack_text.shift(UP * 3.0)
        self.play(FadeIn(stack_text, stack_outline))
        self.wait(2)

        # Example fibonacci run before the real thing
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
        lc = Tree.add_left_child(self, f'fib({fib_idx - 1})', root, 1.0)
        Stack.push(self, stack, f'fib({fib_idx - 1})')
        rc = Tree.add_right_child(self, f'fib({fib_idx - 2})', root, 1.0)
        Stack.push(self, stack, f'fib({fib_idx - 2})')
        self.wait(4)
        self.play(FadeOut(text))

        text = Text("Since nodes and stack elements are the same, once we have\n"
                    "calculated them, we can remove them.\n"
                    "(Remember that fib(1) = 1)", font_size=20).shift(DOWN)
        self.play(Write(text))
        rrc = Tree.add_right_child(self, f'fib({fib_idx - 3})', rc, 1.0)
        Stack.push(self, stack, f'fib({fib_idx - 3})')
        self.wait(3)
        rrc = Tree.replace_text(self, "1", rrc)
        Stack.change(self, stack, "1")
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

        # Load fibonacci listing
        text = Text("Let's load the code for the Fibonacci sequence",
                    font_size=20).shift(DOWN)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeIn(listing))
        self.play(FadeOut(text))

        text = Text("Let's go over the code to understand it's recursiveness."
                    , font_size=20).shift(DOWN)
        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(text))

        text = Text("Now let's visualize the fibonacci sequence for 4.",
                    font_size=20).shift(DOWN)
        self.play(Write(text))
        self.play(listing.animate.shift(LEFT * 4 + UP * 2.5))
        self.play(FadeOut(text))

        vertex_list = [] # list of vertices for use when the call stack is empty
        root = Tree.add_root(self, f'fib({fib_idx})')
        vertex_list.append([root, fib_idx, True])   # Add the root, the current
                                                    # fib num, and True because
                                                    # this is the root.
        Stack.push(self, stack, f'fib({fib_idx})') # push the associated
                                                        # stack number
        cs.append([root, fib_idx, True]) # Do the same for the call stack
        val_group = Group() # We'll use this to replace the vertices with
                            # fib values.
        i = 1.0 # Needed for hacky way of getting tree to visualize correctly

        while cs:
            curr_vertex, curr_val, is_root = cs.pop()

            # Pass over the rest of the while loop if we're at a leaf
            if curr_val == 0 or curr_val == 1:
                continue

            # Add left child
            lc = Tree.add_left_child(self, f"fib({curr_val - 1})", curr_vertex, i)
            cs.append([lc, curr_val - 1, False])
            vertex_list.append([lc, curr_val - 1, False])
            Stack.push(self, stack, f"fib({curr_val - 1})")

            # Add right child
            rc = Tree.add_right_child(self, f"fib({curr_val - 2})", curr_vertex, i)
            cs.append([rc, curr_val - 2, False])
            vertex_list.append([rc, curr_val - 2, False])
            Stack.push(self, stack, f"fib({curr_val - 2})")

            # Now that i is 2 the vertices will be twice as close
            i = 2

        # Go through the tree and replace every child with it's
        # associated fib value.
        while vertex_list:
            curr_vertex, curr_val, is_root = vertex_list.pop()

            if not is_root:
                coor = curr_vertex[1].get_center()
                t = Text(f'{fib(curr_val)}', font_size=18).move_to(coor)
                Tree.remove_child(self, curr_vertex)
                val_group.add(t)
                self.play(FadeIn(val_group[-1]))
                Stack.pop(self, stack)

        # Replace the root with it's associate fib value.
        root_val, root_coor = 4, root[1].get_center()
        Tree.remove_root(self, root)
        root_txt = Text(f'{fib(root_val)}', font_size=18).move_to(root_coor)
        self.play(FadeIn(root_txt))
        Stack.pop(self, stack)

        # Remove everything except the root value.
        self.play(FadeOut(val_group, stack_text, stack_outline, listing))

        final_equation = Text(f'Fibonacci(4) = 5')

        self.play(Transform(root_txt, final_equation))
        self.wait(4)
        self.play(FadeOut(root_txt, final_equation))

        # Added this section relating everything to PLC for posterity.
        concept_group = Group()  # group for concepts
        list_header = (Text("List of Programming Language Concepts used:", font_size=24)
                       .move_to(UP * 2.5))
        concept_group.add(list_header)

        concept1 = (Text("- Recursive functions: The fibonacci sequence is "
                        "recursive. A fundamental subject in PLC", font_size=20)
                   .move_to(UP * 1.5))
        concept_group.add(concept1)

        concept2 = (Text("- Dynamic Heap Allocation and Deallocation: "
                        "Memory on the heap must be allocated with "
                        "call stack pushes\n and deallocated with "
                        "call stack pops.", font_size=20)
                   .move_to(UP * 1.0))
        concept_group.add(concept2)

        concept3 = (Text("- Dynamic Chains: Each element besides the last on "
                        "the call stack is chained to an element "
                        "below it.", font_size=20)
                   .move_to(UP * 0.5))
        concept_group.add(concept3)

        for i in range(len(concept_group)):
            self.play(Write(concept_group[i]))
            self.wait(3)

        self.play(FadeOut(list_header, concept_group))
        self.wait(3)