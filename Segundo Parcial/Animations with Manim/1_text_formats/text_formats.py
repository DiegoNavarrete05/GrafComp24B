from manim import *

class WriteText(Scene): 
    def construct(self): 
        text = Text("This is a regular text")
        self.play(Write(text))
        self.wait(3)

class AddText(Scene): 
    def construct(self): 
        text = Text("This is a regular text")
        self.add(text)
        self.wait(3)

class Formula(Scene): 
    def construct(self): 
        formula = Text("This is a formula")
        self.play(Write(formula))
        self.wait(3)

class TipesOfText(Scene): 
    def construct(self): 
        typesOfText = Tex("""
            This is a regular text,
            $this is a formula$,
            $$this is a formula$$
            """)
        self.play(Write(typesOfText))
        self.wait(3)

class TipesOfText2(Scene): 
    def construct(self): 
        typesOfText = Tex("""
            This is a regular text,
            $\\frac{x}{y}$,
            $$x^2+y^2=a^2$$
            """)
        self.play(Write(typesOfText))
        self.wait(3)

class DisplayFormula(Scene): 
    def construct(self): 
        typesOfText = Tex("""
            This is a regular text,
            $\\displaystyle\\frac{x}{y}$,
            $$x^2+y^2=a^2$$
            """)
        self.play(Write(typesOfText))
        self.wait(3)

class TextInCenter(Scene):
    def construct(self):
        text = Text("Text")
        self.play(Write(text))
        self.wait(3)

class TextOnTopEdge(Scene):
    def construct(self):
        text = Text("Text")
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(3)

class TextOnBottomEdge(Scene):
    def construct(self):
        text = Text("Text")
        text.to_edge(DOWN)
        self.play(Write(text))
        self.wait(3)

class TextOnRightEdge(Scene):
    def construct(self):
        text = Text("Text")
        text.to_edge(RIGHT)
        self.play(Write(text))
        self.wait(3)

class TextOnLeftEdge(Scene):
    def construct(self):
        text = Text("Text")
        text.to_edge(LEFT)
        self.play(Write(text))
        self.wait(3)

class TextInUpperRightCorner(Scene):
    def construct(self):
        text = Text("Text")
        text.to_edge(UP+RIGHT)
        self.play(Write(text))
        self.wait(3)

class TextInLowerLeftCorner(Scene): 
    def construct(self): 
        text = Text("Text") 
        text.to_edge(LEFT+DOWN)
        self.play(Write(text))
        self.wait(3)

class CustomPosition1(Scene):
    def construct(self):
        textM = Text("Text")
        textC = Text("Central text")
        textM.move_to(0.3*UP) 
        self.play(Write(textM),Write(textC))
        self.wait(3)

class CustomPosition2(Scene):
    def construct(self):
        textM = Text("Text")
        textC = Text("Central text")
        textM.move_to(1*UP+1*RIGHT)
        self.play(Write(textM),Write(textC))
        self.wait(1)
        textM.move_to(1*UP+1*RIGHT) 
        self.play(Write(textM))
        self.wait(3)

class RelativePosition1(Scene):
    def construct(self):
        textM = Text("Text")
        textC = Text("Reference text")
        textM.next_to(textC,LEFT,buff=1) 
        self.play(Write(textM),Write(textC))
        self.wait(3)

class RelativePosition2(Scene):
    def construct(self):
        textM = Text("Text")
        textC = Text("Reference text")
        textM.shift(UP*0.1)
        self.play(Write(textM),Write(textC))
        self.wait(3)

class RotateObject(Scene):
    def construct(self):
        textM = Text("Text")
        textC = Text("Reference text")
        textM.shift(UP)
        textM.rotate(PI/4) 
        self.play(Write(textM),Write(textC))
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI)
        self.wait(2)

class MirrorObject(Scene):
    def construct(self):
        textM = Text("Text")
        textM.flip(UP)
        self.play(Write(textM))
        self.wait(2)

class SizeTextOnLaTeX(Scene):
    def construct(self):
        textHuge = Tex("{\\Huge Huge Text 012.\\#!?} Text")
        texthuge = Tex("{\\huge huge Text 012.\\#!?} Text")
        textLARGE = Tex("{\\LARGE LARGE Text 012.\\#!?} Text")
        textLarge = Tex("{\\Large Large Text 012.\\#!?} Text")
        textlarge = Tex("{\\large large Text 012.\\#!?} Text")
        textNormal = Tex("{\\normalsize normal Text 012.\\#!?} Text")
        textsmall = Tex("{\\small small Text 012.\\#!?} Texto normal")
        textfootnotesize = Tex("{\\footnotesize footnotesize Text 012.\\#!?} Text")
        textscriptsize = Tex("{\\scriptsize scriptsize Text 012.\\#!?} Text")
        texttiny = Tex("{\\tiny tiny Texto 012.\\#!?} Text normal")
        textHuge.to_edge(UP)
        texthuge.next_to(textHuge,DOWN,buff=0.1)
        textLARGE.next_to(texthuge,DOWN,buff=0.1)
        textLarge.next_to(textLARGE,DOWN,buff=0.1)
        textlarge.next_to(textLarge,DOWN,buff=0.1)
        textNormal.next_to(textlarge,DOWN,buff=0.1)
        textsmall.next_to(textNormal,DOWN,buff=0.1)
        textfootnotesize.next_to(textsmall,DOWN,buff=0.1)
        textscriptsize.next_to(textfootnotesize,DOWN,buff=0.1)
        texttiny.next_to(textscriptsize,DOWN,buff=0.1)
        self.add(textHuge,texthuge,textLARGE,textLarge,textlarge,textNormal,textsmall,textfootnotesize,textscriptsize,texttiny)
        self.wait(3)

class TextFonts(Scene):
    def construct(self):
        textNormal = Tex("{Roman serif text 012.\\#!?} Text")
        textItalic = Tex("\\textit{Italic text 012.\\#!?} Text")
        textTypewriter = Tex("\\texttt{Typewritter text 012.\\#!?} Text")
        textBold = Tex("\\textbf{Bold text 012.\\#!?} Text")
        textSL = Tex("\\textsl{Slanted text 012.\\#!?} Text")
        textSC = Tex("\\textsc{Small caps text 012.\\#!?} Text")
        textNormal.to_edge(UP)
        textItalic.next_to(textNormal,DOWN,buff=.5)
        textTypewriter.next_to(textItalic,DOWN,buff=.5)
        textBold.next_to(textTypewriter,DOWN,buff=.5)
        textSL.next_to(textBold,DOWN,buff=.5)
        textSC.next_to(textSL,DOWN,buff=.5)
        self.add(textNormal,textItalic,textTypewriter,textBold,textSL,textSC)
        self.wait(3)