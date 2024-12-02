from manim import *

class Aa(Scene):
    def construct(self):
        self.camera.background_color = "#BDD2E4"
        title = Text("""
                    Universidad Autónoma del Estado de México
                    
                            Centro Universitario UAEM Zumpango
                     
                                        Ingeniería en Computación
                     
                                        Graficación Computacional
        """, font_size=28,color=BLACK)
        title.to_edge(UP)
        name_text = Text("Transform", font_size=36, color=BLACK)
        additional_text = Text("""
        Alumno: Diego Argel Navarrete Godines
        
        Profesora: Hazem Álvarez Rodríguez
                
        Periodo: 24B
        """, font_size=24,color=BLACK)
        additional_text.next_to(name_text, ORIGIN + DOWN, buff=1)
    
        self.play(Write(title))
        self.play(FadeIn(name_text))
        self.wait(2)
        self.play(name_text.animate.scale(1.2).set_color(YELLOW))
        self.wait(1)
        self.play(name_text.animate.scale(1/1.2).set_color(BLACK))
        self.wait(1)
        self.play(FadeIn(additional_text))
        self.wait(3)
        
        self.play(FadeOut(name_text), FadeOut(title), FadeOut(additional_text))
        self.wait(1)
        self.camera.background_color = BLACK
        
class TextLike1DArrays(Scene):
    def construct(self):
        # Fondo en hexadecimal
        self.camera.background_color = "#FF5733"

        text = Text("Te"), Text("xt")
        for i in text:
            self.play(FadeIn(i))
            self.wait()
            self.play(FadeOut(i))
        self.wait()


class TextLike2DArraysV1(Scene):
    def construct(self):
        # Fondo en hexadecimal
        self.camera.background_color = "#33FF57"

        text = Text("Te"), Text("xt")
        self.play(FadeIn(text[0][0]))
        self.play(FadeIn(text[0][1]))
        self.play(FadeIn(text[1][0]))
        self.play(FadeIn(text[1][1]))
        self.wait()


class TextLike2DArraysV2(Scene):
    def construct(self):
        # Fondo en hexadecimal
        self.camera.background_color = "#3357FF"

        text = Text("Te"), Text("xt")
        for i in text:
            for j in i:
                self.play(FadeIn(j))

        self.wait()


class TextLike2DArraysV3(Scene):
    def construct(self):
        # Fondo en hexadecimal
        self.camera.background_color = "#FF33A1"

        text = Text("Te"), Text("xt")
        for i in range(len(text)):
            for j in range(len(text[i])):
                self.play(FadeIn(text[i][j]))

        self.wait()


class TransformIssues(Scene):
    def construct(self):
        # Fondo en hexadecimal
        self.camera.background_color = "#A133FF"

        text_1 = VGroup(*[Text(char) for char in "ABC"])
        text_2 = Text("B")  # Crear texto para transformar
        text_1.arrange(RIGHT, buff=0.5)
        text_2.next_to(text_1, UP, buff=1)  # Posicionar text_2 sobre text_1

        self.play(
            *[FadeIn(text_1[i]) for i in [0, 2]],
            FadeIn(text_2)  # Aparece text_2
        )
        self.wait()

        text_1_1_copy = Text("B")\
            .match_style(text_1[1])\
            .match_width(text_1[1])\
            .move_to(text_1[1])

        self.play(ReplacementTransform(text_2, text_1_1_copy))

        self.remove(text_1_1_copy)
        self.add(text_1[1])
        self.wait()
