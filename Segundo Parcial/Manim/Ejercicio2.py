from manim import *

class SquareToCircle(Scene):
    def construct(self):
        # Crear un círculo y un cuadrado
        circle = Circle()
        square = Square()
        
        # Configurar el cuadrado
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        
        # Configurar el color del círculo
        circle.set_fill(PINK, opacity=0.5)

        # Animar la creación del cuadrado
        self.play(Create(square))
        # Transformar el cuadrado en un círculo
        self.play(Transform(square, circle))
        # Desvanecer el círculo
        self.play(FadeOut(square))
