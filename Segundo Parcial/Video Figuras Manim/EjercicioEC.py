from manim import *

class ejercicioEC(Scene):
    def construct(self):
        # Título y fórmula de Basel
        title = Text("Diego Argel Navarrete Godines")
        basel = MathTex(
            r"\sum_{k=1}^\infty \frac{1}{k^2} = \frac{\pi^2}{6}"
        )
        grupo = VGroup(title, basel).arrange(DOWN)
        
        # Animar la aparición del título y la fórmula
        self.play(Write(title), FadeIn(basel, shift=UP))
        self.wait(2)
        
        # Desaparecer título y fórmula
        self.play(FadeOut(grupo))  # Usar FadeOut sobre el grupo (título y fórmula)
        self.wait()

        # Animar el cuadrado
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait(2)  # Esperar para visualizar el resultado de la transformación
        
        self.play(FadeOut(square))
        self.wait()

        decimal = DecimalNumber(0, show_ellipsis=True, num_decimal_places=3, include_sign=True)
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))

        self.add(square, decimal)

        self.play(square.animate.to_edge(DOWN), rate_func=there_and_back, run_time=5)
        self.wait()

        self.play(FadeOut(square), FadeOut(decimal))
        self.wait()

        circulo = Circle()
        self.play(Create(circulo))  # Crear círculo
        self.wait()
        self.play(FadeOut(circulo))  # Desaparecer círculo

        rect = Rectangle(color="red", height=3, width=1)
        self.play(Create(rect))
        self.wait()
        self.play(FadeOut(rect))

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