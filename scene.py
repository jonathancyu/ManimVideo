from manim import *
import math

align_args = {"aligned_edge": LEFT}
point_args = {"radius":0.01, "color":RED, "fill_opacity":1}
tex_args = {"font_size":40}
elbow_args = {"stroke_width": 2, "radius": 0.2, "color": WHITE, "elbow": True}
perp_args = {"stroke_width": 2, "color": WHITE}

line_args = {"stroke_width": 2, "color": WHITE}
class PartA(Scene):
    def new_play(self, *args):
        self.i += 1
        self.remove(self.pagenum)
        self.pagenum = Text(str(self.i)).to_corner(DL)
        self.add(self.pagenum)
        self.old_play(*args)
        
    def construct(self):
        self.i = 0
        self.pagenum = Text("0").to_corner(DL)
        self.old_play = self.play
        self.play = self.new_play
        # section a
        self.triangle_group = VGroup()
        # Triangle
        A = np.array([0, 0.5, 0])
        B = np.array([-1, -2.5, 0])
        C = np.array([5, -2.5, 0])

        triangle = Polygon(A, B, C) 


        self.triangle_group.add(triangle)
        self.play(Create(self.triangle_group))
        point_labels = VGroup(
            Tex("A").move_to(A + [0, 0.2, 0]),
            Tex("B").move_to(B + [-0.2, -0.2, 0]),
            Tex("C").move_to(C + [0.2, -0.2, 0]),
        )
        self.play(Create(point_labels))
        self.triangle_group.add(point_labels)
        
        #P_label = Tex("P").move_to(P + [-0.2, 0, 0])
        #P_group = VGroup(P_point, P_label)

        area_fill = self.triangle_group.copy().set_fill(BLUE, opacity=0.5)
        area_label = Tex("$S$", tex_environment="flushleft").move_to(triangle).shift(DOWN*0.5, LEFT)
        
        self.play(Create(area_fill))
        self.play(Create(area_label))
        S_description = Tex("$S$ = area of the triangle", tex_environment="flushleft", font_size = 40).to_corner(UL)
        self.play(TransformMatchingTex(area_label, S_description))
        self.play(FadeOut(area_fill))


        incircle_group, radius, radius_label = self.incircle(A, B, C)

        r_description = Tex("$r$ = radius of the incircle", tex_environment="flushleft", font_size = 40).next_to(S_description, RIGHT)      
        self.play(TransformMatchingTex(radius_label, r_description))
        self.play(FadeOut(incircle_group, radius))


        circumcircle, circumradius, circumradius_label = self.circumcircle(A, B, C)
                  
        R_description = Tex("$R$ = radius of the circumcircle", tex_environment="flushleft", font_size = 40).next_to(S_description, DOWN).shift(RIGHT)
        self.play(TransformMatchingTex(circumradius_label, R_description))
        self.play(FadeOut(circumcircle, circumradius))


        edge_labels = VGroup(
            Tex("a").move_to((B + C) / 2 + [0, -0.2, 0]),
            Tex("b").move_to((A + C) / 2 + [0.2, 0.2, 0]),
            Tex("c").move_to((A + B) / 2 + [-0.2, 0, 0]),
        )
        self.triangle_group.add(edge_labels)
        self.play(Create(edge_labels))

        #self.triangle_group.shift(RIGHT*2, DOWN)
        #self.play(FadeOut(self.triangle_group), FadeOut(point_labels))
        self.play(self.triangle_group.animate.scale(0.5).shift(RIGHT*2, DOWN*2))



        t1 = MathTex("2p^2 - 2r^2 - 8Rr = ", r"2p^2 - \frac{2p(p-a)(p-b)(p-c)}{p^2} - \frac{2abc}{p}").to_edge(UP).shift(DOWN*2)
        self.play(Create(t1))
        self.wait(5)

        t2 = MathTex(r"= \frac{2p^3 - 2(p-c)(p^2-pb-pa-ab)-2abc}{p}").next_to(t1, DOWN)
        self.play(TransformMatchingShapes(t1[1].copy(), t2))
        self.wait(5)
        self.play(FadeOut(t1[1]))

        t3 = MathTex(r"= \frac{2p^3 - 2(p^3 - p^2b-p^2a + abp - cp^2 + pbc + acp - abc) - 2abc}{p}").next_to(t2, DOWN)
        self.play(Create(t3))
        self.wait(5)
        self.play(FadeOut(t2), t3.animate.next_to(t1, DOWN))
        self.wait(5)


        t4 = MathTex(r"= 2(pb + pa + pc - ab - ac - bc)").next_to(t3, DOWN)
        self.play(Create(t4))
        self.wait(5)
        self.play(FadeOut(t3), t4.animate.next_to(t1, DOWN))
        self.wait(5)

        t5 = MathTex(r"= (a + b + c)(a) + (a + b + c)(b) + (a + b + c)(c)").next_to(t4, DOWN)
        self.play(Create(t5))
        self.wait(5)
        self.play(FadeOut(t4), t5.animate.next_to(t1, DOWN))
        self.wait(5)

        t6 = MathTex(r"= ab +", "b^2", "+ bc +", "a^2",  "+ ab + ac + ac + bc +", "c^2", "- 2ab - 2ac - 2bc").next_to(t5, DOWN)
        self.play(Create(t6))
        self.wait(5)
        self.play(FadeOut(t5), t6.animate.next_to(t1, DOWN))
        self.wait(5)

        t7 = MathTex("=", "a^2", "+", "b^2", "+", "c^2").next_to(t6, DOWN)
        self.play(Create(t7))
        self.wait(5)
        self.play(FadeOut(t6), t7.animate.next_to(t1, DOWN))
        self.wait(5)

        t8 = MathTex("2p^2 - 2r^2 - 8Rr ","=", "a^2+b^2+c^2").next_to(t7, DOWN)
        self.play(Create(t8), FadeOut(t1, t7))

        rect = SurroundingRectangle(t8, buff=0.1, color=YELLOW)
        self.play(Create(rect))
        equation = VGroup(t8, rect)
        self.play(equation.animate.scale(0.6).to_corner(UR))

    
    def bisectors(self, A, B, C, P):
        bisectors = VGroup(
            Line(A, P, stroke_width=2), 
            Line(B, P, stroke_width=2), 
            Line(C, P, stroke_width=2)
        )
        bisector_angles = VGroup(
            angle_bisector_equality(C, A, B, P, 1),
            angle_bisector_equality(A, B, C, P, 2),
            angle_bisector_equality(B, C, A, P, 3)
        )
        return bisectors, bisector_angles

    def incircle(self, A, B, C):

        x, y, r = calculate_incircle(A, B, C)
        P = np.array([x, y, 0])

        bisectors, bisector_angles = self.bisectors(A, B, C, P)

        self.play(Create(bisectors))
        self.play(Create(bisector_angles))
        P_point = Circle(**point_args).move_to(P)
        self.play(Create(P_point))
        self.play(FadeOut(bisectors, bisector_angles))

        incircle_group = VGroup()
        incircle = Circle(radius=r).move_to(P)
        incircle_group.add(incircle)
        radius = Line([x, y, 0], [x+r, y, 0])
        radius_label = Tex("$r$", tex_environment="flushleft").move_to([x+r/2, y+.1, 0])
        incircle_group.add(P_point)
        
        self.play(Create(radius))
        self.play(Create(incircle))
        self.play(Create(radius_label))
        return incircle_group, radius, radius_label
         
    def circumcircle(self, A, B, C):
        x, y, r = calculate_circumcircle(A, B, C)
        P = np.array([x, y, 0])

        m_AB = (A + B)/2
        m_BC = (B + C)/2
        m_AC = (A + C)/2

        perp_bisector_group = VGroup(
            Line(m_AB, P, stroke_width=2),
            Line(m_BC, P, stroke_width=2),
            Line(m_AC, P, stroke_width=2),
            Angle.from_three_points(A, m_AB, P, radius=0.2, elbow=True, stroke_width=2),
            Angle.from_three_points(B, m_BC, P, radius=0.2, elbow=True, stroke_width=2),
            Angle.from_three_points(C, m_AC, P, radius=0.2, elbow=True, stroke_width=2)
        )
        self.triangle_group.add(perp_bisector_group)
        self.play(Create(perp_bisector_group))

        P_point = Circle(**point_args).move_to(P)
        
        self.play(Create(P_point))

        circumcircle = Circle(radius=r).move_to(P)
        r_start = np.array([x, y, 0])
        radius = Line(r_start, C)
        radius_label = Tex("$R$", tex_environment="flushleft").move_to((r_start + C)/2 + [-0.2, -0.1, 0])
        self.play(Create(radius))
        self.play(Create(circumcircle))
        self.play(Create(radius_label))
        return VGroup(circumcircle, P_point), radius, radius_label

