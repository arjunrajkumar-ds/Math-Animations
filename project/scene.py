from manim import *

class CircleToSquare(Scene):
    def construct(self):
        circle = Circle() # Creates a circle
        circle.set_fill(GREEN, opacity=.5) # Sets the colour & transparency
        
        square = Square() # Creates a square
        square.rotate(PI / 2) # Rotation animation

        self.play(Create(circle))
        self.play(Transform(circle, square)) # Transform method to interpolate shapes
        self.play(FadeOut(square)) # Fade out animation

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=.5)

        square = Square()
        square.set_fill(BLUE, opacity=.5)
        square.next_to(circle, DOWN, buff=.5) # Positioning method with directional argument

        self.play(Create(circle), Create(square))
        self.play(square.animate.flip(RIGHT), circle.animate.flip(UP))

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI/4)) # Rotate animation method with .animate prepend
        self.play(Transform(square, circle))
        self.play(square.animate.set_fill(PINK, opacity=.5)) # Fill method with prepend

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=RED, fill_opacity=.7).shift(2 * LEFT)
        right_square = Square(color=BLUE, fill_opacity=.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
            # Left 
        )
        self.wait()

class HollowPurple(Scene):
    def construct(self):
        left_red = Circle(color=RED, fill_opacity=0.9).shift(2 * LEFT)
        right_blue = Circle(color=BLUE, fill_opacity=.9).shift(2 * RIGHT)
        self.play(
            Rotate(left_red, angle=PI), Rotate(right_blue, angle=-PI), run_time=2
        )

class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(.5)
        self.replacement_transform()

    # You can define various functions within your Class; transform / replacement_transform
    # Within the functions, Mobjects can be created / animated
    # Functions can be chained within the self-construct