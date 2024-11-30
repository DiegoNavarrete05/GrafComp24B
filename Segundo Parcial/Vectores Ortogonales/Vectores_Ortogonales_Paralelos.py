from manim import *

class Main(Scene):
    def construct(self):
        # Definir los vectores
        vector_a = Arrow(start=ORIGIN, end=1 * RIGHT + -1 * UP, color=RED, buff=0)
        vector_b = Arrow(start=ORIGIN, end=2 * RIGHT + 2 * UP, color=BLUE, buff=0)

        
        # Etiquetas para los vectores
        nombre_a = MathTex(r"a = (-2, 8, -12)").scale(0.5)
        nombre_a.next_to(vector_a, DOWN * 2)
        nombre_b = MathTex(r"b = (1, -4, 6)").scale(0.5)
        nombre_b.next_to(vector_b, UP)

        self.play(Create(vector_a), Write(nombre_a))
        self.play(Create(vector_b), Write(nombre_b))
        self.wait(1)

        formula_texto = MathTex(r"a \cdot b = a_1 \cdot b_1 + a_2 \cdot b_2").to_edge(UP + LEFT)
        self.play(Write(formula_texto))
        self.wait(1)

        valores_texto = MathTex(r"= (4 \cdot 2) + (-1 \cdot 8)").next_to(formula_texto, DOWN)
        self.play(Write(valores_texto))
        self.wait(1)

        multiplicacion_texto = MathTex(r"= 8 + (-8)").next_to(valores_texto, DOWN)
        self.play(Write(multiplicacion_texto))
        self.wait(1)

        resultado_texto = MathTex(r"= 0").next_to(multiplicacion_texto, DOWN)
        self.play(Write(resultado_texto))
        self.wait(1)

        if 4 * 2 + (-1 * 8) == 0:
            ortogonal_texto = Text("Los vectores son ortogonales (perpendiculares)",font_size=26).to_edge(DOWN)
        else:
            ortogonal_texto = Text("Los vectores no son ortogonales",font_size=26).to_edge(DOWN)
        
        self.play(Write(ortogonal_texto))
        self.wait(2)

        self.play(FadeOut(vector_a), FadeOut(vector_b), FadeOut(nombre_a), FadeOut(nombre_b), 
                  FadeOut(formula_texto), FadeOut(valores_texto), FadeOut(multiplicacion_texto), 
                  FadeOut(resultado_texto), FadeOut(ortogonal_texto))

        vector_a = Arrow(start=ORIGIN, end=6/6 * RIGHT + -18/6 * UP, color=RED, buff=0)
        vector_b = Arrow(start=ORIGIN, end=-4/6 * RIGHT + 12/6 * UP, color=BLUE, buff=0)

        nombre_a = Text("a = (6, -18)").scale(0.5)
        nombre_a.next_to(vector_a, DOWN)
        nombre_b = Text("b = (-4, 12)").scale(0.5)
        nombre_b.next_to(vector_b, LEFT * 2)

        self.play(Create(vector_a), Write(nombre_a))
        self.play(Create(vector_b), Write(nombre_b))
        self.wait(2)

        formula = MathTex("\\frac{a_1}{b_1} = \\frac{a_2}{b_2}").scale(0.7)
        formula.move_to(UP + LEFT * 6)
        
        resultado = MathTex("\\frac{6}{-4} = \\frac{-18}{12}").scale(0.7)
        resultado.next_to(formula, DOWN)

        igualdad = MathTex("1.5 = 1.5").scale(0.7)
        igualdad.next_to(resultado, DOWN)
        

        self.play(Write(formula))
        self.play(Write(resultado))
        self.play(Write(igualdad))
        self.wait(2)

        texto = Text("Son paralelos",font_size=26).to_edge(DOWN)
        self.play(Write(texto))
        self.wait(2)

        self.play(FadeOut(vector_a), FadeOut(vector_b), FadeOut(nombre_a), FadeOut(nombre_b), FadeOut(texto))