class PartB(Scene):    
    def new_play(self, *args):
        self.i += 1
        self.remove(self.pagenum)
        self.pagenum = Text(str(self.i)).to_corner(DL)
        self.add(self.pagenum)
        self.old_play(*args)
        
    def construct(self):
        self.i = 0
        self.pagenum = Text("0").to_corner(DL)
        self.old_play = self.play
        self.play = self.new_play
        # section a
        
        equation1 = MathTex("2p^2 - 2r^2 - 8Rr ","=", "a^2+b^2+c^2").scale(0.6).to_corner(UR)
        rect1 = SurroundingRectangle(equation1, buff=0.1, color=YELLOW)
        equation1_group = VGroup(equation1, rect1)
        self.add(equation1_group)



        self.group = VGroup()

        # Triangle
        A = np.array([0, 0.5, 0])
        B = np.array([-1, -2.5, 0])
        C = np.array([5, -2.5, 0])
        point_labels = VGroup(
            Tex("A").move_to(A + [0, 0.2, 0]),
            Tex("B").move_to(B + [-0.2, -0.2, 0]),
            Tex("C").move_to(C + [0.2, -0.2, 0]),
        )

        triangle = Polygon(A, B, C)
        self.play(Create(triangle))
        self.play(Write(point_labels))

        G, G_Label = self.make_centroid(A, B, C)
        center = G.get_center()
        startpos = center + [-1, 0.5, 0]
        M = Dot(color=GREEN).move_to(startpos)
        lineargs = {"stroke_width":2}
        line = Line(G.get_center(), M.get_center(), **lineargs)
        AM = Line(A, M.get_center(), **lineargs)
        BM = Line(B, M.get_center(), **lineargs)
        CM = Line(C, M.get_center(), **lineargs)

        x = ValueTracker(startpos[0])
        y = ValueTracker(startpos[1])
        M.add_updater(lambda z: z.move_to([x.get_value(), y.get_value(), 0]))



        M_label = MathTex("M").move_to(M.get_center() + [-0.3, 0, 0])
        M_label.add_updater(lambda z: z.move_to(M.get_center() + [-0.3, 0, 0]))

        line.add_updater(lambda z: z.become(Line(G.get_center(), M.get_center(), **lineargs)))
        AM.add_updater(lambda z: z.become(Line(A, M.get_center(), **lineargs)))
        BM.add_updater(lambda z: z.become(Line(B, M.get_center(), **lineargs)))
        CM.add_updater(lambda z: z.become(Line(C, M.get_center(), **lineargs)))

        lines = VGroup(line, AM, BM, CM)

        self.play(Create(M))
        self.play(Write(M_label))
        self.play(Create(lines))
        for pos in [(-0.5, -0.3), (2, -0.2), (-1, 0.5)]:
            new_pos = (center[0] + pos[0], center[1] + pos[1], 0)
            print(new_pos)
            self.play(x.animate.set_value(center[0] + pos[0]), 
                      y.animate.set_value(center[1] + pos[1]))
            self.wait(5)
        
        v_MG = G.get_center() - M.get_center()
        v_MA = A - M.get_center()
        v_MB = B - M.get_center()
        v_MC = C - M.get_center()


        a_MG = Arrow(start=M.get_center(), end=G.get_center(), buff=0, color=BLUE)
        a_MA = Arrow(start=M.get_center(), end=A, buff=0, color=RED)
        a_MB = Arrow(start=M.get_center(), end=B, buff=0, color=RED)
        a_MC = Arrow(start=M.get_center(), end=C, buff=0, color=RED)
        vector_group = VGroup(a_MG, a_MA, a_MB, a_MC)
        self.play(Create(vector_group))
        self.play(FadeOut(lines), FadeOut(triangle), FadeOut(point_labels), FadeOut(M_label), FadeOut(M), FadeOut(G), FadeOut(G_Label))
        
        a_MG1 = Arrow(start=ORIGIN, end=ORIGIN + v_MG, buff=0, color=BLUE)
        a_MG2 = Arrow(start=ORIGIN+v_MG, end=ORIGIN + v_MG*2, buff=0, color=BLUE)
        a_MG3 = Arrow(start=ORIGIN+v_MG*2, end=ORIGIN + v_MG*3, buff=0, color=BLUE)

        pos = ORIGIN + v_MA
        a_MA1 = Arrow(start=ORIGIN, end=pos, buff=0, color=RED)
        a_MB1 = Arrow(start=pos, end=pos + v_MB, buff=0, color=RED)
        pos += v_MB
        a_MC1 = Arrow(start=pos, end=pos + v_MC, buff=0, color=RED)
        self.play(Transform(a_MG, a_MG1), Transform(a_MA, a_MA1), Transform(a_MB, a_MB1), Transform(a_MC, a_MC1))
        self.play(Create(a_MG2))
        self.play(Create(a_MG3))
        self.wait(5)
        t1 = MathTex(r"3\overrightarrow{MG}", "=", r"\overrightarrow{MA}",  "+",  r"\overrightarrow{MB}",  "+", r"\overrightarrow{MC}", **tex_args).to_edge(UP)
        self.play(Write(t1))
        self.play(FadeOut(a_MG), FadeOut(a_MA), FadeOut(a_MB), FadeOut(a_MC), FadeOut(a_MG1), FadeOut(a_MG2), FadeOut(a_MG3), FadeOut(a_MA1), FadeOut(a_MB1), FadeOut(a_MC1))
        self.play(t1.animate.shift(DOWN*2))
        self.wait(5)
        t2 = MathTex("9MG^2", "=", "MA^2", "+", "MB^2", "+", "MC^2" + "+", r"2\overrightarrow{MA}.\overrightarrow{MB}", "+", r"2\overrightarrow{MB}.\overrightarrow{MC}", "+", r"2\overrightarrow{MB}.\overrightarrow{MC}",
                     **tex_args).next_to(t1, DOWN)
        t2_desc = MathTex(r"(\overrightarrow{MA}.\overrightarrow{MB} = MA^2 + MB^2 - AB^2})", **tex_args).next_to(t2, UP)
        self.play(TransformMatchingShapes(t1.copy(), t2))
        self.wait(5)
        self.play(FadeOut(t1))
        self.wait(5)

        self.play(Write(t2_desc))
        self.wait(5)

        t3 = MathTex("9MG^2", "&=", "MA^2", "+", "MB^2", "+", r"MC^2\\" +
                      r"&+ (MA^2 + MB^2 - AB^2)\\",
                      r"&+ (MB^2 + MC^2 - BC^2)\\",
                      r"&+ (MC^2 + MA^2 - AC^2)\\", **tex_args).next_to(t2, DOWN)
        self.play(Create(t3))
        self.wait(5)
        self.play(FadeOut(t2, t2_desc), t3.animate.to_edge(UP).shift(DOWN*2))
        self.wait(5)
        t4 = MathTex("9MG^2", "&=", r"3(MA^2 + MB^2 + MC^2) - (AB^2 + AC^2 + BC2)", **tex_args).next_to(t3, DOWN)
        self.play(Create(t4))
        self.wait(5)    
        self.play(FadeOut(t3), t4.animate.to_edge(UP).shift(DOWN*2))
        self.wait(5)

        equation2 = MathTex("3MG", "&=", r"MA^2 + MB^2 + MC^2 - \tfrac{1}{3}(AB^2 + AC^2 + BC^2)", **tex_args).next_to(t1, DOWN)
        self.play(Create(equation2))
        self.wait(5)
        rect2 = SurroundingRectangle(equation2, buff=0.1)
        self.play(Create(rect2))
        self.wait(5)
        equation2_group = VGroup(equation2, rect2)
        self.play(equation2_group.animate.scale(0.4))
        self.play(equation2_group.animate.next_to(equation1, DOWN, aligned_edge=RIGHT))


        
    
    def make_centroid(self, A, B, C):
        m_AB = (A + B)/2
        m_BC = (B + C)/2
        m_AC = (A + C)/2

        perp_bisector_group = VGroup(
            Line(m_AB, C, stroke_width=2),
            Line(m_BC, A, stroke_width=2),
            Line(m_AC, B, stroke_width=2)
        )
        self.play(Create(perp_bisector_group))

        centroid = (A + B + C)/3
        centroid_point = Dot(color=RED).move_to(centroid)
        centroid_label = MathTex("G").move_to(centroid + [0, -0.3, 0])
        self.play(Create(centroid_point))
        self.play(FadeOut(perp_bisector_group))
        self.play(Write(centroid_label))
        return centroid_point, centroid_label

