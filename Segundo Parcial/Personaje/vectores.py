from manim import *

class VerificarVectores(Scene):
    def construct(self):
        # Definir los vectores
        vector_a = Arrow(start=ORIGIN, end=1 * RIGHT + -2 * UP, color=YELLOW, buff=0)
        vector_b = Arrow(start=ORIGIN, end=2 * RIGHT + 4 * UP, color=BLUE, buff=0)

        # Etiquetas para los vectores
        nombre_a = Text("a = (6, -18)").scale(0.5)
        nombre_a.next_to(vector_a, DOWN)
        nombre_b = Text("b = (4, 12)").scale(0.5)
        nombre_b.next_to(vector_b, UP)

        # Mostrar los vectores y etiquetas
        self.play(Create(vector_a), Write(nombre_a))
        self.play(Create(vector_b), Write(nombre_b))
        self.wait(2)

        # Calcular si son ortogonales o paralelos
        a = [6, -18]
        b = [4, 12]
        
        # Producto punto
        producto_punto = a[0] * b[0] + a[1] * b[1]
        
        # Proporcionalidad (si ambos componentes tienen el mismo factor)
        if producto_punto == 0:
            texto = Text("Los vectores son ortogonales (perpendiculares)").to_edge(DOWN)
        elif a[0] / b[0] == a[1] / b[1]:
            texto = Text("Los vectores son paralelos").to_edge(DOWN)
        else:
            texto = Text("Los vectores no son ortogonales ni paralelos").to_edge(DOWN)
        
        # Mostrar el texto
        self.play(Write(texto))
        self.wait(2)

        # Desvanecer todos los elementos
        self.play(FadeOut(vector_a), FadeOut(vector_b), FadeOut(nombre_a), FadeOut(nombre_b), FadeOut(texto))
