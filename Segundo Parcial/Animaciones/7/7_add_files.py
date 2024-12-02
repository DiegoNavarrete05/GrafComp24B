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
        name_text = Text("Add Files", font_size=36, color=BLACK)
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
class AudioTest(Scene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        group_dots=VGroup(*[Dot()for _ in range(3)])
        group_dots.arrange_submobjects(RIGHT)
        for dot in group_dots:
            self.add_sound("click",gain=-10)
            self.add(dot)
            self.wait()
        self.wait()
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
 
class SVGTest(Scene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        svg = SVGMobject("finger")
        #svg = SVGMobject("camera")
        self.play(DrawBorderThenFill(svg,rate_func=linear))
        self.wait()
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
 
class ImageTest(Scene):
    def construct(self):
        self.camera.background_color = self.get_random_color()
        image = ImageMobject("note")
        self.play(FadeIn(image))
        self.wait()
    def get_random_color(self):
        return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