class PartC(Scene):
    def new_play(self, *args):
        self.i += 1
        self.remove(self.pagenum)
        self.pagenum = Text(str(self.i)).to_corner(DL)
        self.add(self.pagenum)
        self.old_play(*args)

    def construct(self):
        self.i = 0
        self.pagenum = Text("0").to_corner(DL)
        self.old_play = self.play
        self.play = self.new_play
        tex_args = {"font_size": 40}

        # Old equations
        equation1 = MathTex("2p^2 - 2r^2 - 8Rr ","=", "a^2+b^2+c^2").scale(0.4)
        equation1.to_corner(UR)
        rect1 = SurroundingRectangle(equation1, buff=0.1, color=YELLOW)
        equation1_group = VGroup(equation1, rect1)

        equation2 = MathTex("3MG", "&=", r"MA^2 + MB^2 + MC^2 - \tfrac{1}{3}(AB^2 + AC^2 + BC^2)", **tex_args).scale(0.4)
        equation2.next_to(equation1, DOWN, aligned_edge=RIGHT)
        rect2 = SurroundingRectangle(equation2, buff=0.1)
        equation2_group = VGroup(equation2, rect2)

        self.add(equation1_group, equation2_group)
       
        # Triangle
        A = np.array([0, 0.5, 0])
        B = np.array([-1, -2.5, 0])
        C = np.array([5, -2.5, 0])

        triangle = Polygon(A, B, C) 
        point_labels = VGroup(
            Tex("A").move_to(A + [0, 0.2, 0]),
            Tex("B").move_to(B + [-0.2, -0.2, 0]),
            Tex("C").move_to(C + [0.2, -0.2, 0]),
        )
        edge_labels = VGroup(
            Tex("a").move_to((B + C) / 2 + [0, -0.2, 0]),
            Tex("b").move_to((A + C) / 2 + [0.2, 0.2, 0]),
            Tex("c").move_to((A + B) / 2 + [-0.2, 0, 0]),
        )
        triangle_group = VGroup(triangle, point_labels, edge_labels)
        self.play(Create(triangle_group))

        I, incircle = self.incircle(A, B, C)
        # I = M

        

        align_args = {"aligned_edge": LEFT, "buff": 0.1}
        t0 = MathTex(r"3MG^2 = MA^2 + MB^2 + MC^2 - \tfrac{1}{3}(AB^2 + AC^2 + BC^2)", **tex_args).to_corner(UL)
        self.play(Write(t0))
        self.wait(5)
        t1 = Tex(r"Let $M \equiv I$").next_to(t0, DOWN)
        self.play(Write(t1))
        self.wait(5)
        t2 = MathTex(r"3IG^2 = IA^2 + IB^2 + IC^2 - \tfrac{1}{3}(AB^2 + AC^2 + BC^2)", **tex_args).to_corner(UL)
        self.play(TransformMatchingShapes(t0,t2))
        self.play(FadeOut(t1))

        # Draw IK _|_ AB
        elbow_args = {"stroke_width": 2, "radius": 0.2, "color": WHITE, "elbow": True}
        perp_args = {"stroke_width": 2, "color": WHITE}

        E = foot_of_perpendicular(B, I, C)
        IE = Line(E, I, **perp_args)
        IE_angle = Angle.from_three_points(C, E, I, **elbow_args)
        E_label = MathTex("E").move_to(E + [0, -0.3, 0])

        F = foot_of_perpendicular(A, I, C)
        IF = Line(F, I, **perp_args)
        IF_angle = Angle.from_three_points(A, F, I, **elbow_args)
        F_label = MathTex("F").move_to(F + [0.3, 0.3, 0])

        G = foot_of_perpendicular(B, I, A)
        IG = Line(G, I, **perp_args)
        IG_angle = Angle.from_three_points(A, G, I, **elbow_args)
        G_label = MathTex("G").move_to(G + [-0.3, 0.3, 0])

        self.play(Create(IF), Create(IF_angle), Create(IG), Create(IG_angle), Create(IE), Create(IE_angle))
        self.play(Write(E_label), Write(F_label), Write(G_label))
        
        radius_label = Tex("$r$").move_to(IF.get_center() + [0.3, -0.3, 0])

        AFI_fill = Polygon(A, I, F, color=YELLOW)
        self.play(Create(AFI_fill))
        t41 = MathTex(r"IA^2 = IF^2 + AF^2", **tex_args).next_to(t2, DOWN, **align_args)
        t42 = MathTex(r"p = \frac{a + b + c}{2}", **tex_args).next_to(t41, DOWN, **align_args)
        self.play(Write(t41))
        self.wait(5)
        self.play(Write(t42))
       
        self.wait(5)

        t45 = MathTex(r"p = \frac{(AF + FC) + (AG + GB) + (BE + EC)}{2}", **tex_args).next_to(t41, DOWN, **align_args)
        self.play(TransformMatchingShapes(t42, t45))
        AGI_fill = Polygon(A, I, G, color=YELLOW)
        self.wait(5)

        self.play(Create(AGI_fill))
        # TODO: add animation to show that arms of triangle are equal
        AG = Line(A, G, color=YELLOW, stroke_width=3)
        AF = Line(A, F, color=YELLOW, stroke_width=3)
        BG = Line(B, G, color=BLUE, stroke_width=3)
        BE = Line(B, E, color=BLUE, stroke_width=3)
        CE = Line(C, E, color=GREEN, stroke_width=3)
        CF = Line(C, F, color=GREEN, stroke_width=3)

        self.play(FadeOut(AFI_fill), FadeOut(AGI_fill))
        self.play(FadeOut(triangle), Create(AG), Create(AF), Create(BG), Create(BE), Create(CE), Create(CF))

        self.wait(5)

        t46 = MathTex(r"p = AF + BE + EC", **tex_args).next_to(t41, DOWN, **align_args)
        self.play(TransformMatchingShapes(t45, t46))

        t47 = MathTex(r"p = AF + BC", **tex_args).next_to(t41, DOWN, **align_args)
        self.play(TransformMatchingShapes(t46, t47))
        t48 = MathTex(r"p = AF + a", **tex_args).next_to(t41, DOWN, **align_args)
        self.play(TransformMatchingShapes(t47, t48))
        t49 = MathTex(r"AF = p - a", **tex_args).next_to(t41, DOWN, **align_args)
        self.play(TransformMatchingShapes(t48, t49, path_arc=PI/2))
        self.wait(5)

        t5 = MathTex(r"IA^2 = IF^2 + (p-a)^2\\", **tex_args).next_to(t2, DOWN, **align_args)
        self.play(TransformMatchingShapes(t41, t5))
        self.wait(5)

        t51 = MathTex(r"IA^2 = r^2 + (p-a)^2\\", **tex_args).next_to(t2, DOWN, **align_args)
        self.play(TransformMatchingShapes(t5, t51))
        self.wait(5)
        self.play(FadeOut(t49))
        t6 = MathTex(r"IB^2 =  r^2 + (p-b)^2\\", **tex_args).next_to(t51, DOWN, **align_args)
        t7 = MathTex(r"IC^2 = r^2 + (p-c)^2\\", **tex_args).next_to(t6, DOWN, **align_args)
        self.play(Write(t6), Write(t7))

        t8 = MathTex(r"3IG^2 = (p-a)^2 + (p-b)^2 + (p-c)^2 + 3r^2 - \frac{1}{3}(a^2+b^2+c^2)", **tex_args).to_corner(UL)
        self.play(TransformMatchingShapes(t2, t8))
        self.wait(5)
        self.play(FadeOut(t51), FadeOut(t6), FadeOut(t7))

        t9 = MathTex(r"3IG^2 = 3r^2 - p^2 + \frac{2}{3}(a^2+b^2+c^2)", **tex_args).to_corner(UL)
        self.play(TransformMatchingShapes(t8, t9))
        self.wait(5)
        #TODO: pring in part a
        t10 = MathTex(r"3IG^2 = 3r^2 - p^2 + \frac{2}{3}(2p^2 -2r^2 - 8Rr)", **tex_args).to_corner(UL)
        self.play(TransformMatchingShapes(t9, t10))
        self.wait(5)
        t11 = MathTex(r"9IG^2 = 9r^2 - 3p^2 + 4p^2 - 4r^2 - 16Rr", **tex_args).to_corner(UL)
        self.play(TransformMatchingShapes(t10, t11))
        self.wait(5)
        t12 = MathTex(r"9IG^2 =5r^2 - p^2 - 16Rr", **tex_args).to_corner(UL)
        self.play(TransformMatchingShapes(t11, t12))
        self.wait(5)
        equation3 = MathTex(r"IG^2 = \frac{5r^2 - p^2 - 16Rr}{9}", **tex_args).to_corner(UL)
        self.play(TransformMatchingShapes(t12, equation3))    
        self.wait(5)

        
        rect3 = SurroundingRectangle(equation3, buff=0.1, color=YELLOW)
        self.play(Create(rect3))

        self.wait(5)
        self.play(VGroup(equation3, rect3).animate.to_corner(DL))




    def incircle(self, A, B, C):

        x, y, r = calculate_incircle(A, B, C)
        P = np.array([x, y, 0])

        bisectors, bisector_angles = self.bisectors(A, B, C, P)

        self.play(Create(bisectors))
        self.play(Create(bisector_angles))
        P_point = Circle(**point_args).move_to(P)
        P_label = MathTex("I").move_to(P + [0.3, -0.3, 0])
        self.play(Create(P_point))
        self.play(Write(P_label))
        self.play(FadeOut(bisectors, bisector_angles))
        incircle = Circle(radius=r).move_to(P)
        self.play(Create(incircle))
        return P, VGroup(P_point, P_label, incircle)

    def bisectors(self, A, B, C, P):
        bisectors = VGroup(
            Line(A, P, stroke_width=2), 
            Line(B, P, stroke_width=2), 
            Line(C, P, stroke_width=2)
        )
        bisector_angles = VGroup(
            angle_bisector_equality(C, A, B, P, 1),
            angle_bisector_equality(A, B, C, P, 2),
            angle_bisector_equality(B, C, A, P, 3)
        )
        return bisectors, bisector_angles
    
