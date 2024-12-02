from manim import *
import random
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
        name_text = Text("Visual Tools", font_size=36, color=BLACK)
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
        
class MoveBraces(Scene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=",       #0
            "f(x)\\frac{d}{dx}g(x)",        #1
            "+",                            #2
            "g(x)\\frac{d}{dx}f(x)"         #3
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
        t1 = brace1.get_text("$g'f$")
        t2 = brace2.get_text("$f'g$")
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
        )
        self.wait()
        self.play(
            ReplacementTransform(brace1, brace2),
            ReplacementTransform(t1, t2)
        )
        self.wait()

    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class MoveBracesCopy(Scene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
        t1 = brace1.get_text("$g'f$")
        t2 = brace2.get_text("$f'g$")
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
        )
        self.wait()
        self.play(
            ReplacementTransform(brace1.copy(), brace2),
            ReplacementTransform(t1.copy(), t2)
        )
        self.wait()

    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class MoveFrameBox(Scene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=.1)
        framebox2 = SurroundingRectangle(text[3], buff=.1)
        self.play(Create(framebox1))
        self.wait()
        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait()

    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class MoveFrameBoxCopy(Scene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=.1)
        framebox2 = SurroundingRectangle(text[3], buff=.1)
        self.play(Create(framebox1))
        self.wait()
        self.play(
            ReplacementTransform(framebox1.copy(), framebox2),
            path_arc=-np.pi
        )
        self.wait()

    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class MoveFrameBoxCopy2(Scene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=.1)
        framebox2 = SurroundingRectangle(text[3], buff=.1)
        t1 = Text("g'f")
        t2 = Text("f'g")
        t1.next_to(framebox1, UP, buff=0.1)
        t2.next_to(framebox2, UP, buff=0.1)
        self.play(Create(framebox1), FadeIn(t1))
        self.wait()
        self.play(
            ReplacementTransform(framebox1.copy(), framebox2),
            ReplacementTransform(t1.copy(), t2)
        )
        self.wait()

    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class Arrow1(Scene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        arrow = Arrow(LEFT, RIGHT)
        step1.move_to(LEFT*2)
        arrow.next_to(step1, RIGHT, buff=.1)
        step2.next_to(arrow, RIGHT, buff=.1)
        self.play(Write(step1))
        self.wait()
        self.play(GrowArrow(arrow))
        self.play(Write(step2))
        self.wait()

    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class Arrow2(Scene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT*2 + DOWN*2)
        step2.move_to(4*RIGHT + 2*UP)
        arrow1 = Arrow(step1.get_right(), step2.get_left(), buff=0.1)
        arrow1.set_color(RED)
        arrow2 = Arrow(step1.get_top(), step2.get_bottom(), buff=0.1)
        arrow2.set_color(BLUE)
        self.play(Write(step1), Write(step2))
        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        self.wait()

    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class LineAnimation(Scene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT*2 + DOWN*2)
        step2.move_to(4*RIGHT + 2*UP)
        arrow1 = Line(step1.get_right(), step2.get_left(), buff=0.1)
        arrow1.set_color(RED)
        arrow2 = Line(step1.get_top(), step2.get_bottom(), buff=0.1)
        arrow2.set_color(BLUE)
        self.play(Write(step1), Write(step2))
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.wait()

    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class DashedLineAnimation(Scene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT*2 + DOWN*2)
        step2.move_to(4*RIGHT + 2*UP)
        arrow1 = DashedLine(step1.get_right(), step2.get_left(), buff=0.1)
        arrow1.set_color(RED)
        arrow2 = Line(step1.get_top(), step2.get_bottom(), buff=0.1)
        arrow2.set_color(BLUE)
        self.play(Write(step1), Write(step2))
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.wait()

    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class LineAnimation2(Scene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT*2 + DOWN*2)
        step2.move_to(4*RIGHT + 2*UP)
        line = Line(step1.get_right(), step2.get_left(), buff=0.1)
        self.play(Write(step1), Write(step2))
        self.play(Create(line))
        self.play(step2.animate.next_to(step2, LEFT*2))
        self.wait()

    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

class LineAnimation3(Scene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step3 = step2.copy()
        step1.move_to(LEFT*2+DOWN*2)
        step2.move_to(4*RIGHT+2*UP)
        step3.next_to(step2, LEFT*2)
        line = Line(step1.get_right(),step2.get_left(),buff=0.1)
        lineCopy = Line(step1.get_right(),step3.get_bottom(),buff=0.1)
        self.play(Write(step1),Write(step2))
        self.play(Create(line))
        self.play(ReplacementTransform(step2,step3),ReplacementTransform(line,lineCopy))
        self.wait()
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
