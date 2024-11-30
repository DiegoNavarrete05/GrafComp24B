from manim import *
import numpy as np

class TransformationText1V1(Scene): #YA
    def construct(self):
        texto1 = Text("First text")
        texto2 = Text("Second text")
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()


class TransformationText1V2(Scene): #YA
    def construct(self):
        texto1 = Text("First text").to_edge(UP)
        texto2 = Text("Second text")
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()


class TransformationText2(Scene): #YA
    def construct(self):
        texts = [
            Text("Function"),
            Text("Derivative"),
            Text("Integral"),
            Text("Transformation")
        ]
        self.play(Write(texts[0]))
        self.wait()
        for i in range(len(texts) - 1):
            self.play(ReplacementTransform(texts[i], texts[i + 1]))
            self.wait()


class CopyTextV1(Scene): #YA
    def construct(self):
        formula = MathTex(
            "\\frac{d}{dx}", "(", "u", "+", "v", ")", "=",
            "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"
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

class CopyTextV2(Scene): #YA
    def construct(self):
        formula = MathTex(
            "\\frac{d}{dx}", "(", "u", "+", "v", ")", "=",
            "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"
        )
        formula.scale(2)
        formula[8].set_color(RED)
        formula[11].set_color(BLUE)
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

class CopyTextV3(Scene): #YA
	def construct(self):
		formula = MathTex("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		formula[8].set_color(RED)
		formula[11].set_color(BLUE)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()

class CopyTextV4(Scene): #YA
	def construct(self):
		formula = MathTex("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		for letter,color in [("u",RED),("v",BLUE)]:
			formula.set_color_by_tex(letter,color)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()

class CopyTwoFormulas1(Scene): #YA
	def construct(self):
		formula1 = MathTex(
				"\\neg",		#0
				"\\forall",		#1
				"x",			#2
				":",			#3
				"P(x)"			#4
			)
		formula2 = MathTex(
				"\\exists",		#0
				"x",			#1
				":",			#2
				"\\neg",		#3
				"P(x)"			#4
			)
		for size,pos,formula in [(2,2*UP,formula1),(2,2*DOWN,formula2)]:
			formula.scale(size)
			formula.move_to(pos)
		self.play(Write(formula1))
		self.wait()
		changes = [
			[(0,1,2,3,4),
			# | | | | |
			# v v v v v
			 (3,0,1,2,4)],
		]
		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()
               
class CopyTwoFormulas2(Scene): 
    def construct(self):
        formula1 = MathTex("\\neg", "\\forall", "x", ":", "P(x)")
        formula2 = MathTex("\\exists", "x", ":", "\\neg", "P(x)")
        
        formula1.scale(2).move_to(2 * UP)
        formula2.scale(2).move_to(2 * DOWN)
        
        self.play(Write(formula1))
        self.wait()

        changes = [
            [(2, 3, 4), (1, 2, 4)],  # Primera transformación
            [(0,), (3,)],            # Segunda transformación
            [(1,), (0,)]             # Tercera transformación
        ]

        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    formula1[i].copy(), formula2[j]
                ) for i, j in zip(pre_ind, post_ind)
            ], run_time=2)
            self.wait()

class CopyTwoFormulas2Color(Scene): 
    def construct(self):

        formula1 = MathTex("\\neg", "\\forall", "x", ":", "P(x)")
        formula2 = MathTex("\\exists", "x", ":", "\\neg", "P(x)")

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

class CopyTwoFormulas3(Scene): 
    def construct(self):
        formula1 = MathTex("\\neg", "\\forall", "x", ":", "P(x)")
        formula2 = MathTex("\\exists", "x", ":", "\\neg", "P(x)")

        parametters = [
            (2, 2 * UP, formula1, GREEN, "\\forall"),
            (2, 2 * DOWN, formula2, ORANGE, "\\exists")
        ]

        for size, pos, formula, col, sim in parametters:
            formula.scale(size).move_to(pos)
            formula.set_color_by_tex(sim, col)
            formula.set_color_by_tex("\\neg", PINK)

        # Muestra la primera fórmula
        self.play(Write(formula1))
        self.wait()

        # Transformaciones
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


class ChangeTextColorAnimation(Scene): 
    def construct(self):
        text = Text("Text").scale(3)
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.set_color(YELLOW),
            run_time=2
        )
        self.wait()

class ChangeSizeAnimation(Scene): 
    def construct(self):
        text = Text("Text").scale(2)
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.scale(3),
            run_time=2
        )
        self.wait()


class MoveText(Scene): #YA
    def construct(self):
        text = Text("Text").scale(2).shift(LEFT * 2)
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.shift(RIGHT * 2),
            run_time=2,
            path_arc=-np.pi
        )
        self.wait()


class ChangeColorAndSizeAnimation(Scene):#YA
    def construct(self):
        text = Text("Text").scale(2).shift(LEFT * 2)
        self.play(Write(text))
        self.wait()
        self.play(
            text.animate.shift(RIGHT * 2).scale(2).set_color(RED),
            run_time=2,
        )
        self.wait()