class PartD(Scene): 
    def new_play(self, *args):
        self.i += 1
        self.remove(self.pagenum)
        self.pagenum = Text(str(self.i)).to_corner(DL)
        self.add(self.pagenum)
        self.old_play(*args)
        
    def construct(self):
        self.i = 0
        #self.pagenum = Text("0").to_corner(DL)
        #self.old_play = self.play
        #self.play = self.new_play


        
        # Old equations
        equation1 = MathTex("2p^2 - 2r^2 - 8Rr ","=", "a^2+b^2+c^2").scale(0.4)
        equation1.to_corner(UR)
        rect1 = SurroundingRectangle(equation1, buff=0.1, color=YELLOW)

        equation2 = MathTex("3MG", "&=", r"MA^2 + MB^2 + MC^2 - \tfrac{1}{3}(AB^2 + AC^2 + BC^2)", **tex_args).scale(0.4)
        equation2.next_to(equation1, DOWN, aligned_edge=RIGHT)
        rect2 = SurroundingRectangle(equation2, buff=0.1)
        
        equation3 = MathTex(r"IG^2 = \frac{5r^2 - p^2 - 16Rr}{9}", **tex_args).to_corner(DL)
        rect3 = SurroundingRectangle(equation3, buff=0.1, color=YELLOW)

        self.add(equation1, rect1, equation2, rect2, equation3, rect3)


        A = np.array([2, 2, 0])
        B = np.array([0, -1.5, 0])
        C = np.array([6, -1.5, 0])
        triangle = Polygon(A, B, C)
        self.play(Create(triangle))
        incenter = self.incenter(A, B, C)
        circumcenter, O, R = self.circumcenter(A, B, C)
        centroid = self.centroid(A, B, C)
        orthocenter, H = self.orthocenter(A, B, C)
        nine_point_center = self.nine_point_center(O, H, R)


        align_args = {"aligned_edge": LEFT, "buff": 0.1}

        t0 = MathTex(r"\text{\underline{Euler's Theorem}}: \\",
                     r"\overrightarrow{OG} = 2\overrightarrow{GE}\\").scale(0.8).to_corner(UR)
        self.play(Write(t0))
        self.wait(5)
        t1 = MathTex(r"\text{Recall: } \overrightarrow{OH} = 3\overrightarrow{OG}", r" = 6 \overrightarrow{GE}\\").scale(0.5).to_corner(UL)
        self.play(Write(t1[0]))
        self.play(TransformMatchingShapes(t0[1], t1[1]), FadeOut(t0[0]))
        self.wait(5)

        t2 = MathTex(r"OI^2 = OG^2 + GI^2 - 2(OG)(GI)(\cos(\angle OGI))", r" & \text{    }(1)\\",
                     r"EI^2 = EG^2 + GI^2 - 2(EG)(GI)(\cos(\angle EGI))", r" & \text{    }(2)\\").scale(0.5).next_to(t1, DOWN, **align_args)
        self.play(Write(t2))
        self.wait(5)

        t21 = MathTex(r"\cos (\angle OGI) = -\cos (\angle IGE)").scale(0.5).next_to(t2, DOWN, **align_args)
        self.play(Write(t21))
        self.wait(5)
        t22 = MathTex(r"OI^2 = OG^2 + GI^2 + 2GE.GI.\cos (\angle IGE)").scale(0.5).next_to(t21, DOWN, **align_args)
        self.play(Write(t22))
        self.wait(5)
        t23 = MathTex(r"2EI^2 = 2EG^2 + 2GI^2 - 2EG.GI.\cos(\angle EGI)").scale(0.5).next_to(t2, DOWN, **align_args)
        self.play(TransformMatchingShapes(t22, t23), FadeOut(t21))



        t3 = MathTex(r"2\times(2) + (1)").scale(0.5).next_to(t23, DOWN*4, **align_args)
        self.play(Write(t3))
        self.wait(5)

        t4 = MathTex("2EI^2 + OI^2", "=", "OG^2 + 2EG^2 + 3GI^2").scale(0.5).next_to(t23, DOWN, **align_args)
        self.play(TransformMatchingShapes(t2.copy(), t4))
        self.play(FadeOut(t3, t2, t1, t23))
        
        self.play(t4.animate.scale(1.5).to_corner(UL))
        self.wait(5)

        t5 = MathTex(r"EI^2 = \frac{1}{2}(OG^2 + 2EG^2 + 3GI^2 - OI^2)").scale(0.75).to_corner(UL)
        self.play(TransformMatchingShapes(t4, t5))
        self.wait(5)

        t6 = MathTex(r"EI^2 = \frac{1}{2} (\frac{3}{2}OG^2 + 3GI^2 - ","OI^2)").scale(0.75).to_corner(UL)
        self.play(TransformMatchingShapes(t5, t6))
        self.wait(5)

        t8 = MathTex(r"GI^2 = \frac{Sr^2 + p^2 - 16Rr}{9}").scale(0.75).next_to(t6, DOWN, **align_args)
        self.play(Write(t8))
        self.wait(5)

        t9 = MathTex(r"3MG^2 = MA^2 + MB^2 + MC^2 - \frac{1}{3}(AB^2 + AC^2 + BC^2)").scale(0.75).next_to(t8, DOWN, **align_args)
        self.play(Write(t9))
        t91 = MathTex(r"3OG^2 = OA^2 + OB^2 + OC^2 - \frac{1}{3}(a^2 + b^2 + c^2)").scale(0.75).next_to(t8, DOWN, **align_args)
        self.play(TransformMatchingShapes(t9, t91))
        self.wait(5)
        t92 = MathTex(r"3OG^2 = 3R^2 - \frac{1}{3}(2p^2-2r^2+8Rr)").scale(0.75).next_to(t8, DOWN, **align_args)
        self.play(TransformMatchingShapes(t91, t92))
        self.wait(5)
        t93 = MathTex(r"OG^2 = R^2 - \frac{1}{9}(2P^2 - 2r^2 + 8Rr)").scale(0.75).next_to(t8, DOWN, **align_args)
        self.play(TransformMatchingShapes(t92, t93))
        self.wait(5)
        t94 = MathTex(r"OG^2 = \frac{1}{9}(9R^2 - 2p^2 - 2r^2 + 8Rr)").scale(0.75).next_to(t8, DOWN, **align_args)
        self.play(TransformMatchingShapes(t93, t94))
        self.wait(5)

        t10 = MathTex(r"\frac{3}{2}OG^2 = \frac{3}{2}R^2 + \frac{1}{3}r^2 - \frac{1}{3}p^2 + \frac{4}{3}Rr").scale(0.75).next_to(t8, DOWN, **align_args)
        self.play(TransformMatchingShapes(t94, t10))
        self.wait(5)

        t11 = MathTex(r"3GI = \frac{5}{3}r^2 + \frac{3}{9}p^2 - \frac{16}{3}Rr").scale(0.75).next_to(t6, DOWN, **align_args)
        self.play(TransformMatchingShapes(t8, t11))
        self.wait(5)

        t12 = MathTex(r"\frac{3}{2}OG^2 + 3GI^2 &=  (\frac{3}{2}R^2 + \frac{1}{3}r^2 - \frac{1}{3}p^2 + \frac{4}{3}Rr)\\",
                                              r"&+ (\frac{5}{3}r^2 + \frac{3}{9}p^2 - \frac{16}{3}Rr)").scale(0.75).next_to(t6, DOWN, **align_args)
        self.play(TransformMatchingShapes(VGroup(t10, t11), t12))
        self.wait(5)

        t13 = MathTex(r"-OI^2 = -R^2 + 2Rr").scale(0.75).next_to(t6, DOWN, **align_args)
        self.play(TransformMatchingShapes(t12, t13))
        self.wait(5)

        t14 = MathTex(r"OI^2 = R^2 - 2Rr").scale(0.75).next_to(t6, DOWN, **align_args)
        self.play(TransformMatchingShapes(t13, t14))
        self.wait(5)

        t15 = MathTex(r"EI^2 = \frac{1}{2} (\frac{3}{2}OG^2 + 3GI^2 - ","(R^2 - 2Rr))").scale(0.75).to_corner(UL)
        self.play(TransformMatchingShapes(VGroup(t14, t6[1]), t15[1]))
        self.wait(5)

        t16 = MathTex(r"EI^2 = \frac{1}{2} (\frac{1}{2}R^2 + 2r^2 - 2Rr)").scale(0.75).to_corner(UL)
        self.play(TransformMatchingShapes(t15, t16), FadeOut(t6[0]))
        self.wait(5)

        t17 = MathTex(r"EI^2 = \frac{1}{4}(R-2r)^2").scale(0.75).to_corner(UL)
        self.play(TransformMatchingShapes(t16, t17))
        self.wait(5)

        t18 = MathTex(r"EI = \left|\frac{R}{2}-r\right|").scale(0.75).to_corner(UL)
        self.play(TransformMatchingShapes(t17, t18))
        self.wait(5)




        






    def incenter(self, A, B, C):

        x, y, r = calculate_incircle(A, B, C)
        P = np.array([x, y, 0])

        bisectors, bisector_angles = self.bisectors(A, B, C, P)

        self.play(Create(bisectors))
        self.play(Create(bisector_angles))
        incenter = Circle(**point_args).move_to(P)
        self.play(Create(incenter))
        self.play(FadeOut(bisectors, bisector_angles))
        incenter_label = MathTex("I").scale(0.5).move_to(P + [0, -0.2, 0])
        incircle = Circle(radius=r, color=WHITE, stroke_width=2).move_to(P)
        self.play(Create(incircle))
        radius = Line(P, P+ ([-1,-1,0]/np.sqrt(2)*r), color=WHITE, stroke_width=2)
        radius_label = MathTex("r").scale(0.5).move_to(radius.get_center() + [-0.1, 0.1, 0])
        self.play(Write(incenter_label))
        self.play(Create(radius), Write(radius_label))
        return VGroup(incenter, incenter_label)
   
    def circumcenter(self, A, B, C):
        x, y, r = calculate_circumcircle(A, B, C)
        P = np.array([x, y, 0])

        m_AB = (A + B)/2
        m_BC = (B + C)/2
        m_AC = (A + C)/2

        perp_bisector_group = VGroup(
            Line(m_AB, P, stroke_width=2),
            Line(m_BC, P, stroke_width=2),
            Line(m_AC, P, stroke_width=2),
            Angle.from_three_points(A, m_AB, P, radius=0.2, elbow=True, stroke_width=2),
            Angle.from_three_points(B, m_BC, P, radius=0.2, elbow=True, stroke_width=2),
            Angle.from_three_points(C, m_AC, P, radius=0.2, elbow=True, stroke_width=2)
        )
        self.play(Create(perp_bisector_group))

        circumcenter = Circle(**point_args).move_to(P)
        circumcenter_label = MathTex("O").scale(0.5).move_to(P + [0.2, -0.2, 0])
        circumcircle = Circle(radius=r, color=WHITE, stroke_width=2).move_to(P)
        self.play(Create(circumcenter))
        self.play(FadeOut(perp_bisector_group))
        self.play(Create(circumcircle))
        self.play(Write(circumcenter_label))

        return VGroup(circumcenter, circumcenter_label), P, r

    def centroid(self, A, B, C):
        m_AB = (A + B)/2
        m_BC = (B + C)/2
        m_AC = (A + C)/2
        median_A = Line(A, m_BC, **line_args)
        median_B = Line(B, m_AC, **line_args)
        median_C = Line(C, m_AB, **line_args)

        self.play(Create(median_A), Create(median_B), Create(median_C))
        P = (A + B + C)/3
        centroid = Circle(**point_args).move_to(P)
        centroid_label = MathTex("G").scale(0.5).move_to(P + [0.2, -0.2, 0])
        self.play(Create(centroid))
        self.play(FadeOut(median_A, median_B, median_C))
        self.play(Write(centroid_label))
        return VGroup(centroid, centroid_label)
    
    def orthocenter(self, A, B, C):
        elbow_args = {"stroke_width": 2, "radius": 0.2, "color": WHITE, "elbow": True}
       
        fA = foot_of_perpendicular(B, A,  C)
        fB = foot_of_perpendicular(A, B, C)
        fC = foot_of_perpendicular(A, C, B)
        lA = Line(fA, A, stroke_width=2)
        lB = Line(fB, B, stroke_width=2)
        lC = Line(fC, C, stroke_width=2)
        eA = Angle.from_three_points(B, fA, A, **elbow_args)
        eB = Angle.from_three_points(A, fB, B, **elbow_args)
        eC = Angle.from_three_points(A, fC, C, **elbow_args)

        P = seg_intersect(fA, A, fB, B)

        orthocenter = Circle(**point_args).move_to(P)
        self.play(Create(lA), Create(lB), Create(lC), Create(eA), Create(eB), Create(eC))
        self.play(Create(orthocenter))
        #self.play(FadeOut(lA, lB, lC, eA, eB, eC))
        orthocenter_label = MathTex("H").scale(0.5).move_to(P + [0.2, -0.2, 0])
        self.play(Write(orthocenter_label))
        return VGroup(orthocenter, orthocenter_label), P

    def nine_point_center(self, O, H, R):
        center = (O + H)/2
        nine_point_center = Circle(**point_args).move_to(center)
        nine_point_center_label = MathTex("E").scale(0.5).move_to(center + [0, 0.3, 0])
        lines = VGroup(
            Line(O, center, stroke_width=2),
            Line(H, center, stroke_width=2)
        )


        nine_point_circle = Circle(radius=R/2, color=WHITE, stroke_width=2).move_to(center)
        nine_point_radius = Line(center, center + ([1,1,0]/np.sqrt(2))*R/2, stroke_width=2)
        self.play(Create(lines))
        self.play(Create(nine_point_center))
        self.play(FadeOut(lines))
        self.play(Write(nine_point_center_label), Create(nine_point_circle))
        self.play(Create(nine_point_radius))
        radius_label = MathTex("R/2").scale(0.5).move_to(nine_point_radius.get_center() + [-0.1, 0.1, 0])
        self.play(Write(radius_label))
        return VGroup(nine_point_center, nine_point_center_label, nine_point_circle)



    def bisectors(self, A, B, C, P):
        bisectors = VGroup(
            Line(A, P, stroke_width=2), 
            Line(B, P, stroke_width=2), 
            Line(C, P, stroke_width=2)
        )
        bisector_angles = VGroup(
            angle_bisector_equality(C, A, B, P, 1),
            angle_bisector_equality(A, B, C, P, 2),
            angle_bisector_equality(B, C, A, P, 3)
        )
        return bisectors, bisector_angles


