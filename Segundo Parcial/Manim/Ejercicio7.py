from manim import *
import numpy as np

class Shapes(Scene):
  def construct(self):
        cuadrado_centro = Square(color="red").move_to(np.array([0, 0, 0]))
        cuadrado_arriba = Square(color="blue").to_corner(UP+RIGHT)
        cuadrado_abajo = Square(color="green").to_corner(DOWN+LEFT)
        cuadrado_izquierda = Square(color="white").to_corner(UP+LEFT)
        cuadrado_derecha = Square(color="yellow").to_corner(DOWN+RIGHT)

        self.play(Create(cuadrado_centro), Create(cuadrado_arriba), Create(cuadrado_abajo), Create(cuadrado_izquierda), Create(cuadrado_derecha))
        self.wait(2)

        self.play(FadeOut(cuadrado_centro), FadeOut(cuadrado_arriba), FadeOut(cuadrado_abajo), FadeOut(cuadrado_izquierda), FadeOut(cuadrado_derecha))
        self.wait(1)

        linea = Line(np.array([2, 0, 0]), np.array([-2, 1, 0]))
        self.play(Create(linea))
        self.wait(1)
        self.play(FadeOut(linea))