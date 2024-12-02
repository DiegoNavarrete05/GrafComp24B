from manim import *
import numpy as np
class UnifiedAnimationsWithBackgroundColors(Scene):
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

        # TransformationText1V1
        self.camera.background_color = "#D6EAF8"  # Fondo azul claro
        texto1 = Text("First text",color= BLACK)
        texto2 = Text("Second text",color= BLACK)
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()
        self.play(FadeOut(texto2))
        self.play(FadeOut(texto1))

        # TransformationText1V2
        self.camera.background_color = "#FDEDEC"  # Fondo rojo claro
        texto1 = Text("First text",color= BLACK).to_edge(UP)
        texto2 = Text("Second text",color= BLACK)
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()
        self.play(FadeOut(texto2))
        self.play(FadeOut(texto1))

        # TransformationText2
        self.camera.background_color = "#E8F8F5"  # Fondo verde claro
        texts = [
            Text("Function",color= BLACK),
            Text("Derivative",color= BLACK),
            Text("Integral",color= BLACK),
            Text("Transformation",color= BLACK)
        ]
        self.play(Write(texts[0]))
        self.wait()
        for i in range(len(texts) - 1):
            self.play(ReplacementTransform(texts[i], texts[i + 1]))
            self.wait()
        self.play(FadeOut(texts[-1]))

        # CopyTextV1
        self.camera.background_color = "#FDF2E9"  # Fondo naranja claro
        formula = MathTex(
            "\\frac{d}{dx}", "(", "u", "+", "v", ")", "=",
            "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v",color= BLACK
        )
        formula.scale(2)
        self.play(Write(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9]),
            run_time=3
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10]),
            run_time=3
        )
        self.wait()
        self.play(FadeOut(formula))

        # CopyTwoFormulas3
        self.camera.background_color = "#FFCDD2"  # Fondo naranja claro
        formula1 = MathTex("\\neg", "\\forall", "x", ":", "P(x)",color= BLACK)
        formula2 = MathTex("\\exists", "x", ":", "\\neg", "P(x)",color= BLACK)
        parametters = [
            (2, 2 * UP, formula1, GREEN, "\\forall"),
            (2, 2 * DOWN, formula2, ORANGE, "\\exists")
        ]
        for size, pos, formula, col, sim in parametters:
            formula.scale(size).move_to(pos)
            formula.set_color_by_tex(sim, col)
            formula.set_color_by_tex("\\neg", PINK)

        self.play(Write(formula1))
        self.wait()
        changes = [
            [(2, 3, 4), (1, 2, 4)],
            [(0,), (3,)],
            [(1,), (0,)]
        ]
        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    formula1[i].copy(), formula2[j]
                ) for i, j in zip(pre_ind, post_ind)
            ], run_time=2)
            self.wait()
        self.play(FadeOut(formula1), FadeOut(formula2))

        # ChangeTextColorAnimation
        self.camera.background_color = "#E3F2FD"  # Fondo naranja claro
        text = Text("Text",color= BLACK).scale(3)
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.set_color(YELLOW),
            run_time=2
        )
        self.wait()
        self.play(FadeOut(text))

        # ChangeSizeAnimation
        self.camera.background_color = "#E8F5E9"  # Fondo naranja claro
        text = Text("Text",color= BLACK).scale(2)
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.scale(3),
            run_time=2
        )
        self.wait()
        self.play(FadeOut(text))

        # MoveText
        self.camera.background_color = "#FFFDE7"  # Fondo naranja claro
        text = Text("Text",color= BLACK).scale(2).shift(LEFT * 2)
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.shift(RIGHT * 2),
            run_time=2,
            path_arc=-np.pi
        )
        self.wait()
        self.play(FadeOut(text))

        self.camera.background_color = "#F3E5F5"  # Fondo naranja claro
        # ChangeColorAndSizeAnimation
        text = Text("Text").scale(2).shift(LEFT * 2)
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.shift(RIGHT * 2).scale(2).set_color(RED),
            run_time=2,
        )
        self.wait()
        self.play(FadeOut(text))