class PartE(Scene):
    def new_play(self, *args):
        self.i += 1
        self.remove(self.pagenum)
        self.pagenum = Text(str(self.i)).to_corner(DL)
        self.add(self.pagenum)
        self.old_play(*args)
        
    def construct(self):
        self.i = 0
        self.pagenum = Text("0").to_corner(DL)
        self.old_play = self.play
        #self.play = self.new_play

        # equations
        equation1 = MathTex("2p^2 - 2r^2 - 8Rr ","=", "a^2+b^2+c^2").scale(0.4)
        equation1.to_corner(UR)
        rect1 = SurroundingRectangle(equation1, buff=0.1, color=YELLOW)

        equation2 = MathTex("3MG", "&=", r"MA^2 + MB^2 + MC^2 - \tfrac{1}{3}(AB^2 + AC^2 + BC^2)", **tex_args).scale(0.4)
        equation2.next_to(equation1, DOWN, aligned_edge=RIGHT)
        rect2 = SurroundingRectangle(equation2, buff=0.1)
        
        equation3 = MathTex(r"IG^2 = \frac{5r^2 - p^2 - 16Rr}{9}", **tex_args).to_corner(DL)
        rect3 = SurroundingRectangle(equation3, buff=0.1, color=YELLOW)

        self.add(equation1, rect1, equation2, rect2, equation3, rect3)



        A = np.array([2, 2, 0])
        B = np.array([0, -1.5, 0])
        C = np.array([6, -1.5, 0])
        triangle = Polygon(A, B, C)
        self.play(Create(triangle))
        incenter = self.incenter(A, B, C)
        circumcenter, O, R = self.circumcenter(A, B, C)
        centroid = self.centroid(A, B, C)
        orthocenter, H = self.orthocenter(A, B, C)
        nine_point_center = self.nine_point_center(O, H, R)

        excircles = self.excircles(A, B, C)
        self.play(FadeOut(excircles))

        t1 = MathTex(r"3MG^2 = MA^2 + MB^2 + MC^2 - \frac{1}{3}(AB^2+AC^2+BC^2)").scale(0.5).to_corner(UL)
        self.play(FadeOut(rect2))
        self.play(Transform(equation2, t1))
        self.wait(5)
        self.remove(equation2)

        t2 = MathTex(r"OG^2 = R^2 - \frac{1}{9}(a^2+b^2+c^2()").scale(0.5).next_to(t1, DOWN, **align_args)
        self.play(Write(t2))
        self.wait(5)

        t3 = MathTex(r"AE = \frac{1}{2}\sqrt{2AH^2+2AO^2-2HO^2}").scale(0.5).next_to(t2, DOWN, **align_args)
        self.play(Write(t3))
        self.wait(5)

        t4 = MathTex("OH = 3GO").scale(0.5).next_to(t3, DOWN, **align_args)
        self.play(Write(t4))
        self.wait(5)

        t41 = MathTex("OH^2 = 9GO^2").scale(0.5).next_to(t3, DOWN, **align_args)
        self.play(TransformMatchingShapes(t4, t41))
        self.wait(5)

        t5 = MathTex("AO = R").scale(0.5).next_to(t41, DOWN, **align_args)
        self.play(Write(t5))
        self.wait(5)

        t6 = MathTex(r"AH = 2R\cos(\angle A)").scale(0.5).next_to(t5, DOWN, **align_args)
        self.play(Write(t6))
        self.wait(5)

        t7 = MathTex(
            r"AE = \frac{1}{2} \sqrt{R^2 + c^2 + b^2 - a^2} = \frac{1}{2}\sqrt{R^2+2bc\cos(\angle A)}\\",
            r"BE = \frac{1}{2} \sqrt{R^2 + c^2 + a^2 - b^2} = \frac{1}{2}\sqrt{R^2+2ac\cos(\angle B)}\\",
            r"CE = \frac{1}{2} \sqrt{R^2 + a^2 + b^2 - c^2} = \frac{1}{2}\sqrt{R^2+2ab\cos(\angle C)}\\"
        ).scale(0.5).next_to(t6, DOWN, **align_args)
        self.play(Write(t7[0]))
        self.wait(5)
        self.play(Write(t7[1:]))
        self.wait(5)

        self.play(FadeOut(t1, t2, t3, t41, t5, t6), t7.animate.to_corner(UL))
        self.wait(5)

        t8 = MathTex(r"IM^2 = \frac{aAM^2 + bBM^2 + cCM^2 - abc}{a+b+c}").scale(0.5).next_to(t7, DOWN, **align_args)
        self.play(Write(t8))
        self.wait(5)
        t81 = MathTex(
            r"I_1M^2 &= \frac{-aAM^2 + bBM^2 + cCM^2 + abc}{-a+b+c}\\",
            r"I_2M^2 &= \frac{aAM^2 - bBM^2 + cCM^2 + abc}{a-b+c}\\",
            r"I_3M^2 &= \frac{aAM^2 + bBM^2 - cCM^2 + abc}{a+b-c}"        
        ).scale(0.5).next_to(t7, DOWN, **align_args)
        self.play(TransformMatchingShapes(t8, t81[0]))
        self.wait(5)
        self.play(Write(t81[1:]))
        self.wait(5)

        t9 = MathTex(r"I_1E^2 = \frac{-aAE^2 + bBE^2 + cCE^2 + abc}{-a+b+c}").scale(0.5).next_to(t7, DOWN, **align_args)
        self.play(FadeOut(t81[1:]))
        self.play(TransformMatchingShapes(t81[0], t9))
        self.wait(5)

        t10 = MathTex(
            r"I_1E^2 = \frac{\frac{R^2}{4}(-a+b+c) + \frac{abc}{2}(\cos(\angle A) + \cos(\angle B) + \cos(\angle C)) + abc}{-a + b + c}",
        ).scale(0.5).next_to(t7, DOWN, **align_args)
        self.play(TransformMatchingShapes(t9, t10))
        self.wait(5)

        t11 = MathTex(
            r"I_1E^2 &= (\frac{R}{2}+r_1)^2",
        ).scale(0.5).next_to(t10, DOWN, **align_args)
        self.play(Write(t11))
        self.wait(5)
        self.play(FadeOut(t10, t7), t11.animate.scale(2).to_corner(UL))
        t12 = MathTex(
            r"I_1E &= \frac{R}{2}+r_1\\",
            r"I_2E &= \frac{R}{2}+r_2\\",
            r"I_3E &= \frac{R}{2}+r_3",
        ).to_corner(UL)
        self.play(TransformMatchingShapes(t11, t12[0]))
        self.wait(5)
        self.play(Write(t12[1:]))
        self.wait(5)
        self.play(FadeIn(excircles))
        


    def incenter(self, A, B, C):


        x, y, r = calculate_incircle(A, B, C)
        P = np.array([x, y, 0])
        I = P
        bisectors, bisector_angles = self.bisectors(A, B, C, P)

        incenter = Circle(**point_args).move_to(P)
        incenter_label = MathTex("I").scale(0.5).move_to(P + [0, -0.2, 0])
        incircle = Circle(radius=r, color=WHITE, stroke_width=2).move_to(P)
        elbow_args = {"stroke_width": 2, "radius": 0.2, "color": WHITE, "elbow": True}
        perp_args = {"stroke_width": 2, "color": WHITE}
        E = foot_of_perpendicular(B, I, C)
        IE = Line(E, I, **perp_args)
        IE_angle = Angle.from_three_points(C, E, I, **elbow_args)
        E_label = MathTex("E").move_to(E + [0, -0.3, 0])

        F = foot_of_perpendicular(A, I, C)
        IF = Line(F, I, **perp_args)
        IF_angle = Angle.from_three_points(A, F, I, **elbow_args)
        F_label = MathTex("F").move_to(F + [0.3, 0.3, 0])

        G = foot_of_perpendicular(B, I, A)
        IG = Line(G, I, **perp_args)
        IG_angle = Angle.from_three_points(A, G, I, **elbow_args)
        G_label = MathTex("G").move_to(G + [-0.3, 0.3, 0])

        self.play(Create(bisectors))
        self.play(Create(bisector_angles))
        self.play(Create(incenter))
        self.play(Create(incircle))
        self.play(Write(incenter_label))

        self.play(Create(IE), Create(IF), Create(IG), Write(E_label), Write(F_label), Write(G_label), Create(IE_angle), Create(IF_angle), Create(IG_angle))

        
        AG = Line(A, G, color=YELLOW, stroke_width=3)
        AF = Line(A, F, color=YELLOW, stroke_width=3)
        BG = Line(B, G, color=BLUE, stroke_width=3)
        BE = Line(B, E, color=BLUE, stroke_width=3)
        CE = Line(C, E, color=GREEN, stroke_width=3)
        CF = Line(C, F, color=GREEN, stroke_width=3)

        self.play(FadeOut(self.triangle), Create(AG), Create(AF), Create(BG), Create(BE), Create(CE), Create(CF))

    def incenter(self, A, B, C):

        x, y, r = calculate_incircle(A, B, C)
        P = np.array([x, y, 0])

        bisectors, bisector_angles = self.bisectors(A, B, C, P)

        self.play(Create(bisectors))
        self.play(Create(bisector_angles))
        incenter = Circle(**point_args).move_to(P)
        self.play(Create(incenter))
        self.play(FadeOut(bisectors, bisector_angles))
        incenter_label = MathTex("I").scale(0.5).move_to(P + [0, -0.2, 0])
        incircle = Circle(radius=r, color=WHITE, stroke_width=2).move_to(P)
        self.play(Create(incircle))
        self.play(Write(incenter_label))
        return VGroup(incenter, incenter_label)
         
    def circumcenter(self, A, B, C):
        x, y, r = calculate_circumcircle(A, B, C)
        P = np.array([x, y, 0])

        m_AB = (A + B)/2
        m_BC = (B + C)/2
        m_AC = (A + C)/2

        perp_bisector_group = VGroup(
            Line(m_AB, P, stroke_width=2),
            Line(m_BC, P, stroke_width=2),
            Line(m_AC, P, stroke_width=2),
            Angle.from_three_points(A, m_AB, P, radius=0.2, elbow=True, stroke_width=2),
            Angle.from_three_points(B, m_BC, P, radius=0.2, elbow=True, stroke_width=2),
            Angle.from_three_points(C, m_AC, P, radius=0.2, elbow=True, stroke_width=2)
        )
        self.play(Create(perp_bisector_group))

        circumcenter = Circle(**point_args).move_to(P)
        circumcenter_label = MathTex("O").scale(0.5).move_to(P + [0.2, -0.2, 0])
        self.play(Create(circumcenter))
        self.play(FadeOut(perp_bisector_group))
        self.play(Write(circumcenter_label))

        return VGroup(circumcenter, circumcenter_label), P, r

    def centroid(self, A, B, C):
        m_AB = (A + B)/2
        m_BC = (B + C)/2
        m_AC = (A + C)/2
        line_args = {"stroke_width": 2, "color": WHITE}
        median_A = Line(A, m_BC, **line_args)
        median_B = Line(B, m_AC, **line_args)
        median_C = Line(C, m_AB, **line_args)

        self.play(Create(median_A), Create(median_B), Create(median_C))
        P = (A + B + C)/3
        centroid = Circle(**point_args).move_to(P)
        centroid_label = MathTex("G").scale(0.5).move_to(P + [0.2, -0.2, 0])
        self.play(Create(centroid))
        self.play(FadeOut(median_A, median_B, median_C))
        self.play(Write(centroid_label))
        return VGroup(centroid, centroid_label)
    
    def orthocenter(self, A, B, C):
        elbow_args = {"stroke_width": 2, "radius": 0.2, "color": WHITE, "elbow": True}
       
        fA = foot_of_perpendicular(B, A,  C)
        fB = foot_of_perpendicular(A, B, C)
        fC = foot_of_perpendicular(A, C, B)
        lA = Line(fA, A, stroke_width=2)
        lB = Line(fB, B, stroke_width=2)
        lC = Line(fC, C, stroke_width=2)
        eA = Angle.from_three_points(B, fA, A, **elbow_args)
        eB = Angle.from_three_points(A, fB, B, **elbow_args)
        eC = Angle.from_three_points(A, fC, C, **elbow_args)

        P = seg_intersect(fA, A, fB, B)

        orthocenter = Circle(**point_args).move_to(P)
        self.play(Create(lA), Create(lB), Create(lC), Create(eA), Create(eB), Create(eC))
        self.play(Create(orthocenter))
        #self.play(FadeOut(lA, lB, lC, eA, eB, eC))
        orthocenter_label = MathTex("H").scale(0.5).move_to(P + [0.2, -0.2, 0])
        self.play(Write(orthocenter_label))
        return VGroup(orthocenter, orthocenter_label), P

    def nine_point_center(self, O, H, R):
        center = (O + H)/2
        nine_point_center = Circle(**point_args).move_to(center)
        nine_point_center_label = MathTex("E").scale(0.5).move_to(center + [0, 0.3, 0])
        lines = VGroup(
            Line(O, center, stroke_width=2),
            Line(H, center, stroke_width=2)
        )


        nine_point_circle = Circle(radius=R/2, color=WHITE, stroke_width=2).move_to(center)
        nine_point_radius = Line(center, center + ([1,1,0]/np.sqrt(2))*R/2, stroke_width=2)
        self.play(Create(lines))
        self.play(Create(nine_point_center))
        self.play(FadeOut(lines))
        self.play(Write(nine_point_center_label), Create(nine_point_circle))
        return VGroup(nine_point_center, nine_point_center_label, nine_point_circle)

    def bisectors(self, A, B, C, P):
        bisectors = VGroup(
            Line(A, P, stroke_width=2), 
            Line(B, P, stroke_width=2), 
            Line(C, P, stroke_width=2)
        )
        bisector_angles = VGroup(
            angle_bisector_equality(C, A, B, P, 1),
            angle_bisector_equality(A, B, C, P, 2),
            angle_bisector_equality(B, C, A, P, 3)
        )
        return bisectors, bisector_angles
    
    def excircles(self, A, B, C):
        a = np.linalg.norm(B - C)
        b = np.linalg.norm(A - C)
        c = np.linalg.norm(A - B)
        s = (a + b + c)/2
        area = np.sqrt(s*(s-a)*(s-b)*(s-c))
        D = (a*A + b*B - c*C)/(a + b - c)
        E = (a*A - b*B + c*C)/(a - b + c)
        F = (-a*A + b*B + c*C)/(-a + b + c)
        r_d = area/(s-c)
        r_e = area/(s-b)
        r_f = area/(s-a)
        D_circle = Circle(radius=r_d, color=WHITE, stroke_width=2).move_to(D)
        E_circle = Circle(radius=r_e, color=WHITE, stroke_width=2).move_to(E)
        F_circle = Circle(radius=r_f, color=WHITE, stroke_width=2).move_to(F)
        D_dot = Circle(**point_args).move_to(D)
        E_dot = Circle(**point_args).move_to(E)
        F_dot = Circle(**point_args).move_to(F)
        D_label = MathTex("I_1").scale(0.5).move_to(D + [0.2, -0.2, 0])
        E_label = MathTex("I_2").scale(0.5).move_to(E + [0.2, -0.2, 0])
        F_label = MathTex("I_3").scale(0.5).move_to(F + [0.2, -0.2, 0])
        self.play(Create(D_circle), Create(E_circle), Create(F_circle))
        self.play(Create(D_dot), Create(E_dot), Create(F_dot))
        self.play(Write(D_label), Write(E_label), Write(F_label))

        return VGroup(D_circle, E_circle, F_circle, D_label, E_label, F_label, D_dot, E_dot, F_dot)

# Problem 2.26
class rs_equals_K(Scene):
    def construct(self):
        A = np.array([0, 0.5, 0])
        B = np.array([-1, -2.5, 0])
        C = np.array([5, -2.5, 0])

        triangle = Polygon(A, B, C) 
        point_labels = VGroup(
            Tex("A").move_to(A + [0, 0.2, 0]),
            Tex("B").move_to(B + [-0.2, -0.2, 0]),
            Tex("C").move_to(C + [0.2, -0.2, 0]),
        )
        edge_labels = VGroup(
            Tex("a").move_to((B + C) / 2 + [0, -0.2, 0]),
            Tex("b").move_to((A + C) / 2 + [0.2, 0.2, 0]),
            Tex("c").move_to((A + B) / 2 + [-0.2, 0, 0]),
        )
        triangle_group = VGroup(triangle, point_labels, edge_labels)
        self.play(Create(triangle_group))

        I, incircle = self.incircle(A, B, C)


        E = foot_of_perpendicular(B, I, C)
        IE = Line(E, I, **perp_args)
        IE_angle = Angle.from_three_points(C, E, I, **elbow_args)
        E_label = MathTex("E").move_to(E + [0, -0.3, 0])

        F = foot_of_perpendicular(A, I, C)
        IF = Line(F, I, **perp_args)
        IF_angle = Angle.from_three_points(A, F, I, **elbow_args)
        F_label = MathTex("F").move_to(F + [0.3, 0.3, 0])

        G = foot_of_perpendicular(B, I, A)
        IG = Line(G, I, **perp_args)
        IG_angle = Angle.from_three_points(A, G, I, **elbow_args)
        G_label = MathTex("G").move_to(G + [-0.3, 0.3, 0])

        self.play(Create(IE), Create(IE_angle), Create(IF), Create(IF_angle), Create(IG), Create(IG_angle), Create(E_label), Create(F_label), Create(G_label))

        AI = DashedLine(A, I, **line_args)
        BI = DashedLine(B, I, **line_args)
        CI = DashedLine(C, I, **line_args)
        self.play(Create(AI), Create(BI), Create(CI))

        t0 = MathTex(r"K_{ABC} = ","K_{IBC} + K_{IAC} + K_{IAB}").to_corner(UL)
        self.play(Create(t0))
        self.wait(5)

        t1 = MathTex(r"K_{IBC}=\frac{1}{2}(IU)(BC)", r"=\frac{1}{2}(r)(a)").next_to(t0, DOWN, **align_args)
        self.play(Create(t1))
        self.wait(5)

        t2 = MathTex(r"K_{IAC}=\frac{1}{2}rb").next_to(t1, DOWN, **align_args)
        t3 = MathTex(r"K_{IAB}=\frac{1}{2}rc").next_to(t2, DOWN, **align_args)
        self.play(Create(t2), Create(t3))

        self.wait(5)

        t4 = MathTex(r"K_{ABC} = \frac{1}{2}ra + \frac{1}{2}rb + \frac{1}{2}rc", 
                     r"= \frac{1}{2}r(a+b+c))", r"=rs").to_corner(UL)
        self.play(FadeOut(t0), Create(t4[0]), FadeOut(t1), FadeOut(t2), FadeOut(t3))
        self.wait(5)

        self.play(Create(t4[1]))
        self.wait(5)
        self.play(Create(t4[2]))
        self.wait(5)


        t5 = MathTex(r"r=\frac{K_{ABC}}{s}",
                     r"=\sqrt{\frac{s(s-a)(s-b)(s-c)}{s}}"
                     ).next_to(t4, DOWN, **align_args)
        self.play(Create(t5[0]))
        self.wait(5)
        self.play(FadeOut(t4))
        self.play(Create(t5[1]))
        self.wait(5)


    def incircle(self, A, B, C):

        x, y, r = calculate_incircle(A, B, C)
        P = np.array([x, y, 0])

        bisectors, bisector_angles = self.bisectors(A, B, C, P)

        self.play(Create(bisectors))
        self.play(Create(bisector_angles))
        P_point = Circle(**point_args).move_to(P)
        P_label = MathTex("I").move_to(P + [0.3, -0.3, 0])
        self.play(Create(P_point))
        self.play(Write(P_label))
        self.play(FadeOut(bisectors, bisector_angles))
        incircle = Circle(radius=r).move_to(P)
        self.play(Create(incircle))
        return P, VGroup(P_point, P_label, incircle)

    def bisectors(self, A, B, C, P):
        bisectors = VGroup(
            Line(A, P, stroke_width=2), 
            Line(B, P, stroke_width=2), 
            Line(C, P, stroke_width=2)
        )
        bisector_angles = VGroup(
            angle_bisector_equality(C, A, B, P, 1),
            angle_bisector_equality(A, B, C, P, 2),
            angle_bisector_equality(B, C, A, P, 3)
        )
        return bisectors, bisector_angles

# Law of cosines
class law_of_cosines(Scene):
    def construct(self):        
        A = np.array([0, 0.5, 0])
        B = np.array([-1, -2.5, 0])
        C = np.array([5, -2.5, 0])
        offset = [1.6,3,0]
        A += offset
        B += offset
        C += offset
        triangle = Polygon(A, B, C) 
        point_labels = VGroup(
            Tex("A").move_to(A + [0, 0.2, 0]),
            Tex("B").move_to(B + [-0.2, -0.2, 0]),
            Tex("C").move_to(C + [0.2, -0.2, 0]),
        )
        edge_labels = VGroup(
            Tex("a").move_to((B + C) / 2 + [0, -0.2, 0]),
            Tex("b").move_to((A + C) / 2 + [0.2, 0.2, 0]),
            Tex("c").move_to((A + B) / 2 + [-0.2, 0, 0]),
        )
        triangle_group = VGroup(triangle, point_labels, edge_labels)
        self.play(Create(triangle_group))
        
        A_foot = foot_of_perpendicular(B,A,C)
        height = DashedLine(A, A_foot, **line_args)
        height_label = MathTex("h").move_to((A + A_foot) / 2 + [0.2, 0, 0])
        P_label = MathTex("P").move_to(A_foot + [0.2, -0.2, 0])
        self.play(Create(height), Create(height_label))

        self.wait(5)

        x_label = MathTex("x").move_to((C + A_foot) / 2 + [0, 0.2, 0])
        self.play(Create(x_label))
        self.wait(5)

        t0 = MathTex(r"\cos(C)=\frac{PC}{AC}=x/b").to_corner(UL)
        self.play(Create(t0))
        self.wait(5)
        t01 = MathTex(r"x = b\cos(C)").next_to(t0, DOWN, **align_args)
        self.play(Create(t01))
        self.play(FadeOut(t0), t01.animate.to_corner(UL))
        self.wait(5)

        t1 = MathTex(r"b^2=x^2+h^2").next_to(t01, DOWN, **align_args)
        t2 = MathTex("c^2=h^2+(a-x)^2").next_to(t1, DOWN, **align_args)
        self.play(Create(t1), Create(t2))
        self.wait(5)

        t3 = MathTex(r"c^2&=(b^2-x^2)+(a-x)^2\\",
                    r"&=(b^2-x^2+a^2-2ax+x^2)\\",
                    r"&=a^2+b^2-2ax=a^2+b^2-2ab\cos(C)\\").next_to(t2, DOWN, **align_args)
        self.play(Create(t3[0]))
        self.wait(1)
        self.play(Write(t3[1]))
        self.wait(1)
        self.play(Write(t3[2]))

# Euler's theorem

class eulers_theorem(Scene):
    def construct(self):

        A = np.array([3, 1, 0])
        B = np.array([2, -1.5, 0])
        C = np.array([6, -1.5, 0])
        triangle = Polygon(A, B, C)
        point_labels = VGroup(
            Tex("A").move_to(A + [0, 0.2, 0]),
            Tex("B").move_to(B + [-0.2, -0.2, 0]),
            Tex("C").move_to(C + [0.2, -0.2, 0]),
        )
        self.play(Create(triangle), Create(point_labels))

        circumcenter, O, R = self.circumcenter(A, B, C)
        centroid, G = self.centroid(A, B, C)

        H = ((G-O)*2) + G 
        H_point = Circle(**point_args).move_to(H)
        H_label = MathTex("H").move_to(H + [-0.2, 0, 0]).scale(0.5)
        euler_line = Line(H, O, **line_args)
        self.play(Create(euler_line), Create(H_point), Create(H_label))
        self.wait(5)

        M = (B + C)/2 
        M_point = Circle(**point_args).move_to(M).scale(0.5)
        M_label = MathTex("M").move_to(M + [0.2, -0.2, 0])
        self.play(Create(M_point), Create(M_label))
        self.wait(5)

        AH = Line(A, H, **line_args)
        AM = Line(A, M, **line_args)
        OM = Line(O, M, **line_args)
        OM_angle = Angle.from_three_points(C, M, O, stroke_width=2, elbow=True, radius=0.1)
        self.play(Create(AH), Create(AM), Create(OM), Create(OM_angle))
        self.wait(5)

        t00 = MathTex(r"AG =2GM").to_corner(UL)
        self.play(Create(t00))
        self.wait(5)

        t0 = MathTex(r"HG = 2OM").next_to(t00, DOWN, **align_args)
        self.play(Create(t0))
        self.wait(5)

        radius=0.2

        t1 = MathTex(r"\angle AGH = \angle MGO").next_to(t0, DOWN, **align_args)
        AGH_angle = Angle.from_three_points(A, G, H, radius=radius, stroke_width=2)
        MGO_angle = Angle.from_three_points(M, G, O, radius=radius, stroke_width=2)
        self.play(Create(AGH_angle), Create(MGO_angle), Create(t1))
        self.wait(5)

        similarity = MathTex(r"\triangle AGH \sim \triangle MGO").next_to(t1, DOWN, **align_args)
        self.play(Create(similarity))
        self.wait(5)

        self.play(similarity.animate.to_corner(UL))
        t2 = MathTex(r"\angle AHO = \angle MOG").next_to(similarity, DOWN, **align_args)
        self.play(FadeOut(t00, t0, t1), Create(t2))
        self.wait(5)
        t3 = MathTex(r"AH \| MO").next_to(t2, DOWN, **align_args)
        self.play(Create(t3))
        self.wait(5)

        t4 = MathTex(r"AH \perp BC").next_to(t3, DOWN, **align_args)
        self.play(Create(t4))
        self.wait(5)

        self.play(FadeOut(AM, euler_line, OM, OM_angle, AGH_angle, MGO_angle, centroid, circumcenter))
        self.wait(5)

        A_foot = foot_of_perpendicular(B,A,C)
        B_foot = foot_of_perpendicular(A,B,C)
        C_foot = foot_of_perpendicular(A,C,B)
        H_A_foot = Line(H, A_foot, **line_args)
        A_foot_angle = Angle.from_three_points(A, A_foot, C, radius=radius, stroke_width=2, elbow=True)
        self.play(Create(H_A_foot), Create(A_foot_angle))
        self.wait(5)
        B_foot_angle = Angle.from_three_points(B, B_foot, A, radius=radius, stroke_width=2, elbow=True)
        C_foot_angle = Angle.from_three_points(C, C_foot, B, radius=radius, stroke_width=2, elbow=True)
        B_altitude = Line(B, B_foot, **line_args)
        C_altitude = Line(C, C_foot, **line_args)
        self.play(Create(B_foot_angle), Create(C_foot_angle), Create(B_altitude), Create(C_altitude))
        self.wait(5)


    def circumcenter(self, A, B, C):
        x, y, r = calculate_circumcircle(A, B, C)
        P = np.array([x, y, 0])

        m_AB = (A + B)/2
        m_BC = (B + C)/2
        m_AC = (A + C)/2

        perp_bisector_group = VGroup(
            Line(m_AB, P, stroke_width=2),
            Line(m_BC, P, stroke_width=2),
            Line(m_AC, P, stroke_width=2),
            Angle.from_three_points(A, m_AB, P, radius=0.2, elbow=True, stroke_width=2),
            Angle.from_three_points(B, m_BC, P, radius=0.2, elbow=True, stroke_width=2),
            Angle.from_three_points(C, m_AC, P, radius=0.2, elbow=True, stroke_width=2)
        )
        self.play(Create(perp_bisector_group))

        circumcenter = Circle(**point_args).move_to(P)
        circumcenter_label = MathTex("O").scale(0.5).move_to(P + [0.2, -0.2, 0])
        self.play(Create(circumcenter))
        self.play(FadeOut(perp_bisector_group))
        self.play(Write(circumcenter_label))

        return VGroup(circumcenter, circumcenter_label), P, r

    def centroid(self, A, B, C):
        m_AB = (A + B)/2
        m_BC = (B + C)/2
        m_AC = (A + C)/2
        line_args = {"stroke_width": 2, "color": WHITE}
        median_A = Line(A, m_BC, **line_args)
        median_B = Line(B, m_AC, **line_args)
        median_C = Line(C, m_AB, **line_args)

        self.play(Create(median_A), Create(median_B), Create(median_C))
        P = (A + B + C)/3
        centroid = Circle(**point_args).move_to(P)
        centroid_label = MathTex("G").scale(0.5).move_to(P + [-0.2, -0.2, 0])
        self.play(Create(centroid))
        self.play(FadeOut(median_A, median_B, median_C))
        self.play(Write(centroid_label))
        return VGroup(centroid, centroid_label), P
    

# Heron's formula
class herons_formula(Scene):
    def construct(self):
        A = np.array([0, 0.5, 0])
        B = np.array([-1, -2.5, 0])
        C = np.array([5, -2.5, 0])
        offset = [0,-0.5,0]
        A += offset
        B += offset
        C += offset
        triangle = Polygon(A, B, C) 
        point_labels = VGroup(
            Tex("A").move_to(A + [0, 0.2, 0]),
            Tex("B").move_to(B + [-0.2, -0.2, 0]),
            Tex("C").move_to(C + [0.2, -0.2, 0]),
        )
        edge_labels = VGroup(
            Tex("a").move_to((B + C) / 2 + [0, -0.2, 0]),
            Tex("b").move_to((A + C) / 2 + [0.2, 0.2, 0]),
            Tex("c").move_to((A + B) / 2 + [-0.2, 0, 0]),
        )

        self.play(Create(triangle), Create(point_labels), Create(edge_labels))
        self.wait(5)

        t0 = MathTex(r"K=",r"\frac{1}{2}ab\sin(C)").to_corner(UL)
        self.play(Create(t0))
        self.wait(5)
        t01 = MathTex(r"4K^2=",r"a^2b^2\sin^2(C)").to_corner(UL)
        self.play(TransformMatchingShapes(t0, t01))
        self.wait(5)
        t02 = MathTex(r"4K^2=",r"a^2b^2(1-\cos^2(C))").to_corner(UL)
        self.play(TransformMatchingShapes(t01, t02))
        self.wait(5)
        
        t1 = MathTex(r"c^2=a^2+b^2-2ab\cos(C)").next_to(t0, DOWN, **align_args)
        self.play(Create(t1))
        t11 = MathTex(r"\cos(C) =\frac{c^2-a^2-b^2}{2ab}").next_to(t0, DOWN, **align_args)
        self.play(TransformMatchingShapes(t1, t11))
        self.wait(5)

        t2 = MathTex(r"4K^2=",r"a^2b^2\left(1-\frac{(c^2-a^2-b^2)^2}{4a^2b^2}\right)").to_corner(UL)
        self.play(TransformMatchingShapes(VGroup(t02, t11), t2))
        self.wait(5)

        t3 = MathTex(r"4K^2=",r"a^2b^2-\frac{(c^2-a^2-b^2)^2}{4}").to_corner(UL)
        self.play(TransformMatchingShapes(t2, t3))
        self.wait(5)

        t4 = MathTex(r"16K^2&=4a^2b^2-(c^2-a^2-b^2)^2\\",
                     r"&=[2ab+(c^2-a^2-b^2)][2ab-(c^2-a^2-b^2)]\\",
                     r"&=[(c^2(a-b)^2)][(a+b)^2-c^2]\\",
                     r"&=[c+(a-b)][c-(a-b)][(a+b)+c][(a+b)-c]"                 
                     
                     ).to_corner(UL)
        self.play(TransformMatchingShapes(t3, t4[0]))
        self.wait(5)
        self.play(Create(t4[1]))
        self.wait(5)
        self.play(Create(t4[2]))
        self.wait(5)
        self.play(Create(t4[3]))
        self.wait(5)
        t5 = MathTex(r"16K^2=[c+(a-b)][c-(a-b)][(a+b)+c][(a+b)-c]").to_corner(UL)
        self.play(TransformMatchingShapes(VGroup(t4[0], t4[3]), t5), FadeOut(t4[1],t4[2]))
        self.wait(5)
        t6 = MathTex(r"s=\frac{a+b+c}{2}").next_to(t5, DOWN, **align_args)
        self.play(Create(t6))
        self.wait(5)

        t7 = MathTex("c+(a-b)=c+a-b = (a+b+c)-2b = 2s-2b=2(s-b)").next_to(t6, DOWN, **align_args)
        self.play(Create(t7))
        self.wait(5)
        t8 = MathTex("b+c-a = 2(s-a)").next_to(t7, DOWN, **align_args)
        t9 = MathTex("a+b-c = 2(s-c)").next_to(t8, DOWN, **align_args)
        t10 = MathTex("a+b+c = 2s").next_to(t9, DOWN, **align_args)
        self.play(Create(t8),Create(t9), Create(t10))
        self.wait(5)

        t11 = MathTex("16K^2 =2(s-a)2(s-b)2(s-c)2s").to_corner(UL)
        self.play(FadeOut(t5), FadeOut(t6,t7,t8,t9,t10), Create(t11))
        self.wait(5)

        t12 = MathTex("K^2 =s(s-a)(s-b)(s-c)").to_corner(UL)
        self.play(TransformMatchingShapes(t11, t12))
        self.wait(5)

        

def angle_bisector_equality(B, A, C, P, n):
        angle_group = VGroup()
        for i in range(n):
            radius = 0.3 + 0.05 * i
            BAP = Angle.from_three_points(B, A, P, radius=radius, other_angle=True, stroke_width=2)
            CAP = Angle.from_three_points(C, A, P, radius=radius, stroke_width=2)
            angle_group.add(BAP, CAP)
        return angle_group

def calculate_incircle(a, b, c):
    # `d`, `e`, `f` are the side lengths of the triangle
    d = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    e = math.sqrt((c[0] - b[0])**2 + (c[1] - b[1])**2)
    f = math.sqrt((c[0] - a[0])**2 + (c[1] - a[1])**2)

    # `s` is the semiperimeter of the triangle
    s = (d + e + f) / 2

    # `r` is the radius of the incircle
    r = math.sqrt(((s - d)*(s - e)*(s - f)) / s)

    # `x`, `y` are the coordinates of the center of the incircle
    x = ((e * a[0]) + (f * b[0]) + (d * c[0])) / (d + e + f)
    y = ((e * a[1]) + (f * b[1]) + (d * c[1])) / (d + e + f)

    return (x, y, r)

def calculate_circumcircle(A, B, C):
    m_AB = (A[1] - B[1]) / (A[0] - B[0])
    m_BC = (B[1] - C[1]) / (B[0] - C[0])

    x = (m_AB * m_BC * (A[1] - C[1]) + m_BC * (A[0] + B[0]) - m_AB * (B[0] + C[0])) / (2 * (m_BC - m_AB))
    y = -1 * (x - (A[0] + B[0]) / 2) / m_AB + (A[1] + B[1]) / 2
    r = math.sqrt((x - A[0])**2 + (y - A[1])**2)

    return x, y, r

def foot_of_perpendicular(A, B, C):
    """Return the foot of perpendicular from A to line BC."""
    AB = B - A
    AC = C - A
    return A + np.dot(AB, AC) / np.dot(AC, AC) * AC

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def perp( a ) :
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

# line segment a given by endpoints a1, a2
# line segment b given by endpoints b1, b2
# return 
def seg_intersect(a1,a2, b1,b2) :
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = np.dot( dap, db)
    num = np.dot( dap, dp )
    return (num / denom.astype(float))*db + b1
